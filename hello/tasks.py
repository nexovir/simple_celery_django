
from celery import shared_task


@shared_task
def print_hello(self):
    print('salam abbas')