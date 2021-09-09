import io
from django.core.files.images import ImageFile

from django.utils.decorators import method_decorator
from api.serializers import TodoSerializer, TodoItemSerializer
from django.http.response import JsonResponse
from api.models import Todo, TodoItem
from api.views.base import ProtectedView

from api.utils import check_post_data


class TodoAllView(ProtectedView):
    def get(self, request, session):
        return JsonResponse({
            "items": TodoSerializer(Todo.objects.filter(user_id=self.user["google_id"]), many=True).data,
        })

    @method_decorator(check_post_data)
    def post(self, request, session, data):
        try:
            # TODO validate data
            todo = Todo.objects.create(
                user_id=self.user["google_id"],
                name=data["name"],
            )
            return JsonResponse({
                "success": True,
                "msg": TodoSerializer(todo).data,
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "msg": str(e),
            }, status=400)


class TodoView(ProtectedView):
    def get(self, request, session, todo_id):
        return JsonResponse({
            "items": TodoItemSerializer(TodoItem.objects.filter(todo_id=todo_id), many=True).data,
        })

    @method_decorator(check_post_data)
    def put(self, request, session, data, todo_id):
        try:
            # TODO validate
            todo = Todo.objects.filter(
                user_id=self.user["google_id"],
                id=todo_id,
            )
            if todo is not None:
                todo.update(
                    name=data["name"]
                )
            return JsonResponse({
                "success": True,
                "msg": TodoSerializer(todo.first()).data,
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "msg": str(e),
            }, status=400)

    def delete(self, request, session, todo_id):
        try:
            todo = Todo.objects.filter(
                user_id=self.user["google_id"],
                id=todo_id,
            )
            if todo is not None:
                todo.delete()
            return JsonResponse({
                "success": True,
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "msg": str(e),
            }, status=400)

    @method_decorator(check_post_data)
    def post(self, request, session, data, todo_id):
        try:
            # TODO validate
            todo_item = TodoItem.objects.create(
                todo_id=todo_id,
                **data,
            )
            return JsonResponse({
                "success": True,
                "msg": TodoItemSerializer(todo_item).data,
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "msg": str(e),
            }, status=400)


class TodoDetailView(ProtectedView):
    def get(self, request, session, todo_id, item_id):
        return JsonResponse({
            "items": TodoItemSerializer(TodoItem.objects.filter(todo_id=todo_id, item_id=item_id).first).data,
        })

    @method_decorator(check_post_data)
    def put(self, request, session, data, todo_id, item_id, is_form=False):
        try:
            # TODO validate
            if is_form:
                data = {
                    "image": ImageFile(io.BytesIO(data["content"]), name=data["params"]["filename"]),
                }
            todo_item = TodoItem.objects.filter(
                todo_id=todo_id,
                id=item_id,
            )
            if todo_item is not None:
                todo_item.update(
                    **data
                )
            return JsonResponse({
                "success": True,
                "msg": TodoItemSerializer(todo_item.first()).data,
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "msg": str(e),
            }, status=400)

    def delete(self, request, session, todo_id, item_id):
        try:
            todo_item = TodoItem.objects.filter(
                todo_id=todo_id,
                id=item_id,
            )
            if todo_item is not None:
                todo_item.delete()
            return JsonResponse({
                "success": True,
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "msg": str(e),
            }, status=400)
