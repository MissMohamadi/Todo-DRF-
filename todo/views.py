from urllib import request
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodoSerializers, UserSerializer
from rest_framework import status
from .models import Todo, User
from rest_framework import generics,mixins
from rest_framework import viewsets


#region functiohn view
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



@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail_view(requset : Request, todo_id: int):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except todo.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)

    if requset.method == 'GET':
        serializer = TodoSerializers(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)


    elif requset.method == 'PUT':
        serializer = TodoSerializers(todo, data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    elif requset.method == 'DELETE':
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
#endregion

#region ClassBase view

class TodoListApiView(APIView):

    def get(self , request : Request):
        todos = Todo.objects.order_by('priority').all()
        serializer = TodoSerializers(todos, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request : Request):
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

class TodoDetailView(APIView):

    def get_object(self , todo_id : int):
        try:
            todo = Todo.objects.get(pk=todo_id)
            return todo
        except todo.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self,request : Request, todo_id : int):
        todo = self.get_object(todo_id)
        serializer = TodoSerializers(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request : Request, todo_id : int):
        todo = self.get_object(todo_id)
        serializer = TodoSerializers(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    def delete(self, request : Request, todo_id : int):
        todo = self.get_object(todo_id)
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)

#endregion

#region Mixins ApiView
class TodoListMixinsApiview(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializers

    def get(self,request : Request):
        return self.list(request)

    def post(self, request : Request):
        return self.create(request)

class TodoDetailMixinsApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializers

    def get(self, request : Request, pk : int):
        return self.retrieve(request, pk)

    def put(self, request : Request, pk : int):
        return self.update(request, pk)

    def delete(self, request : Request, pk : int):
        return self.destroy(request, pk)
#endregion

#region Generic Base View

class TodoListGenericApiView(generics.ListCreateAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializers

class TodoDetailGenericApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializers

#endregion

#region ViewSets

class TodoViewSetsApiView(viewsets.ModelViewSet):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializers

#endregion

#region User Generic ApiView

class UserGenericApiView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

#endregion