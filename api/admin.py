from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Exercise)
admin.site.register(models.Guide)
admin.site.register(models.Tags)
admin.site.register(models.Equipment)