# dimedbpy: Python wrapper for DIMEdb's REST API

dimedbpy provides a way to interact with the DIMEdb web service in Python. It provides metabolite queries by name, structure, and adduct information.

Here's a quick example, showing how to retrieve metabolites by its name:

```python

from dimedbpy import get_metabolites

metabolites = get_metabolites("name", "Caffeine")

for metabolite in metabolites:
    print metabolite.adducts

```

## Installation

### Clone the repository

Install dimedbpy using ```python-pip```:

```
pip install dimedbpy
```

Or clone the latest development version of dimedbpy from GitHub. This version may not be 100% stable, but will include new features that have yet to be released.

```
git clone https://www.github.com/KeironO/dimedbpy
cd dimedbpy
python setup.py install
```
