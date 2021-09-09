from api.serializers import TodoSerializer, TodoItemSerializer
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

    def update(self, request, todo_id):
        try:
            to_update = request.body
            # TODO validate
            todo = Todo.objects.filter(
                user=self.user["google_id"],
                todo_id=todo_id
            )
            if todo is not None:
                todo.update(
                    name=to_update["name"]
                )
            return JsonResponse({
                "success": True,
                "msg": TodoItemSerializer(todo).data,
            })
        except Exception:
            return JsonResponse({
                "success": False,
            }, status=400)

    def post(self, request, todo_id):
        try:
            to_post = request.body
            # TODO validate
            todo = Todo.objects.create(
                user=self.user["google_id"],
                name=to_post["name"]
            )
            return JsonResponse({
                "success": True,
                "msg": TodoSerializer(todo).data,
            })
        except Exception:
            return JsonResponse({
                "success": False,
            }, status=400)

    def delete(self, request, todo_id):
        try:
            todo = Todo.objects.filter(
                user=self.user["google_id"],
                todo_id=todo_id,
            )
            if todo is not None:
                todo.destroy()
            return JsonResponse({
                "success": True,
            })
        except Exception:
            return JsonResponse({
                "success": False,
            }, status=400)


class TodoDetailView(ProtectedView):
    def get(self, request, todo_id, item_id):
        return JsonResponse({
            "items": TodoSerializer(TodoItem.objects.filter(todo_id=todo_id, item_id=item_id), many=True).data,
        })

    def update(self, request, todo_id, item_id):
        try:
            to_update = request.body
            # TODO validate
            todo_item = TodoItem.objects.filter(
                user=self.user["google_id"],
                todo_id=todo_id,
                item_id=item_id,
            )
            if todo_item is not None:
                todo_item.update(
                    desc=to_update["desc"],
                    image=to_update["image"],
                    status=to_update["status"],
                )
            return JsonResponse({
                "success": True,
                "msg": TodoItemSerializer(todo_item).data,
            })
        except Exception:
            return JsonResponse({
                "success": False,
            }, status=400)

    def post(self, request, todo_id):
        try:
            to_post = request.body
            # TODO validate
            todo_item = TodoItem.objects.create(
                todo_id=todo_id,
                desc=to_post["desc"],
                image=to_post["image"],
                status=to_post["status"],
            )
            return JsonResponse({
                "success": True,
                "msg": TodoItemSerializer(todo_item).data,
            })
        except Exception:
            return JsonResponse({
                "success": False,
            }, status=400)

    def delete(self, request, todo_id, item_id):
        try:
            todo_item = TodoItem.objects.filter(
                todo_id=todo_id,
                item_id=item_id,
            )
            if todo_item is not None:
                todo_item.destroy()
            return JsonResponse({
                "success": True,
            })
        except Exception:
            return JsonResponse({
                "success": False,
            }, status=400)
