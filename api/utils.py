import json
from functools import wraps

from django.http import JsonResponse


def check_post_data(f):
    @wraps(f)
    def wrapper(request, session, *args, **kwargs):
        if request.body == b"":
            return JsonResponse({'msg': "invalid_param"}, status=400)
        if isinstance(request.body, bytes):
            return f(request, session, json.loads(request.body.decode("utf-8")), *args, **kwargs)
        return f(request, session, json.loads(request.body), *args, **kwargs)
    return wrapper
