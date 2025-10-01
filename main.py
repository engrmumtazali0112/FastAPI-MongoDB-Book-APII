from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes.route import router
import os

app = FastAPI(title="FastAPI MongoDB Book API")

# Path to frontend folder
frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")

# Mount only static assets (CSS, JS)
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

# Serve index.html at "/"
@app.get("/")
async def serve_frontend():
    return FileResponse(os.path.join(frontend_dir, "index.html"))

# Books API
app.include_router(router, prefix="/books", tags=["Books"])
