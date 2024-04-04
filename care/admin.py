from django.contrib import admin

# Register your models here.
from .models import Pharmmodels, PharmConverse, PharmMessages

admin.site.register(Pharmmodels)
admin.site.register(PharmConverse)
admin.site.register( PharmMessages)

