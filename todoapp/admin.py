from django.contrib import admin

from .models import ToDoWork,ToDoHobby,ToDoProject

admin.site.register(ToDoWork)
admin.site.register(ToDoProject)
admin.site.register(ToDoHobby)
