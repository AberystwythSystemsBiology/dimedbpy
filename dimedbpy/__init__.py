'''
dimedbpy

Python interface for the DIMEdb REST service.
https://github.com/KeironO/dimedbpy
'''

__author__ = "Keiron O'Shea"
__email__ = "keo7@aber.ac.uk"
__version__ = "0.0.1a"
__license__ = "MIT"

API_BASE = "http://dimedb.ibers.aber.ac.uk/api/metabolites?where={%(search_param)s}"

import requests
from Metabolite import Metabolite

PROPERTY_MAP = {
    'inchikey': '"_id"',
    'name' : '"Identification Information.Name"',
    'molecular_formula' : '"Identification Information.Molecular Formula"',
    'smiles' : '"Identification Information.SMILES"',
    'inchi' : '"Identification Information.InChI"',
    'kegg' : '"External Sources.KEGG Compound"',
    'pubchem' : '"External Sources.PubChem"',
    'cas' : '"External Sources.CAS"',
    'hmdb' : '"External Sources.HMDB Accession"',
    'wikidata' : '"External Sources.Wikidata"',
    'chemspider' : '"External Sources.Chemspider"',
    'biocyc' : '"External Sources.BioCyc"',
    'chebi' : '"External Sources.ChEBI"'
}

def request(namespace, identifier , polarity, tolerance):
    if namespace == "adduct":
        gte = str(identifier-tolerance)
        lte = (identifier+tolerance)

        sp=  '"Adducts" : {"$elemMatch" : {"Polarity" : "%(polarity)s", ' \
              '"Accurate Mass" : {"$lte" : %(lte)s, "$gte" : %(gte)s}}}' % dict(polarity=polarity.title(),
                                                                           lte=lte, gte=gte)
    else:
        sp = PROPERTY_MAP[namespace] + ': "'+ identifier + '"'
    url = API_BASE % dict(search_param=sp)
    return requests.get(url)

def get_json(identifier, namespace, polarity, tolerance):
    try:
        response = request(identifier, namespace, polarity, tolerance)
        if response.status_code == 200:
            return response.json()["_items"]
    except Exception, e:
        return []

def _metabolites_to_frame(metabolites):
    import pandas as pd
    return pd.DataFrame.from_records([m.to_dict() for m in metabolites], index="_id")

def get_metabolites(identifier, namespace="inchikey", as_dataframe=False, polarity="Neutral", tolerance=0.5):
    results = get_json(identifier, namespace, polarity, tolerance)
    metabolites = [Metabolite(r) for r in results if r != None]
    if as_dataframe:
        return _metabolites_to_frame(metabolites)
    return metabolites

if __name__ == "__main__":
    metabolites = get_metabolites("adduct", 193.03)
