from pymongo import MongoClient
from pymongo.server_api import ServerApi
import json

# MongoDB connection
uri = "mongodb+srv://engrmumtazali01:Gani12%40%23@cluster0.ie4s7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

# Connect to database
db = client["book_db"]
collection = db["book_collection"]

# Fetch all books
books = list(collection.find())

# Display books
print("\n" + "="*80)
print("📚 BOOKS IN DATABASE")
print("="*80 + "\n")

if not books:
    print("No books found in the database.")
else:
    for i, book in enumerate(books, 1):
        print(f"Book #{i}")
        print(f"ID: {book['_id']}")
        print(f"Title: {book.get('title', 'N/A')}")
        print(f"Author: {book.get('author', 'N/A')}")
        print(f"Year: {book.get('published_year', 'N/A')}")
        print(f"Description: {book.get('description', 'N/A')}")
        print("-" * 80)

print(f"\nTotal Books: {len(books)}\n")

# Close connection
client.close()