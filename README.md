# dimedbpy: Python wrapper for DIMEdb's REST API

dimedbpy provides a way to interact with the DIMEdb web service in Python. It provides metabolite queries by name, structure, and adduct information.

Here's a quick example, showing how to retrieve metabolites by id (InChIKey):

```python

from dimedbpy import get_metabolites

metabolites = get_metabolites("DOUMFZQKYFQNTF-WUTVXBCWSA-N")

for metabolite in metabolites:
    print metabolite.name

```

## Installation

### Clone the repository

```
git clone https://www.github.com/KeironO/dimedbpy
cd dimedbpy
python setup.py install
```