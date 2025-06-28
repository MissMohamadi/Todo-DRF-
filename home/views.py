from django.shortcuts import render
from todo.models import Todo
from django.http import  JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
def index_page(request):
    context = {
        'todos':Todo.objects.order_by('priority').all()
    }
    return render(request,'home/index.html', context)

def todos_json(request ):
    todos = list(Todo.objects.order_by('priority').all().values('title','is_done'))
    context = {'todos':todos}
    return JsonResponse(context)

@api_view(['GET'])
def todos_json_drf(request : Request):
    todos = list (Todo.objects.order_by('priority').all().values('title', 'is_done'))
    context = {'todos': todos}
    return Response(context, status=status.HTTP_200_OK)

