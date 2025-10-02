# 📚 FastAPI MongoDB Book Management System

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/main/icons/folder-api.svg" width="100" />
</p>

A modern, full-stack book management system with a beautiful responsive UI, built with FastAPI backend and vanilla JavaScript frontend, powered by MongoDB.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

[Features](#features) • [Screenshots](#screenshots) • [Installation](#installation) • [Usage](#usage) • [API Reference](#api-reference) • [Contributing](#contributing)

</div>

---

## ✨ Features

### Backend Features
- **🔍 Get all books**: Retrieve a complete list of all books in the collection
- **📖 Get book by ID**: Fetch detailed information about a specific book
- **➕ Create new book**: Add books with title, author, published year, and description
- **✏️ Update book**: Modify existing book details with PUT request
- **🗑️ Delete book**: Remove books from the collection
- **🔒 Input validation**: Pydantic schemas ensure data integrity
- **📊 Interactive API docs**: Built-in Swagger UI and ReDoc documentation
- **⚡ High performance**: Async/await support for optimal speed

### Frontend Features
- **🎨 Modern gradient UI**: Beautiful purple gradient design with smooth animations
- **📱 Fully responsive**: Works seamlessly on desktop, tablet, and mobile devices
- **🔎 Real-time search**: Instant search across title, author, description, and year
- **✅ Form validation**: Client-side validation for all required fields
- **🎯 Smooth interactions**: Hover effects, animations, and transitions
- **📋 CRUD operations**: Complete create, read, update, and delete functionality
- **🔔 Toast notifications**: Success and error messages for all operations
- **📊 Data table**: Clean, organized display with action buttons
- **🎭 Empty states**: Friendly messages when no books are found
- **♿ Accessible**: Semantic HTML and proper form labels

---

## 🖼️ Screenshots

### Book Management Form
*Beautiful form interface for adding and editing books with gradient styling*
<img width="1346" height="608" alt="image" src="https://github.com/user-attachments/assets/8bcab04a-8305-4d04-befe-1f95ba45d817" />

### Book Collection Table

*Responsive data table with search functionality and action buttons*
<img width="1236" height="642" alt="image" src="https://github.com/user-attachments/assets/ff0f1257-6b09-4865-a69d-21ba7dae46ce" />

---

## 📋 Prerequisites

- **Python 3.8+**
- **MongoDB** (local installation or MongoDB Atlas)
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

---

## 🔧 Installation

### Backend Setup

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
   
Create a `.env` file in the project root:

```env
MONGODB_URL=mongodb://localhost:27017
DB_NAME=book_database
```

5. **Run the FastAPI application**

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### Frontend Setup

1. **Open the HTML file**

Simply open `index.html` in your web browser, or use a local server:

```bash
# Using Python's built-in server
python -m http.server 8080

# Then visit http://localhost:8080
```

2. **Verify API connection**

The frontend is configured to connect to `http://127.0.0.1:8000/books`. Make sure your FastAPI backend is running.

---

## 🖥️ Usage

### Accessing the Application

Once both backend and frontend are running:

- **Frontend UI**: Open `index.html` in your browser
- **API Endpoints**: `http://127.0.0.1:8000`
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

### Using the Interface

1. **Adding a Book**
   - Fill in all required fields (Title, Author, Year, Description)
   - Click "💾 Save Book"
   - See success notification

2. **Searching Books**
   - Type in the search box
   - Results filter in real-time across all fields

3. **Editing a Book**
   - Click the "✏️ Edit" button on any book row
   - Form populates with existing data
   - Modify fields and click "💾 Update Book"

4. **Deleting a Book**
   - Click the "🗑️ Delete" button
   - Confirm deletion in the prompt
   - Book is removed from the collection

---

## 📘 API Reference

### Book Schema

```json
{
  "id": "string (MongoDB ObjectID)",
  "title": "string (required)",
  "author": "string (required)",
  "published_year": "integer (required, 1000-2099)",
  "description": "string (required)"
}
```

### API Endpoints

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| GET | `/books/` | Get all books | None |
| GET | `/books/{id}` | Get a specific book | None |
| POST | `/books/` | Create a new book | Book object |
| PUT | `/books/{id}` | Update a book | Book object |
| DELETE | `/books/{id}` | Delete a book | None |

### Example API Requests

**Create a Book**
```bash
curl -X POST "http://127.0.0.1:8000/books/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Rich Dad Poor Dad",
    "author": "Robert Kiyosaki",
    "published_year": 1997,
    "description": "A financial education classic"
  }'
```

**Get All Books**
```bash
curl -X GET "http://127.0.0.1:8000/books/"
```

**Update a Book**
```bash
curl -X PUT "http://127.0.0.1:8000/books/{book_id}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Title",
    "author": "Updated Author",
    "published_year": 2024,
    "description": "Updated description"
  }'
```

**Delete a Book**
```bash
curl -X DELETE "http://127.0.0.1:8000/books/{book_id}"
```

---

## 🎨 Design Features

### Color Scheme
- **Primary Gradient**: Purple (#667eea) to Deep Purple (#764ba2)
- **Secondary**: Gray tones for buttons and borders
- **Accent**: Yellow (#ffc107) for edit buttons, Red (#dc3545) for delete

### Animations
- Fade-in effects on page load
- Smooth hover transitions on buttons and table rows
- Slide-in toast notifications
- Scroll-to-top on edit action

### Responsive Breakpoints
- **Desktop**: Full grid layout with 3-column form
- **Tablet**: Adjusted spacing and 2-column grid
- **Mobile**: Single column layout, stacked buttons

---

## 📁 Project Structure

```
FastAPI-MongoDB-Book-API/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration and environment variables
│   ├── database.py          # MongoDB connection setup
│   ├── routes/
│   │   ├── __init__.py
│   │   └── book.py          # Book CRUD endpoints
│   ├── models/
│   │   ├── __init__.py
│   │   └── book.py          # Book data models
│   └── schemas/
│       ├── __init__.py
│       └── book.py          # Pydantic validation schemas
├── index.html               # Frontend application
├── .env                     # Environment variables
├── .gitignore
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🔒 CORS Configuration

The API is configured to accept requests from the frontend. Default CORS settings allow:
- Origin: `http://127.0.0.1:8080` (or your frontend URL)
- Methods: GET, POST, PUT, DELETE
- Headers: Content-Type

---

## 🧪 Testing

### Manual Testing
1. Start the backend server
2. Open the frontend in a browser
3. Test all CRUD operations
4. Verify search functionality
5. Check responsive design on different devices

### API Testing
Use the built-in Swagger UI at `http://127.0.0.1:8000/docs` to test all endpoints interactively.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Contribution Guidelines
- Follow PEP 8 style guide for Python code
- Use meaningful commit messages
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation as needed

---

## 🐛 Known Issues

- None at the moment! Please report any bugs you find.

---

## 🚀 Future Enhancements

- [ ] Add book cover image upload
- [ ] Implement pagination for large datasets
- [ ] Add sorting options (by title, author, year)
- [ ] Include book rating system
- [ ] Add user authentication
- [ ] Export data to CSV/PDF
- [ ] Advanced filtering options
- [ ] Dark mode toggle
- [ ] Multi-language support

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Engr Mumtaz Ali**

- GitHub: [@engrmumtazali0112](https://github.com/engrmumtazali0112)
- Email: engrmumtazali0112@gmail.com

---

## 🙏 Acknowledgments

- FastAPI documentation and community
- MongoDB documentation
- Inspiration from modern web design trends
- All contributors and users of this project

---

## 📞 Support

If you have any questions or need help, please:
- Open an issue on GitHub
- Contact via email: engrmumtazali0112@gmail.com
- Check existing documentation and issues

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [Engr Mumtaz Ali](https://github.com/engrmumtazali0112)

</div>
