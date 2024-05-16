from pymongo import MongoClient
import certifi
import os

MONGO_URI = os.environ.get('DB_URL')

ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["CABJ"]

    except ConnectionError:
        print('Error de conexión con la db')
        
    return db
