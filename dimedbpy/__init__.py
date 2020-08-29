"""
dimedbpy

Python interface for the DIMEdb REST service.
https://github.com/KeironO/dimedbpy
"""

from .metabolite import Metabolite
from .methods import _request, _get_json, _metabolites_to_frame
from prettytable import PrettyTable


def get_metabolites(identifier, namespace="inchikey", as_dataframe=False):
    results = _get_json(identifier, namespace)
    metabolites = [Metabolite(r) for r in results if r != None]
    if as_dataframe:
        return _metabolites_to_frame(metabolites)
    return metabolites


def mass_search(
    mass: float=69.420, polarity: str="positive", tolerance: float = 0.2, isotopic_distributions=None, as_dataframe=False
):

    gte = mass - tolerance
    lte = mass + tolerance

    polarity = polarity.title()

    if isotopic_distributions == None:
        common_adducts = {
            "Neutral": ["[M]"],
            "Negative": ["[M-H]1-", "[M+Cl]1-", "[M+Br]1+"],
            "Positive": ["[M+H]1+", "[M+K]1+", "[M+Na]1+"],
        }

        isotopic_distributions = common_adducts[polarity]

    sp = (
        '"Isotopic Distributions" : {"$elemMatch" : {"Polarity" : "%(polarity)s", "Adduct" : {"$in" : %(adducts)s},'
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

        click.echo(
            "Mass-to-ion: %(m)s, Polarity: %(p)s, Tolerance: %(t)s m/z (Found %(l)s)"
            % dict(m=mass, p=polarity, t=tolerance, l=len(metabolites))
        )
        click.echo(pretty_table)
        return metabolites
    else:
        return []


