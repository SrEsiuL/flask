class Goleador:
    def __init__(self, name, goals, pg):
        self.name = name
        self.goals = goals
        self.pg = pg

    def toDBCollection(self):
        return{
            '_id':self._id,
            'name': self.name,
            'goals': self.goals,
            'pg': self.pg
        }