# 🔎 Get Person's DIAN Rut Status by TIN 📑🇨🇴

 ![PyPi version](https://badgen.net/pypi/v/dian-person-rut-status/)

This module allows you to retrieve a person's DIAN RUT status by providing their TIN (NIT in Spanish) through [DIAN's public official website](https://muisca.dian.gov.co/WebRutMuisca/DefConsultaEstadoRUT.faces). It is implemented as a function that operates synchronously within the [requests library](https://requests.readthedocs.io/en/latest/). Currently, it is an early version, so I consider it as a Minimum Viable Product (MVP) which is ready to be used.


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
