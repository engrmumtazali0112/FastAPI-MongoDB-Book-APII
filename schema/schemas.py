# schema.py
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    description: str
    published_year: int
    author: str

class BookResponse(BaseModel):
    id: str
    title: str
    description: str
    published_year: int
    author: str 