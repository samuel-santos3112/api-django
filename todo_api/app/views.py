from app.models import Todo
from app.serializers import TodoSerializer

from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

class TodoListAndCreate(APIView):
    def get(self, request):
        todoList = Todo.objects.all()
        serializer = TodoSerializer(todoList, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailChangeAndDelete(APIView):
    def get_object(self, id):
        try:
            return Todo.objects.get(pk=id)
        except Todo.DoesNotExist:
            raise NotFound()

    def put(self, request, id):
        todo = self.get_object(id)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        todo = self.get_object(id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        todo = self.get_object(id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data) 


       