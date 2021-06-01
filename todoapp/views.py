from django.shortcuts import render

from django.views.generic import ListView,View

from django.http import JsonResponse

from .models import ToDoWork,ToDoProject,ToDoHobby

# Create your views here.
def list_view(request):
    context = {}
    works = ToDoWork.objects.all()
    projects = ToDoProject.objects.all()
    hobbies = ToDoHobby.objects.all()
    context['works'] = works
    context['projects'] =projects
    context['hobbies'] = hobbies
    return render(request,'todo.html',context)

class add_work(View):
    def get(self, request):
        msg = request.GET.get('msg',None)
        obj = ToDoWork.objects.create(msg=msg)
        data={'id':obj.id,'msg':obj.msg}
        return JsonResponse(data)

class add_project(View):
    def get(self, request):
        msg = request.GET.get('msg',None)
        obj = ToDoProject.objects.create(msg=msg)
        data={'id':obj.id,'msg':obj.msg}
        return JsonResponse(data)

class add_hobby(View):
    def get(self, request):
        msg = request.GET.get('msg',None)
        obj = ToDoHobby.objects.create(msg=msg)
        data={'id':obj.id,'msg':obj.msg}
        return JsonResponse(data)

class delete_work(View):
    def get(self, request):
        id = request.GET.get('id',None)
        ToDoWork.objects.get(id=id).delete()
        data={
            'deleted':True
        }
        return JsonResponse(data)

class delete_project(View):
    def get(self, request):
        id = request.GET.get('id',None)
        ToDoProject.objects.get(id=id).delete()
        data={
            'deleted':True
        }
        return JsonResponse(data)

class delete_hobby(View):
    def get(self, request):
        id = request.GET.get('id',None)
        ToDoHobby.objects.get(id=id).delete()
        data={
            'deleted':True
        }
        return JsonResponse(data)