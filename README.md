# 🔎 Get Person's DIAN Rut Status by NIT 📑🇨🇴

 ![PyPi version](https://badgen.net/pypi/v/dian-person-rut-status/)

This is a module that allows you to get a person's DIAN Rut status by its NIT through [DIAN's public official website](https://muisca.dian.gov.co/WebRutMuisca/DefConsultaEstadoRUT.faces). It is implemented as a sync function under the [requests library](https://requests.readthedocs.io/en/latest/). Currently, this is an early MVP ready to use. 

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


person_rut_status = muisca.get_person_rut_status(nit="Person NIT")
```

Where the __nit__ argument represents the __Colombia Unique Taxpayer Number__ , which is a number assigned to persons who must pay taxes. The __nit__ must be without its __check digit__.


## Expected Responses

```python
from dian_person_rut_status import muisca

person_rut_status = muisca.get_person_rut_status(nit="Person NIT")

```