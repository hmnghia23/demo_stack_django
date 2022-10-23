from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    kpi = models.CharField(max_length=200, null=True, blank=True)
    okrs = models.BooleanField()
    salary = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return f'{self.name} - {self.kpi} - {self.okrs} - {self.salary} - {self.updated}'

    class Meta:
        db_table = 'Employee'