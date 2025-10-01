const API_URL = "http://127.0.0.1:8000/books";

const bookForm = document.getElementById("bookForm");
const booksTableBody = document.querySelector("#booksTable tbody");

// Fetch and display books
async function fetchBooks() {
  const res = await fetch(API_URL + "/");
  const books = await res.json();
  booksTableBody.innerHTML = "";
  books.forEach(book => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${book.title}</td>
      <td>${book.description}</td>
      <td>${book.published_year}</td>
      <td>${book.author}</td>
      <td>
        <button class="action edit" onclick="editBook('${book.id}')">Edit</button>
        <button class="action delete" onclick="deleteBook('${book.id}')">Delete</button>
      </td>
    `;
    booksTableBody.appendChild(row);
  });
}

// Add or Update Book
bookForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const bookId = document.getElementById("bookId").value;
  const book = {
    title: document.getElementById("title").value,
    description: document.getElementById("description").value,
    published_year: parseInt(document.getElementById("published_year").value),
    author: document.getElementById("author").value
  };

  if (bookId) {
    // Update
    await fetch(`${API_URL}/${bookId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(book)
    });
  } else {
    // Create
    await fetch(API_URL + "/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(book)
    });
  }

  bookForm.reset();
  document.getElementById("bookId").value = "";
  fetchBooks();
});

// Edit Book
async function editBook(id) {
  const res = await fetch(`${API_URL}/${id}`);
  const book = await res.json();
  document.getElementById("bookId").value = book.id;
  document.getElementById("title").value = book.title;
  document.getElementById("description").value = book.description;
  document.getElementById("published_year").value = book.published_year;
  document.getElementById("author").value = book.author;
}

// Delete Book
async function deleteBook(id) {
  await fetch(`${API_URL}/${id}`, { method: "DELETE" });
  fetchBooks();
}

// Initial load
fetchBooks();
