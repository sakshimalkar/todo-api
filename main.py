from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# In-memory storage
todos = []
counter = {"id": 1}

# Schema
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False

# Routes
@app.get("/")
def home():
    return {"message": "Todo API is running!"}

@app.post("/todos", status_code=201)
def create_todo(todo: TodoCreate):
    new_todo = {
        "id": counter["id"],
        "title": todo.title,
        "description": todo.description,
        "done": todo.done
    }
    todos.append(new_todo)
    counter["id"] += 1
    return new_todo

@app.get("/todos")
def get_all_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_one_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return {"error": "Todo not found"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated: TodoCreate):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = updated.title
            todo["description"] = updated.description
            todo["done"] = updated.done
            return todo
    return {"error": "Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos.pop(i)
            return {"message": "Deleted successfully"}
    return {"error": "Todo not found"}
