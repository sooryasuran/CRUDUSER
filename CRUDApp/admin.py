from django.contrib import admin

# Register your models here.
from CRUDApp import models

admin.site.register(models.Login)
admin.site.register(models.Profile)