class Goleador:
    def __init__(self, name, goals, pg):
        self.id2 =  (str(goals)+name.replace(" ","")+str(pg))
        self.name = name
        self.goals = goals
        self.pg = pg

    def toDBCollection(self):
        return{
            'id2':self.id2,
            'name': self.name,
            'goals': self.goals,
            'pg': self.pg
        }
