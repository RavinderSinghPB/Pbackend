from pymongo import MongoClient

def get_db(conn_str = 'mongodb://localhost:27017/' , db_name = 'dev'):
    client = MongoClient(conn_str)
    return client[db_name], client