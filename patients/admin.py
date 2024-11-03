from django.contrib import admin

# Register your models here.
from .models import Boxes, Project, Contact

admin.site.register(Boxes)
admin.site.register(Project)
admin.site.register(Contact)