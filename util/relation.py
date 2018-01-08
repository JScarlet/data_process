class Relation:
    def __init__(self, subject, relation, object):
        self.subject = subject
        self.relation = relation
        self.object = object

    def __eq__(self, other):
        if isinstance(other, Relation):
            return self.subject == other.subject and self.relation == other.relation and self.object == other.object
        else:
            return False

    def to_json(self):
        return {"subject": self.subject, "relation": self.relation, "object": self.object}

    def __hash__(self):
        return hash(self.subject + self.relation + self.object)

    def __str__(self):
        return self.subject + ',' + self.relation + ',' + self.object