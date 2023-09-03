"""
Created on Fri May 26 19:24:14 2023

author: Conner Hufnagel
"""

from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId

class AnimalShelter(object):
    
    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        # USER = 'aacuser'
        # PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31465
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    def create(self, data):
        # as long as there is data to be created...
        if data is not None:
            # ... insert the new, created document
            result = self.database.animals.insert_one(data) 
            return result.acknowledged # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    def read(self, query):
        # set cursor to result of find key : value pair
        cursor = self.collection.find(query)
        # list results
        return list(cursor)
    
    def update(self, query, update_data):
        # set query and update_data as key : value pairs
        result = self.collection.update_many(query, {"$set": update_data})
        # finds documents that match query, updates to match update_data
        return result.modified_count
    
    def delete(self, query):
        # finds documents that match query key : value pair
        result = self.collection.delete_many(query)
        # deletes those documents
        return result.deleted_count
