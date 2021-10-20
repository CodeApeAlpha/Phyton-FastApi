from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import uvicorn


class Todo(BaseModel):
    name: str
    due_date: str
    description: str


app = FastAPI()

store_todo = []


#  Home Get Request
@app.get('/')
async def home():
    return {
        "Hello": "User"
    }


#  Post Request

@app.post("/todo/")
async def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo


@app.get("/todo/", response_model=List[Todo])
async def get_all_todo():
    return store_todo


@app.get("/todo/{t_index_id}")
async def get_todo(t_index_id: int):
    try:

        return store_todo[t_index_id]

    except:

        raise HTTPException(status_code=404, detail="Todo Not Found")


@app.put("/todo/{t_index_id}")
async def update_todo(t_index_id: int, todo: Todo):
    try:
        store_todo[t_index_id] = todo
        return store_todo[t_index_id]

    except:

        raise HTTPException(status_code=404, detail="Todo Not Found")


@app.delete("/todo/{t_index_id}")
async def delete_todo(t_index_id: int):
    try:

        obj = store_todo[t_index_id]
        store_todo.pop(t_index_id)
        return obj

    except:

        raise HTTPException(status_code=404, detail="Todo Not Found")


uvicorn.run(app)
