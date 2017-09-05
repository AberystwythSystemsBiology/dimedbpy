'''
dimedbpy

Python interface for the DIMEdb REST service.
https://github.com/KeironO/dimedbpy
'''

__author__ = "Keiron O'Shea"
__email__ = "keo7@aber.ac.uk"
__version__ = "0.0.1a"
__license__ = "MIT"

API_BASE = "http://dimedb.ibers.aber.ac.uk/api/metabolites/?where={%(search_param)s}"

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

def request(namespace=None, identifier=None, sp=None, projection=None):
    if sp == None:
        sp = PROPERTY_MAP[namespace] + ': "'+ identifier + '"'
    url = API_BASE % dict(search_param=sp)
    if projection != None:
        url += projection
    return requests.get(url)

def get_json(identifier, namespace,):
    try:
        response = request(identifier, namespace)
        if response.status_code == 200:
            return response.json()["_items"]
    except Exception, e:
        return []

def _metabolites_to_frame(metabolites):
    import pandas as pd
    return pd.DataFrame.from_records([m.to_dict() for m in metabolites], index="_id")

def get_metabolites(identifier, namespace="inchikey", as_dataframe=False):
    results = get_json(identifier, namespace)
    metabolites = [Metabolite(r) for r in results if r != None]
    if as_dataframe:
        return _metabolites_to_frame(metabolites)
    return metabolites


def mass_search(mass, polarity, tolerance, adducts=None, as_dataframe=False):
    gte = mass - tolerance
    lte = mass + tolerance

    polarity = polarity.title()

    if adducts == None:
        common_adducts = {
            "Neutral" : ["[M]"],
            "Negative" : ["[M-H]1-", "[M+Cl]1-", "[M+Br]1+"],
            "Positive" : ["[M+H]1+", "[M+K]1+", "[M+Na]1+"]
        }

        adducts = common_adducts[polarity]

    sp = '"Adducts" : {"$elemMatch" : {"Polarity" : "%(polarity)s", "Adduct" : {"$in" : %(adducts)s},' \
         '"Accurate Mass" : {"$lte" : %(lte)s, "$gte" : %(gte)s}}}' % dict(polarity=polarity.title(),lte=lte, gte=gte, adducts=str(adducts).replace("'", '"'))


    projection = '&projection={"Identification Information" : 1, "Physicochemical Properties" : 1, "External Sources" : 1, "Pathways" : 1, "Adducts.%(polarity)s.$":1}' % dict(polarity=polarity)

    response = request(sp=sp, projection=projection)
    if response.status_code == 200:
        metabolites = [Metabolite(r) for r in response.json()["_items"] if r!= None]
        return metabolites
    else:
        return []


if __name__ == "__main__":
    metabolites = mass_search(100, "Negative", 0.05, adducts=["[M-H]1-"])
    for metabolite in metabolites:
        print metabolite.adducts
