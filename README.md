# dimedbpy
Python wrapper for the DimeDB REST API. 

## Example usage

```python

from dimedbpy import get_metabolites

metabolites = get_metabolites("DOUMFZQKYFQNTF-WUTVXBCWSA-N")

for metabolite in metabolites:
    print metabolite.name

```