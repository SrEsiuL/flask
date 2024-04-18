from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://leacevedo09:B0caJun10rs@cabj.wxpr3ru.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["CABJ"]

    except ConnectionError:
        print('Error de conexión con la db')
        
    return db
