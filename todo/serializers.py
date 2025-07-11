from rest_framework import serializers
from .models import Todo, User


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
         model = Todo
         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializers(read_only=True, many=True)
    class Meta:
        model = User
        fields = '__all__'


