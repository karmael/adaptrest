import json
from functools import wraps

from django.http import JsonResponse

from requests_toolbelt.multipart import decoder


def check_post_data(f):
    @wraps(f)
    def wrapper(request, session, *args, **kwargs):
        if request.body == b"":
            return JsonResponse({'msg': "invalid_param"}, status=400)
        if isinstance(request.body, bytes):
            try:
                return f(request, session, json.loads(request.body.decode("utf-8")), *args, **kwargs)
            except UnicodeDecodeError:
                lst = []
                for part in decoder.MultipartDecoder(request.body, request.META.get("CONTENT_TYPE")).parts:
                    disposition = part.headers[b'Content-Disposition']
                    params = {}
                    for dispPart in str(disposition).split(';'):
                        kv = dispPart.split('=', 2)
                        params[str(kv[0]).strip()] = str(kv[1]).strip('\"\'\t \r\n') if len(kv) > 1 else str(kv[0]).strip()
                    type = part.headers[b'Content-Type'] if b'Content-Type' in part.headers else None
                    lst.append({'content': part.content, "type": type, "params": params})
                return f(request, session, lst[0], *args, is_form=True, **kwargs)
        return f(request, session, json.loads(request.body), *args, **kwargs)
    return wrapper
