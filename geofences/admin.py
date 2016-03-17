from django.contrib import admin
from django.contrib.auth.models import Group, User
from leaflet.admin import LeafletGeoAdmin

from .models import EmployeeArea


admin.site.register(EmployeeArea, LeafletGeoAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
