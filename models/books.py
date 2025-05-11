from pydantic import BaseModel

class Book(BaseModel):
    title: str
    description: str
    published_year: int
    author: str
