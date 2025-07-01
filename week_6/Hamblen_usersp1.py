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
print("\n-- Display All Users --")
for user in db.users.find({}, {"_id": 0, "firstName": 1, "lastName": 1}):
    print(user)

