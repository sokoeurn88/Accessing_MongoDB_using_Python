from pymongo import MongoClient

user = 'root'
password = 'NzU4MS1zb2tvZXVy' # password u just got when running start_mongo
host = 'localhost'
# Create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)

# Connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# Get database list
print("Getting list of databases")
dbs = connection.list_database_names()

# Print database names
for db in dbs:
    print(db)
print("Closing the connection to mongodb server")

# Close server connection
connection.close()