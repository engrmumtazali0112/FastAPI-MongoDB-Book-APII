from fastapi import FastAPI
from routes.route import router

app = FastAPI()

# Include the router with a prefix "/books"
app.include_router(router, prefix="/books", tags=["books"])