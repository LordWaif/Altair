from pymongo import MongoClient

def connectMongo(db_name):
    client = MongoClient('mongodb+srv://altair-admin-victor:ebgLlVUfbYr0EXfn@altair-nv.b4uqhas.mongodb.net/?retryWrites=true&w=majority')
    db = client[db_name]
    return db

def addRegra(database,regra):
    collections = database['regra']