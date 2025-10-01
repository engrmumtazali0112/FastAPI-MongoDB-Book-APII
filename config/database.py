from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://engrmumtazali01:Gani12%40%23@cluster0.ie4s7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command("ping")
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print("❌ Connection error:", e)

db = client["book_db"]
collection_name = db["book_collection"]