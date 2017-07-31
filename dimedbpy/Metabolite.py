class Metabolite(object):
    def __init__(self, record):
        self.record = record

    @property
    def _id(self):
        return self.record["_id"]

    @property
    def name(self):
        return self.record["Identification Information"]["Name"]

    def to_dict(self):
        return {"_id" : self._id, "Name" : self.name}

    def __repr__(self):
        return "Metabolite(%s)" % self._id