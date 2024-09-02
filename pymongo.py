
""" 
pip install pymongo

Database
•	Database is a container for collections.
•	Each database gets its own set of files.
•	A single MongoDB server can has multiple databases.
Collection
•	Collection is a group of documents.
•	Collection is equivalent to RDBMS table.
•	A collection consist inside a single database.
•	Collections do not enforce a schema.
•	A Collection can have different fields within a Documents.


""" 
import pymongo
from pymongo import MongoClient

# Connection to clustser that is holding the database
cluster = MongoClient("")   # Add connection string "mongodb+srv://tim:<password>@cluster....." Add password there
# Pick the database
db = cluster["test"]
# Pick the collection
collection = db["test"]
"""
collection is like mini db 

Bunch of dictionary keys
{"_id": 0, "name": "Tim", "score":5}

"_id": 0 is mandatory, else automatically gets generated

""" 
post = {"_id":0, "name": "Tim", "score":5}
collection.insert_one(post) 
""" 
post is actually document. Here it is posted to database (from the link)
"""  
# Send multiple post
post1 = {"_id":5, "name": "Timen", "score":5}
post2 = {"_id":6, "name": "Jim", "score":5}
collection.insert_many([post1, post2])   

# Querrying MongoDB
# remove insert after insert and then run find

results = collection.find({"name":"bill"})
print(results)                   # here we get only cursor object

for result in results:
    print(result)                # we get the dictionary

for result in results:
    print(result["name"])        # to access specific field, it returns all names

# So to get one result first access only id


results = collection.find({"_id":5})
for result in results:
    print(result["_id"])


results = collection.find({"_id":5, "name": "bill"}) # can add multiple fields, regex

# to get only one result 
results = collection.find_one({"_id":0})
# to get everything
results = collections.find({})
for x in results:
    print(x)

# Deleting the data
results = colelction.delete_one({"_id":0})
results = collection.delete_many({})      # specify here, or deletes everything


# Update and Replace

results = collection.update_one({}, {})     # search documentation for update operators

results = collection.update_one({"_id":5}, {"$set":{"name":"alex"}})
# Adding new field 
results = collection.update_one({"_id":5}, {"$set":{"hello":5}})  # check syntax for update_many

results = collection.update_one({"_id":5}, {"$set":{"hello":5}})

# Counting documents
post_count = collection.count_documents({})
print(post_count)
# https://www.youtube.com/watch?v=rE_bJl2GAY8 

db.inventory.insertMany([
    {_id:1, item:{name: "ab", code: "123"}, qty:15, tags:["A", "B", "C"]},
    {_id:2, item:{name: "cd", code: "123"}, qty:20, tags:["B"]},
    { _id: 3, item: { name: "ij", code: "456" }, qty: 25, tags: [ "A", "B" ] },
    { _id: 4, item: { name: "xy", code: "456" }, qty: 30, tags: [ "B", "A" ] },
    { _id: 5, item: { name: "mn", code: "000" }, qty: 20, tags: [ [ "A", "B" ], "C" ] }
] )

db.inventory.find({tags: ["A","B"]})


# Output:

# { "acknowledged" : true, "insertedIds" : [ 1, 2, 3, 4, 5 ] }
# { "_id" : 3, "item" : { "name" : "ij", "code" : "456" }, "qty" : 25, "tags" : [ "A", "B" ] }
# { "_id" : 5, "item" : { "name" : "mn", "code" : "000" }, "qty" : 20, "tags" : [ [ "A", "B" ], "C" ] }  

# Query and Prjections

db.inventory.find( { $or: [ { quantity: { $lt: 20 } }, { price: 10 } ] } ) 


# Getting dates

var start = new Date("2016-07-30")/1000,
    end = new Date("2016-08-01")/1000;
db.dataProfTable.find({
    "timestamp": { "$gte": start, "$lte": end }
}) 
