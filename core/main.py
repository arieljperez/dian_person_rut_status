from typing import Union, Dict

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

import os

FORM_CLASS_INFO = '.tipoFilaNormalVerde'

TOKEN_FIELD = 'com.sun.faces.VIEW'

FORM_PREFIX = 'vistaConsultaEstadoRUT:formConsultaEstadoRUT'

TOKEN = os.environ.get('TOKEN')

VALUE_ATTR = 'value'

NATURAL_PERSON_VALUES = ['primerNombre', 'otrosNombres', 'primerApellido', 'segundoApellido']

PERSON_MAIN_VALUES_KEYS = [ 'dv', 'status', 'name']

PERSON_VALUES_KEYS = ['nit', *PERSON_MAIN_VALUES_KEYS]

WEB_RUT_MUISCA_URL = 'https://muisca.dian.gov.co/WebRutMuisca/DefConsultaEstadoRUT.faces'

DEFAULT_TIMEOUT = 10

DEFAULT_ATTEMPTS = 5

def remove_none_elements_from_dict(d: dict) -> Dict:
    return {key: value for key, value in d.items() if value is not None and value != ''}


def list_contains_elements_of_list(a:list, b:list)->bool:
    return  all(item in a for item in b)


def as_form_field(field_name:str='')->str:
    return FORM_PREFIX + ':' + field_name if field_name else FORM_PREFIX

def get_value_from_tag(tag:Tag, value:str)->Union[str, None]:
    return tag.contents[0] if tag.contents else tag.attrs.get(value, None)


def find_value_in_soup(soup:BeautifulSoup, value:str)->Union[str, None]:
    if not (tag := soup.find(attrs={'id': as_form_field(value)})):
        return
    
    return get_value_from_tag(tag=tag, value=VALUE_ATTR)

def concat_full_name_by_name_strings(names:list)->Union[str, None]:
    return ' '.join(names) if all(names) else None


def get_person_name_from_soup(soup:BeautifulSoup):
    
    if name := find_value_in_soup(soup=soup, value='razonSocial'):
        return name
    
    return concat_full_name_by_name_strings([find_value_in_soup(soup=soup, value=value) for value in NATURAL_PERSON_VALUES])

    
def get_person_data_from_soup(soup:BeautifulSoup):
    
    person_data = {PERSON_VALUES_KEYS[0]: find_value_in_soup(soup=soup, value='numNit'),
                     PERSON_VALUES_KEYS[1]: find_value_in_soup(soup=soup, value='dv'),
                     PERSON_VALUES_KEYS[2]: find_value_in_soup(soup=soup, value='estado'),
                     PERSON_VALUES_KEYS[3]: get_person_name_from_soup(soup=soup)}
    
    person_data = remove_none_elements_from_dict(d=person_data)
    
    return person_data if list_contains_elements_of_list(a=list(person_data.keys()), b=PERSON_MAIN_VALUES_KEYS) else None 


PAYLOAD_DATA = {as_form_field('modoPresentacionSeleccionBO'): 'pantalla',
                as_form_field('siguienteURL'): '',
                as_form_field('modoPresentacionFormBO'): 'pantalla',
                as_form_field('modoOperacionFormBO'): '',
                as_form_field('mantenerCriterios'): '',
                as_form_field('btnBuscar.x'): 48,
                as_form_field('btnBuscar.y'): 11,
                TOKEN_FIELD: TOKEN,
                as_form_field(): 'vistaConsultaEstadoRUT:formConsultaEstadoRUT',
                as_form_field('_idcl'): '',
                }



def get_person_info(nit:str, attempts:int=DEFAULT_ATTEMPTS, timeout:int=DEFAULT_TIMEOUT)->Union[Dict, None]:
    
    if attempts == 0:
        return None
    
    try:
        response = requests.post(url=WEB_RUT_MUISCA_URL, data={**PAYLOAD_DATA, as_form_field('numNit'): nit}, timeout=timeout)
    except (Exception, requests.Timeout) as possible_errors:
        return get_person_info(nit=nit, attempts=DEFAULT_ATTEMPTS-1)
    
    soup = BeautifulSoup(response.text, features='html.parser') if response else None
    
    if not soup:
        return
    
    return get_person_data_from_soup(soup=soup)