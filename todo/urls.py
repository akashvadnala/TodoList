"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todoapp import  views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/',views.list_view, name="lists"),
    path('todolist/work/',views.add_work.as_view(), name="work_add"),
    path('todolist/project/',views.add_project.as_view(), name="project_add"),
    path('todolist/hobby/',views.add_hobby.as_view(), name="hobby_add"),
    path('todolist/workdelete/',views.delete_work.as_view(),name="work_delete"),
    path('todolist/projectdelete/',views.delete_project.as_view(),name="project_delete"),
    path('todolist/hobbydelete/',views.delete_hobby.as_view(),name="hobby_delete"),
]
