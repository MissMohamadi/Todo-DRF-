from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import TodoSerializers
from rest_framework import status
from .models import Todo

# Create your views here.

@api_view(['GET', 'POST'])
def all_todo(request : Request):
    todos = Todo.objects.order_by('priority').all()
    todo_serialized = TodoSerializers(todos, many=True)
    return  Response( todo_serialized.data ,status.HTTP_200_OK)