
""" 
pip install pymongo


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


