"""
dimedbpy

Python interface for the DIMEdb REST service.
https://github.com/KeironO/dimedbpy
"""

from .metabolite import Metabolite
from .methods import _request, _get_json, _metabolites_to_frame
from prettytable import PrettyTable
from urllib.parse import quote


def get_metabolites(namespace, identifier, as_dataframe=False):
    results = _get_json(namespace.lower(), identifier)
    metabolites = [Metabolite(r) for r in results if r != None]
    if as_dataframe:
        return _metabolites_to_frame(metabolites)
    return metabolites


def mass_search(
    mass: float = 69.420,
    polarity: str = "positive",
    tolerance: float = 1.00,
    isotopic_distributions=None,
    as_dataframe=False,
):

    if tolerance > 30.00:
        raise AttributeError("Sorry, but due to abuse the maximum tolerance is now restricted to +/- 30 m/z.")

    gte = mass - tolerance
    lte = mass + tolerance

    polarity = polarity.title()

    if isotopic_distributions == None:
        common_adducts = {
            "Neutral": ["[M]"],
            "Negative": ["[M-H]1-", "[M+Cl]1-", "[M+Br]1-"],
            "Positive": ["[M+H]1+", "[M+K]1+", "[M+Na]1+"],
        }

        isotopic_distributions = common_adducts[polarity]

    sp = (
        '"Adducts" : {"$elemMatch" : {"Polarity" : "%(polarity)s", "Adduct" : {"$in" : %(isotopic_distributions)s},'
        '"Accurate Mass" : {"$lte" : %(lte)s, "$gte" : %(gte)s}}}'
        % dict(
            polarity=polarity.title(),
            lte=lte,
            gte=gte,
            isotopic_distributions=str(isotopic_distributions).replace("'", '"'),
        )
    )

    projection = (
        '&projection={"Identification Information" : 1, "Physicochemical Properties" : 1, "External Sources" : 1, "Pathways" : 1, "Adducts.%(polarity)s.$":1}'
        % dict(polarity=polarity)
    )
    response = _request(sp=sp, projection=projection)
    if response.status_code == 200:
        metabolites = [Metabolite(r) for r in response.json()["_items"] if r != None]
        if as_dataframe == True:
            metabolites = _metabolites_to_frame(metabolites)
        pretty_table = PrettyTable()
        pretty_table._set_field_names(["InChIKey", "Name", "Molecular Formula"])
        for m in metabolites:
            pretty_table.add_row([m._id, m.name, m.molecular_formula])
        return metabolites
    else:
        return {"Error": response.status_code}
