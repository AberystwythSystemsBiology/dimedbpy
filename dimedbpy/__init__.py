'''
dimedbpy

Python interface for the DIMEdb REST service.
https://github.com/KeironO/dimedbpy
'''

from .metabolite import Metabolite
import .methods, click
from prettytable import PrettyTable

def get_metabolites(identifier, namespace="inchikey", as_dataframe=False):
    results = methods._get_json(identifier, namespace)
    metabolites = [Metabolite(r) for r in results if r != None]
    if as_dataframe:
        return methods._metabolites_to_frame(metabolites)
    return metabolites


@click.command()
@click.option("--mass", default=100, help="Mass-to-ion (m/z)", type=float)
@click.option("--polarity", default="Neutral",  help="Polarity/Ionisation (Positive, Negative, Neutral)", type=str)
@click.option("--tolerance", default=0.05, help="+/- m/z tolerance")
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

    response = methods._request(sp=sp, projection=projection)
    if response.status_code == 200:
        metabolites = [Metabolite(r) for r in response.json()["_items"] if r!= None]
        if as_dataframe == True:
            metabolites = methods._metabolites_to_frame(metabolites)
        pretty_table = PrettyTable()
        pretty_table._set_field_names(["InChIKey", "Name", "Molecular Formula"])
        for m in metabolites:
            pretty_table.add_row([m._id, m.name, m.molecular_formula])

        click.echo("Mass-to-ion: %(m)s, Polarity: %(p)s, Tolerance: %(t)s m/z (Found %(l)s)" % dict(m=mass, p=polarity, t=tolerance, l=len(metabolites)))
        click.echo(pretty_table)
        return metabolites
    else:
        return []

if __name__ == "__main__":
    mass_search()
