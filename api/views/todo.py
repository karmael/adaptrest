from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo


@api_view(['GET'])
def TodoOverview(request):
    api_urls = {
        'List' : '/todo-list/',
        'Detail View' : '/todo-detail/<int:pk>/',
        'Create' : '/todo-create/',
        'Update' : '/todo-update/<int:pk>/',
        'Delete' : '/todo-delete/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def TodoList(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def TodoDetail(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def TodoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
	
@api_view(['POST'])
def TodoUpdate(request, pk):
    todo = Todo.objects.get(id = pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def TodoDelete(request, pk):
    todo = Todo.objects.get(id = pk)
    todo.delete()
    return Response("Todo deleted successfully.")
