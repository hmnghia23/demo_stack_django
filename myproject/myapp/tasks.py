from celery import shared_task
from myapp.handlers.process_employee_data import (
    create_data,
    update_data,
    delete_data
)

@shared_task(name='CREATE_DB')
def create():
    create_data()

@shared_task(name='UPDATE_DB')
def update():
    update_data()

@shared_task(name='DELETE_DB')
def delete():
    delete_data()