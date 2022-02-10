from django.db import models
from app.models import outlet
from django.utils import timezone

class Visit(models.Model):
    date = models.DateField(default=timezone.now())
    visit_outlet = models.ForeignKey(outlet.Outlet, on_delete=models.CASCADE, related_name='outlets_visit')
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def get_outlet(self):
        return self.visit_outlet
