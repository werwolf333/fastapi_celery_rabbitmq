import time
from celery import chain
from .celery_app import celery


@celery.task(queue='task_queue')
def step1():
    time.sleep(5)
    return "result step1"


@celery.task(queue='task_queue')
def step2(result):
    time.sleep(5)
    return f"{result} and result step2"


def make_buns():
    bun_chain = chain(
        step1.s(),
        step2.s(),
    )
    return bun_chain.apply_async()
