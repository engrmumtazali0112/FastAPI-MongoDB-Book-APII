from fastapi import APIRouter, HTTPException, status
from models.books import Book
from config.database import collection_name
from bson import ObjectId

router = APIRouter()

# Helper function to convert MongoDB document to dictionary
def book_serial(book) -> dict:
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "description": book["description"],
        "published_year": book["published_year"],
        "author": book["author"]
    }

# Get all books
@router.get("/", response_model=list)
async def get_books():
    books = list(collection_name.find())
    return [book_serial(book) for book in books]

# Get a single book by ID
@router.get("/{book_id}", response_model=dict)
async def get_book(book_id: str):
    if not ObjectId.is_valid(book_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")
    
    book = collection_name.find_one({"_id": ObjectId(book_id)})
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_serial(book)

# Create a new book
@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def post_book(book: Book):
    book_dict = book.dict()
    result = collection_name.insert_one(book_dict)
    new_book = collection_name.find_one({"_id": result.inserted_id})
    return book_serial(new_book)

# Update a book by ID
@router.put("/{book_id}", response_model=dict)
async def update_book(book_id: str, book: Book):
    if not ObjectId.is_valid(book_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")
    
    updated_book = collection_name.find_one_and_update(
        {"_id": ObjectId(book_id)},
        {"$set": book.dict()},
        return_document=True
    )
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_serial(updated_book)

# Delete a book by ID
@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: str):
    if not ObjectId.is_valid(book_id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId format")
    
    deleted_book = collection_name.find_one_and_delete({"_id": ObjectId(book_id)})
    if not deleted_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return None