from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from .models import Task
from rest_framework import status



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def TaskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializers(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TaskDetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializers(tasks,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def TaskCreate(request):
    serializer=TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def TaskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def TaskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response(status=status.HTTP_200_OK)