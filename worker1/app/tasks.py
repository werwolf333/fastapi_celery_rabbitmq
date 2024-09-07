import time
from .celery_app import celery


@celery.task(queue='task_queue')
def do_task():
    time.sleep(10)
    return f"do task"
