from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .tasks import do_task
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def create_task(request: Request, task_count: int = Form(...)):
    task_ids = []
    for i in range(task_count):
        task = do_task.delay()
        task_ids.append(task.id)

    return templates.TemplateResponse("main.html", {"request": request, "task_ids": task_ids})
