class Metabolite(object):
    def __init__(self, record):
        self._record = record
        self._identification_info = self._record["Identification Information"]
        self._physicochemical_properties = self._record["Physicochemical Properties"]
        self._external_sources = self._record["External Sources"]
        self._pathways = self._record["Pathways"]
        self.adducts = self._record["Adducts"]

    @property
    def _id(self):
        return self._record["_id"]

    # Identification Information

    @property
    def name(self):
        return self._identification_info["Name"]

    @property
    def synonyms(self):
        return self._identification_info["Synonyms"]

    @property
    def systematic_name(self):
        return self._identification_info["Systematic Name"]

    @property
    def smiles(self):
        return self._identification_info["SMILES"]
    
    @property
    def molecular_formula(self):
        return self._identification_info["Molecular Formula"]

    @property
    def inchi(self):
        return self._identification_info["InChI"]


    # Physicochemical Properties

    @property
    def clogP(self):
        return self._physicochemical_properties["clogP"]

    @property
    def polar_surface_area(self):
        return self._physicochemical_properties["Polar Surface Area"]

    @property
    def secondary_amines(self):
        return self._physicochemical_properties["Secondary Amines"]

    @property
    def ether_oxygens(self):
        return self._physicochemical_properties["Ether Oxygens"]

    @property
    def rings(self):
        return self._physicochemical_properties["Rings"]

    @property
    def hydrogen_bond_acceptors(self):
        return self._physicochemical_properties["Hydrogen Bond Acceptors"]

    @property
    def hydrogen_bond_donors(self):
        return self._physicochemical_properties["Hydrogen Bond Donors"]

    @property
    def aromatic_rings(self):
        return self._physicochemical_properties["Aromatic Rings"]

    @property
    def formal_charge(self):
        return self._physicochemical_properties["Formal Charge"]

    @property
    def mr_values(self):
        return self._physicochemical_properties["MR Values"]

    @property
    def fraction_sp3_carbon(self):
        return self._physicochemical_properties["Fraction of SP3 Carbon"]

    @property
    def carboxylic_acids(self):
        return self._physicochemical_properties["Carboxylic Acids"]

    @property
    def molecular_weight(self):
        return self._physicochemical_properties["Molecular Weight"]

    @property
    def rotatable_bonds(self):
        return self._physicochemical_properties["Rotatable Bonds"]

    # External Sources

    @property
    def chebi(self):
        return self._external_sources["ChEBI"]

    @property
    def hmdb(self):
        return self._external_sources["HMDB Accession"]

    @property
    def pubchem(self):
        return self._external_sources["PubChem"]

    @property
    def kegg(self):
        return self._external_sources["KEGG Compound"]

    @property
    def cas(self):
        return self._external_sources["CAS"]

    @property
    def wikidata(self):
        return self._external_sources["Wikidata"]

    @property
    def biocyc(self):
        return self._external_sources["BioCyc"]

    @property
    def chemspider(self):
        return self._external_sources["Chemspider"]

    # Pathway Info

    @property
    def kegg_pathways(self):
        return self._pathways["KEGG"]

    @property
    def smpdb_pathways(self):
        return self._pathways["SMPDB"]

    @property
    def biocyc_pathways(self):
        return self._pathways["BioCyc"]

    @property
    def structure_url(self):
        return "http://dimedb.ibers.aber.ac.uk/view/structure/%(id)s" % dict(id=self._id)

    def to_dict(self):
        return self._record

    def __repr__(self):
        return "Metabolite(%s)" % self._id