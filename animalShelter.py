from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):

	""" CRUD operations for Animal collection in MongoDB """


	def __init__(self):

		# Initializing the MongoClient. This helps to access the MongoDB databases and collections.

		self.client = MongoClient('mongodb://aacuser:aacuser@localhost:37160/aac')

		self.database = self.client['aac']


# Create Method

	def create(self, createData):

		if createData is not None:

			self.database.animals.insert(createData)  # data should be dictionary

		else:

			raise Exception("Nothing to save, because data parameter is empty")

# Read Method

	def read(self, readData):

		if readData is not None:

			return (self.database.animals.find(readData, {"_id":False})) # data should be dictionary

		else:

			raise Exception("Nothing to output, because data parameter is empty")

# Update Method

	def update(self, animalID, updateData):

		if updateData is not None:

			self.database.animals.update(animalID, {"$set": updateData}) # data should be dictionary

		else:

			raise Exception("Nothing to output, because data parameter is empty")

# Delete Method

	def delete(self, deleteData):

		if deleteData is not None:

			self.database.animals.delete_one(deleteData) # data should be dictionary

		else:

			raise Exception("Nothing to output, because data parameter is empty")
