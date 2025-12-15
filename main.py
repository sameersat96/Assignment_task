from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import uuid
app = FastAPI(title="Task Board API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class TaskCreate(BaseModel):
    title: str
class TaskUpdate(BaseModel):
    completed: Optional[bool] = None
class Task(BaseModel):
    id: str
    title: str
    completed: bool
    created_at: str
tasks: dict[str, dict] = {}
@app.get("/api/tasks", response_model=list[Task])
def list_tasks():
    return sorted(tasks.values(), key=lambda t: t["created_at"], reverse=True)
@app.post("/api/tasks", response_model=Task, status_code=201)
def add_task(task: TaskCreate):
    if not task.title.strip():
        raise HTTPException(status_code=400, detail="Task title cannot be empty")
    
    task_id = str(uuid.uuid4())
    new_task = {
        "id": task_id,
        "title": task.title.strip(),
        "completed": False,
        "created_at": datetime.utcnow().isoformat()
    }
    tasks[task_id] = new_task
    return new_task
@app.patch("/api/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, task_update: TaskUpdate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if task_update.completed is not None:
        tasks[task_id]["completed"] = task_update.completed
    
    return tasks[task_id]
@app.delete("/api/tasks/{task_id}", status_code=204)
def delete_task(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    del tasks[task_id]
    return None
@app.get("/")
def serve_frontend():
    return FileResponse("index.html")
