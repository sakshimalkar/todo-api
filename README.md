# 📝 Todo REST API

A simple REST API to manage tasks — built with Python and FastAPI.

---
### Live Demo:


## 🛠️ Technologies & Skills Used

- **Python** — core programming language
- **FastAPI** — web framework for building REST APIs
- **Pydantic** — data validation and schema definition
- **Uvicorn** — ASGI server to run the application
- **Swagger UI** — auto-generated interactive API documentation
- **REST API concepts** — GET, POST, PUT, DELETE, HTTP status codes, JSON

---

## 📮 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/todos` | Create a new task |
| GET | `/todos` | Get all tasks |
| GET | `/todos/{id}` | Get a single task |
| PUT | `/todos/{id}` | Update a task |
| DELETE | `/todos/{id}` | Delete a task |

---

## ⚙️ How to Run

```bash
pip install fastapi uvicorn
python -m uvicorn main:app --reload
```

Then open `http://127.0.0.1:8000/docs` to test all endpoints.

---

## 👩‍💻 Author

**Sakshi Malkar**  
🔗 [LinkedIn](https://linkedin.com/in/sakshi-malkar) · [GitHub](https://github.com/sakshimalkar)
