# dimedbpy: Python wrapper for the DIMEdb REST API

[![Project Status: Active - The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/0.1.0/active.svg)](http://www.repostatus.org/#active)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dimedbpy.svg)
![PyPI](https://img.shields.io/pypi/v/dimedbpy.svg)
![PyPI - License](https://img.shields.io/pypi/l/dimedbpy.svg)
![PyPI - Status](https://img.shields.io/pypi/status/dimedbpy.svg)
[![Build Status](https://travis-ci.org/AberystwythSystemsBiology/dimedbpy.svg?branch=master)](https://travis-ci.org/AberystwythSystemsBiology/dimedbpy)

<a href="https://www.github.com/KeironO/dimedbpy"><img src="http://svgshare.com/i/2uc.svg" align="left" hspace="10" vspace="6"></a>

dimedbpy provides a quick and easy way to interact with the DIMEdb web service through Python. It provides metabolite queries by name, structure, and isotope information.

## Installation

DIMEpy requires Python 3+ and is unfortunately not compatible with Python 2. If you are still using Python 2, a clever workaround is to install Python 3 and use that instead.

You can install it through pypi using pip:

```
pip install dimedbpy
```

If you want the 'bleeding edge' version, you can also install directly from this repository using git - but beware of dragons:

```
pip install git+https://www.github.com/AberystwythSystemsBiology/dimedbpy
```

## Usage

### Simple Search

Here's a quick example, showing how to retrieve metabolites by name. Note that `name` is the namespace and `Sucrose` is the search value:

```python

from dimedbpy import get_metabolites

metabolites = get_metabolites("name", "Sucrose")

for metabolite in metabolites:
    print(metabolite.name)
```

The following namespaces are supported:


**Namespace** | **API Translation** | **Descripton** | **Example**
--- | --- | --- | ---
`inchikey` | `"Identification Information.Name"` | Compiled InChIKey | CZMRCDWAGMRECN-UGDNZRGBSA-N
`name` | `"Identification Information.Name"` | Common name | Sucrose
`molecular_formula` | `"Identification Information.Molecular Formula"` | Textual description of elemental composition |  C12H22O11
`smiles` | `"Identification Information.SMILES"` | Isometric SMILES | Too long.
`inchi` | `"Identification Information.InChI"` | Unique InChI identifier | Too long.
`kegg` | `"External Sources.KEGG Compound"` | KEGG Compound Identifier | C00089
`pubchem` | `"External Sources.PubChem"` | PubChem Identifier | 5988
`cas` | `"External Sources.CAS"` | CAS Registry Number | 57-50-1
`hmdb` | `"External Sources.HMDB Accession"` | HMDB Accession Number | HMDB00258
`chemspider` | `"External Sources.Chemspider"` | Chemspider Identifier | 5768
`biocyc` | `"External Sources.BioCyc"` | Bio/MetaCyc Identifier | SUCROSE
`chebi` | `"External Sources.ChEBI"` | ChEBI Identifier | 17992



### Mass Search

You can search for metabolites easily through the `mass_search` method.

Here's a simplified example:

```python
import dimedbpy

metabolites = = dimedbpy.mass_search(
                    mass=420.69,
                    polarity="positive",
                    tolerance=0.25,
                    isotopic_distributions=[
                    "[M-H]1-", "[M+Cl]1-", "[M+Br]1-"
                    ]
                )
```


This is pretty self-explanatory.

There's a `as_dataframe` parameter you can use to output it as a pandas dataframe.

> ***Note:*** If nothing is passed to the `isotopic_distributions` parameter, then sane defaults are used (Negative: [M-H]1-, [M+Cl]1-, M+Br]1 and Positive: [M+H]1+, [M+K]1+, [M+Na]1+)

### Metabolite Object

As noted previously, both the `get_metabolites()` and `mass_search()` methods returns a list of `Metabolite` objects.

If you already know the InChIKey of the metabolite you're interested in - it is possible to instantiate a Metabolite instantly using the `from_inchikey` method.

```python
from dimedbpy import Metabolite

metabolite = Metabolite.from_inchikey("DOUMFZQKYFQNTF-WUTVXBCWSA-N")
```

In addition to this, For ease of access `Metabolite` contains a `_record` property which represents a Python dictionary that contains all of the data about the Metabolite.

Moreover, the `to_dict()` class method returns a simplified dictionary representation of the aforementioned data. Through this method it is also possible to list the desired properties to obtain, for example:

```python
from dimedbpy import Metabolite

metabolite = Metabolite.from_inchikey("DOUMFZQKYFQNTF-WUTVXBCWSA-N")

metabolite.to_dict(properties=["Name", "Synonyms", "Molecular Formula"])
```


## Bug reporting and feature suggestions

Please report all bugs or feature suggestions to the issues tracker. **Please do not email me directly**.

We welcome all sorts of contribution, so please be as candid as you want(!)

## Resources
* [DIMEdb Home Page](https://dimedb.ibers.aber.ac.uk/)
* [DIMEdb Help Page](https://dimedb.ibers.aber.ac.uk/help)

## License
dimedbpy is released under the terms of the permissive [MIT license](https://github.com/KeironO/dimedbpy/blob/master/LICENSE).
