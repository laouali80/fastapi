from fastapi import FastAPI
from model import Todo

app = FastAPI()

todos = [
    {
    "id": 1,
    "description": "test description"
},
    {
    "id": 2,
    "description": "test2 description"
},
    {
    "id": 3,
    "description": "test3 description"
}
]

@app.get('/')
def test():
    return {"response": "test"}


@app.get('/todos')
def get_todos():
    """Get todos."""
    return {"todos": todos}


@app.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    """Get a todo."""
    for todo in todos:

        if todo["id"] == todo_id:
            return {'todo': todo}
    return {"response": "Not found"}


@app.post('/todos')
def create_todo(addTodo: Todo):
    """Add a todo."""
    todos.append(addTodo)
    return {"response": "Added."}


@app.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    """Delete a todo."""
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
    return {"response": "Deleted."}


@app.put('/todos/{todo_id}')
def update_todo(todo_id: int, newTodo: Todo):
    """Update a todo."""
    for todo in todos:
        if todo['id'] == todo_id:
            todo['id'] = newTodo.id
            todo['description'] = newTodo.description
            return {"response": "Updated."}        
    return {"response": "Not found"}


