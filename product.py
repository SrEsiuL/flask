class Product:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        

def toDBCollection(self):
    return{
        'name': self.name,
        'price': self.age,
        'quantity': self.email
    }