# 📚 FastAPI MongoDB Book API

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/main/icons/folder-api.svg" width="100" />
</p>

A modern RESTful API for managing a collection of books, built with FastAPI and MongoDB.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[Features](#features) • [Demo](#live-demo) • [Installation](#installation) • [Usage](#usage) • [API Reference](#api-reference) • [Contributing](#contributing)

</div>

## ✨ Features

- **🔍 Get all books**: Retrieve a paginated list of all books with sorting and filtering options
- **📖 Get a book by ID**: Retrieve a single book by its unique MongoDB ObjectID
- **➕ Create a new book**: Add a new book with validation for required fields
- **✏️ Update a book by ID**: Modify the details of an existing book
- **🗑️ Delete a book by ID**: Remove a book from the database
- **🔎 Search functionality**: Find books by title, author, or genre
- **🔒 Input validation**: Ensure data integrity with Pydantic schemas
- **📊 Swagger UI documentation**: Interactive API documentation
- **🐳 Docker support**: Easy deployment with Docker

## 🚀 Live Demo

API Endpoint: [https://fastapi-mongodb-book-api.herokuapp.com](https://fastapi-mongodb-book-api.herokuapp.com)  
API Documentation: [https://fastapi-mongodb-book-api.herokuapp.com/docs](https://fastapi-mongodb-book-api.herokuapp.com/docs)

## 📋 Prerequisites

- Python 3.8+
- MongoDB
- Docker (optional)

## 🔧 Installation

### Option 1: Local Setup

1. **Clone the repository**

```bash
git clone https://github.com/engrmumtazali0112/FastAPI-MongoDB-Book-API.git
cd FastAPI-MongoDB-Book-API
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
   
Create a `.env` file in the project root with the following variables:

```
MONGODB_URL=mongodb://localhost:27017
DB_NAME=book_database
```

5. **Run the application**

```bash
uvicorn app.main:app --reload
```

### Option 2: Docker Setup

1. **Clone the repository**

```bash
git clone https://github.com/engrmumtazali0112/FastAPI-MongoDB-Book-APII.git
cd FastAPI-MongoDB-Book-API
```

2. **Build and start the Docker containers**

```bash
docker-compose up -d
```

## 🖥️ Usage

Once the application is running, you can access:

- API at [http://localhost:8000](http://localhost:8000)
- Interactive API documentation at [http://localhost:8000/docs](http://localhost:8000/docs)
- Alternative API documentation at [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 📘 API Reference

### Book Schema

```json
{
  "id": "string (ObjectID)",
  "title": "string",
  "author": "string",
  "genre": "string",
  "publication_year": "integer",
  "isbn": "string",
  "description": "string",
  "price": "float",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

### Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/books` | Get all books |
| GET | `/books/{id}` | Get a book by ID |
| POST | `/books` | Create a new book |
| PUT | `/books/{id}` | Update a book by ID |
| DELETE | `/books/{id}` | Delete a book by ID |
| GET | `/books/search` | Search for books |

## 🧪 Testing

Run the test suite with:

```bash
pytest
```

For test coverage report:

```bash
pytest --cov=app
```

## 📁 Project Structure

```
FastAPI-MongoDB-Book-API/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── book.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── book.py
│   └── schemas/
│       ├── __init__.py
│       └── book.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_book.py
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Engr Mumtaz Ali - [@engrmumtazali0112](https://github.com/engrmumtazali0112) - engrmumtazali0112@gmail.com

Project Link: [https://github.com/engrmumtazali0112/FastAPI-MongoDB-Book-API](https://github.com/engrmumtazali0112/FastAPI-MongoDB-Book-APII)

---

<div align="center">
  <sub>Built with ❤️ by Engr Mumtaz Ali</sub>
</div>