from django.contrib import admin
from .models import Task, Category

admin.site.register(Category)
admin.site.register(Task)
