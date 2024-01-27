from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Task
from .serializer import TaskSerializer, TaskValidateSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'PUT', 'DELETE'])
def task_view_id(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(data={'error: Director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = TaskValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': serializer.errors})
        task.title = serializer.validated_data.get('title')
        task.description = serializer.validated_data.get('description')
        task.completed = serializer.validated_data.get('completed')
        task.created = serializer.validated_data.get('created')
        task.save()
        return Response(data=TaskSerializer(task).data)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def task_view(request):
    if request.method == 'GET':
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(data=serializer.data)
    else:
        serializer = TaskValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})
        elif request.method == 'POST':
            title = request.data.get('title')
            description = request.data.get('description')
            completed = request.data.get('completed')
            created = request.data.get('created')
            task = Task.objects.create(title=title,description=description,completed=completed,created=created)
            serializer = TaskSerializer(task)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
