'''
DimeDBPy

Python interface for the DimeDB REST service.
https://github.com/KeironO/dimedbpy
'''

__author__ = "Keiron O'Shea"
__email__ = "keo7@aber.ac.uk"
__version__ = "0.0.1a"
__license__ = "MIT"

API_BASE = "http://0.0.0.0:5000/api/metabolites?where={%(search_param)s}"

import requests
from Metabolite import Metabolite
PROPERTY_MAP = {
    'molecular_formula' : '"Identification Information.Molecular Formula"',
    'inchikey' : '"_id"'
}

def request(identifier, namespace):
    sp = PROPERTY_MAP[namespace] + ': "'+ identifier + '"'
    url = API_BASE % dict(search_param=sp)
    return requests.get(url)

def get_json(identifier, namespace):
    try:
        response = request(identifier, namespace)
        if response.status_code == 200:
            return response.json()["_items"]
    except Exception, e:
        print e
        return None

def metabolites_to_frame(metabolites):
    import pandas as pd
    return pd.DataFrame.from_records([m.to_dict() for m in metabolites], index="_id")

def get_metabolites(identifier, namespace="inchikey", as_dataframe=False):
    results = get_json(identifier, namespace)
    metabolites = [Metabolite(r) for r in results if r != None]
    if as_dataframe:
        return metabolites_to_frame(metabolites)
    return metabolites

if __name__ == "__main__":
    print get_metabolites("DOUMFZQKYFQNTF-WUTVXBCWSA-N", as_dataframe=True)
