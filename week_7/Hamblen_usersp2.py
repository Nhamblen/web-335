"""
Author: Noah Hamblen
Date: 7/9/25
File Name: Hamblen_usersp2.py
Description: This program connects to MongoDB database and performs operations.
"""

# Import required libraries
from pymongo import MongoClient
import datetime

# Connect to MongoDB using the connection string
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")

# Access the web335DB database
db = client['web335DB']

# Step 3: Create a new user document
new_user = {
    "firstName": "Noah",
    "lastName": "Hamblen",
    "employeeId": "7",
    "email": "nhamblen@example.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Insert the document into the users collection
user_id = db.users.insert_one(new_user).inserted_id
print("User created with ID:", user_id)

# Step 4: Prove the document was created
print("\n-- Document Created --")
print(db.users.find_one({"employeeId": "7"}))

# Step 5: Update the email address of the created document
db.users.update_one(
    {"employeeId": "7"},
    {
        "$set": {
            "email": "noah.hamblen@example.com"
        }
    }
)

# Step 6: Prove the document was updated
print("\n-- Document Updated --")
print(db.users.find_one({"employeeId": "7"}))

# Step 7: Delete the user document
delete_result = db.users.delete_one({"employeeId": "7"})
print("\n-- Document Deleted --")
print("Documents deleted:", delete_result.deleted_count)

# Step 8: Prove the document was deleted
print("\n-- Verify Deletion --")
print(db.users.find_one({"employeeId": "7"}))