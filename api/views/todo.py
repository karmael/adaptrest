from api.serializers import TodoSerializer
from django.http.response import JsonResponse
from api.models import Todo, TodoItem
from api.views.base import ProtectedView


class TodoAllView(ProtectedView):
    def get(self, request):
        return JsonResponse({
            "items": TodoSerializer(Todo.objects.filter(user=self.user["google_id"]), many=True).data,
        })


class TodoView(ProtectedView):
    def get(self, request, todo_id):
        return JsonResponse({
            "items": TodoSerializer(TodoItem.objects.filter(todo_id=todo_id), many=True).data,
        })


class TodoDetailView(ProtectedView):
    def get(self, request, todo_id, item_id):
        return JsonResponse({
            "items": TodoSerializer(TodoItem.objects.filter(todo_id=todo_id, item_id=item_id), many=True).data,
        })
