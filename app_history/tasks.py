from celery import shared_task


@shared_task()
def simple_task():
    print("1.2.3")
