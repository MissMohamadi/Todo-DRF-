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
    if request.method == 'GET':
        todos = Todo.objects.order_by('priority').all()
        todo_serialized = TodoSerializers(todos, many=True)
        return  Response( todo_serialized.data ,status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(None, status.HTTP_400_BAD_REQUEST)
