"""
Author: Noah Hamblen
Date: 6/30/25
File Name: Hamblen_usersp1.py
Description: This program connects to MongoDB database and performs operations.
"""

# Import MongoClient
from pymongo import MongoClient

# Connect to MongoDB using the connection string
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")

# Access the web335DB database
db = client['web335DB']

# Display all documents in the users collection
print("\n-- Displaying All Users --")
for user in db.users.find({}, {"_id": 0, "firstName": 1, "lastName": 1}):
    print(user)

# Display a document where the employeeId is 1011
print("\n-- Displaying User With Employee ID 1011 --")
user_1011 = db.users.find_one({"employeeId": "1011"})
print(user_1011)

# Display a document where the lastName is Mozart
print("\n-- Displaying User With Last Name Mozart --")
user_mozart = db.users.find_one({"lastName": "Mozart"})
print(user_mozart)