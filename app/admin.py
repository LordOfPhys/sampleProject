from django.contrib import admin
from .models.employee import Employee
from .models.visit import Visit
from .models.outlet import Outlet

admin.site.register(Employee)
admin.site.register(Visit)
admin.site.register(Outlet)