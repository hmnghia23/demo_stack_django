import os
import django
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.handlers.process_employee_data import *

if __name__ == '__main__':
    print('STARTED')
    start = time.time()
    # create_data()
    # update_data()
    # delete_data()
    print("FINISHED: ", time.time() - start)