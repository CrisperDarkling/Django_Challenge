from django.contrib import admin
from .models import TodoItem
from .models import EditItem

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(EditItem)