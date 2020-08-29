# dimedbpy: Python wrapper for the DIMEdb REST API

[![Project Status: Active - The project has reached a stable, usable state and is being actively developed.](http://www.repostatus.org/badges/0.1.0/active.svg)](http://www.repostatus.org/#active)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dimedbpy.svg)
![PyPI](https://img.shields.io/pypi/v/dimedbpy.svg)
![PyPI - License](https://img.shields.io/pypi/l/dimedbpy.svg)
![PyPI - Status](https://img.shields.io/pypi/status/dimedbpy.svg)
[![Build Status](https://travis-ci.org/AberystwythSystemsBiology/dimedbpy.svg?branch=master)](https://travis-ci.org/AberystwythSystemsBiology/dimedbpy)

<a href="https://www.github.com/KeironO/dimedbpy"><img src="http://svgshare.com/i/2uc.svg" align="left" hspace="10" vspace="6"></a>

dimedbpy provides a way to interact with the DIMEdb web service in Python. It provides metabolite queries by name, structure, and isotope information.

Here's a quick example, showing how to retrieve metabolites by its name:

```python

from dimedbpy import get_metabolites

metabolites = get_metabolites("name", "Caffeine")

for metabolite in metabolites:
    print(metabolite.isotopic_distributions)
```

## Resources
* [DIMEdb Help Page](http://dimedb.ibers.aber.ac.uk/help)
* [Wiki](https://github.com/KeironO/dimedbpy/wiki)

## License
Code released under [the MIT license](https://github.com/KeironO/dimedbpy/blob/master/LICENSE).
