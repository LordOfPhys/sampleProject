from django.db import models
from app.models import employee

class Outlet(models.Model):
    label = models.CharField(max_length=100, default='label')
    e = models.ForeignKey(employee.Employee, on_delete=models.CASCADE, related_name='outlets_employee')

    def get_employee(self):
        return self.e