# main_app/celery_app.py
from kombu import Queue
from celery import Celery

def make_celery():
    return Celery(
        "app",
        broker="amqp://guest:guest@rabbitmq//",
        backend="rpc://"
    )


celery = make_celery()
celery.conf.task_queues = (
    Queue('task_queue', routing_key='task_queue'),
)
celery.conf.worker_prefetch_multiplier = 2
celery.conf.task_routes = {
    'app.tasks.process_data': {'queue': 'task_queue'},
}
celery.autodiscover_tasks(['app.tasks'])

