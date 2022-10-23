from myapp.models import Employee
from datetime import datetime


employee_data = [
    {
        'name': 'nghiahm4',
        'kpi': '90%',
        'okrs': True,
        'salary': 500
    },
    {
        'name': 'nguyennt65',
        'kpi': '0%',
        'okrs': False,
        'salary': 100
    },
    {
        'name': 'minhnc27',
        'kpi': '80%',
        'okrs': True,
        'salary': 700
    },
        {
        'name': 'tynp',
        'kpi': '50%',
        'okrs': False,
        'salary': 900
    },
    {
        'name': 'nguyennt63',
        'kpi': '80%',
        'okrs': True,
        'salary': 400
    }
]


new_employee_data = [ 
    {
        'name': 'nhandd3',
        'kpi': '70%',
        'okrs': True,
        'salary': 900
    },
    {
        'name': 'thiennk5',
        'kpi': '50%',
        'okrs': True,
        'salary': 200
    },
    {
        'name': 'mantn2',
        'kpi': '80%',
        'okrs': False,
        'salary': 700
    },
        {
        'name': 'lanlt23',
        'kpi': '30%',
        'okrs': False,
        'salary': 700
    },
    {
        'name': 'nghiahm4',
        'kpi': '50%',
        'okrs': True,
        'salary': 800
    },
    {
        'name': 'duongntt63',
        'kpi': '80%',
        'okrs': True,
        'salary': 500
    },
    {
        'name': 'tailm2',
        'kpi': '80%',
        'okrs': True,
        'salary': 400
    },
    {
        'name': 'nguyennt65',
        'kpi': '70%',
        'okrs': False,
        'salary': 200
    },
    {
        'name': 'minhnc27',
        'kpi': '50%',
        'okrs': True,
        'salary': 300
    },
]

def create_data():
    for data in employee_data:
        Employee.objects.create(
            name=data['name'], 
            kpi=data['kpi'],
            okrs=data['okrs'],
            salary=data['salary']
        )


def update_data():
    for data in new_employee_data:
        updated = Employee.objects.filter(name=data['name']).update(kpi=data['kpi'], salary=data['salary'])
        if not updated:
            Employee.objects.create(
                name=data['name'], 
                kpi=data['kpi'],
                okrs=data['okrs'],
                salary=data['salary']
            )
        
def delete_data():
    Employee.objects.all().delete()