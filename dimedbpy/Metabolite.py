class Metabolite(object):
    def __init__(self, record):
        self.record = record

    @property
    def _id(self):
        return self.record["_id"]

    @property
    def name(self):
        return self.record["Identification Information"]["Name"]

    @property
    def synonyms(self):
        return self.record["Identification Information"]["Synonyms"]

    @property
    def systematic_name(self):
        return self.record["Identification Information"]["Systematic Name"]

    @property
    def smiles(self):
        return self.record["Identification Information"]["SMILES"]
    
    @property
    def molecular_formula(self):
        return self.record["Identification Information"]["Molecular Formula"]

    @property
    def inchi(self):
        return self.record["Identification Information"]["InChI"]

    @property
    def structure_url(self):
        return "http://0.0.0.0:5000/view/structure/%(id)s" % dict(id=self._id)

    def to_dict(self):
        return {"_id" : self._id, "Name" : self.name, "Molecular Formula" : self.molecular_formula}

    def __repr__(self):
        return "Metabolite(%s)" % self._id