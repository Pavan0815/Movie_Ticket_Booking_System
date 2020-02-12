from pymongo import MongoClient


class Connection:
    @staticmethod
    def connect(collection_name):
        connection = MongoClient(host="localhost", port=27017)

        return connection["Movie_Ticket"][collection_name]
