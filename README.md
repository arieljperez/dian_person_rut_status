# 🔎 Get Person's DIAN Rut Status by TIN 📑🇨🇴

 ![PyPi version](https://badgen.net/pypi/v/dian-person-rut-status/)

This is a module that allows you to get a person's DIAN RUT status by its TIN (NIT in Spanish) through [DIAN's public official website](https://muisca.dian.gov.co/WebRutMuisca/DefConsultaEstadoRUT.faces). It is implemented as a sync function under the [requests library](https://requests.readthedocs.io/en/latest/). Currently, this is an early MVP ready to use. 

## DIAN Public official site
The public oficial can be [found here](https://muisca.dian.gov.co/WebRutMuisca/DefConsultaEstadoRUT.faces).

## Installation

```bash
pip install dian_person_rut_status
```

## Usage

Once the package is installed.

```python
from dian_person_rut_status import muisca


person_rut_status = muisca.get_person_rut_status(tin="Colombian Person TIN")
```

The __'tin'__ in this context refers to the __Colombia Unique Taxpayer Number__, a unique identifier assigned to individuals obligated to pay taxes. It is important to note that the __'tin'__ should be provided without its __check digit__


## Expected Responses

```python
from dian_person_rut_status import muisca

person_rut_status = muisca.get_person_rut_status(tin="Colombian Person TIN")

```