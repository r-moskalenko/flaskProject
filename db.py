from pymongo import MongoClient
import os


def get_connection(database_name):
    host = os.environ.get("MONGO_HOST")
    if not host:
        host = "localhost"
    port = os.environ.get("MONGO_PORT")
    if not port:
        port = "27017"
    port = int(port)
    print("host=", host, "port=", port)
    mongo_client = MongoClient(host=host, port=port)

    return mongo_client.get_database(database_name)


def _getDB(client):
    db = client.FlaskBlog
    return db


def _getCollection(collection_name, db):
    collection = db[collection_name]
    return collection


def closeConnection(client):
    client.close()