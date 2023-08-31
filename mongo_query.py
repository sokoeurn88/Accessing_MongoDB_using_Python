from pymongo import MongoClient

user = 'root'
password = 'NzU4MS1zb2tvZXVy'
host = 'localhost'

# Create connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

# Connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# Select the 'training' dababase
db = connection.training

# Select 'pyhon' collection
collection = db.python

# Create a sample document
doc = {"lab":"Accessing mongodb using python", "Subject":"No SQL databases"}

# Insert a sample document
print("Insert a document into collection")
db.collection.insert_one(doc)

# Query for all documents in 'training' databse and 'python' collection
docs = db.collection.find()
print("Printing documents in collection")

for document in docs:
    print(document)

# Close the connection
print("Closing the connection")
connection.close()

















