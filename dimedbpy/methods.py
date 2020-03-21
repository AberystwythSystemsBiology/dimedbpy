import requests, pandas as pd


PROPERTY_MAP = {
    "inchikey": '"_id"',
    "name": '"Identification Information.Name"',
    "molecular_formula": '"Identification Information.Molecular Formula"',
    "smiles": '"Identification Information.SMILES"',
    "inchi": '"Identification Information.InChI"',
    "kegg": '"External Sources.KEGG Compound"',
    "pubchem": '"External Sources.PubChem"',
    "cas": '"External Sources.CAS"',
    "hmdb": '"External Sources.HMDB Accession"',
    "wikidata": '"External Sources.Wikidata"',
    "chemspider": '"External Sources.Chemspider"',
    "biocyc": '"External Sources.BioCyc"',
    "chebi": '"External Sources.ChEBI"',
}

API_BASE = "http://dimedb.ibers.aber.ac.uk/api/metabolites/?where={%(search_param)s}"


def _request(namespace=None, identifier=None, sp=None, projection=None):
    if sp == None:
        sp = PROPERTY_MAP[namespace] + ': "' + identifier + '"'
    url = API_BASE % dict(search_param=sp)
    if projection != None:
        url += projection
    return requests.get(url)


def _get_json(
    identifier, namespace,
):
    try:
        response = _request(identifier, namespace)
        if response.status_code == 200:
            return response.json()["_items"]
    except Exception:
        return []


def _metabolites_to_frame(metabolites, properties=["_id", "Name", "Molecular Formula"]):
    return pd.DataFrame.from_records(
        [m.to_dict(properties=properties) for m in metabolites], index="_id"
    )
