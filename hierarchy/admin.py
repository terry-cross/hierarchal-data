from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from hierarchy.models import Hierarchy

# Register your models here.
admin.site.register(Hierarchy, DraggableMPTTAdmin)