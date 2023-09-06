from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://Acevedo:147258369@bocajuniors.qcsorb3.mongodb.net/?retryWrites=true&w=majority'
#mongodb+srv://Acevedo:147258369@bocajuniors.qcsorb3.mongodb.net/?retryWrites=true&w=majority
#mongodb+srv://Acevedo:147258369@bocajuniors.qcsorb3.mongodb.net/
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["CABJ"]

    except ConnectionError:
        print('Error de conexión con la db')
        
    return db
