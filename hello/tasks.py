
from celery import shared_task


@shared_task
def print_hello():
    print("salam abbas")
    return "done"