#connect to the mongodb server.
from pymongo import MongoClient

user = 'root'
password = 'NzU4MS1zb2tvZXVy'
host = 'localhost'

# Create connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

# connect to mongodb server
connection = MongoClient(connecturl)

# select a database named training.
db = connection.training

# select a collection named mongodb_glossary.
collection = db.mongodb_glossary

# insert the following documents into the collection mongodb_glossary.

# Create samples document
doc1 = {"database":"a database contains collections"}
doc2 = {"collection":"a collection stores the documents"}
doc3 = {"document":"a document contains the data in the form of key value pairs."}

# Insert a samples document
print("Insert document into collection")
db.collection.insert_one(doc1)
db.collection.insert_one(doc2)
db.collection.insert_one(doc3)

#query and print all the documents in the training database and mongodb_glossary collection.
docs = db.collection.find()
print("Print document in collection")

for document in docs:
    print(document)

# Close connectin
print("Close connection")
connection.close()

























