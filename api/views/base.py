import logging

import os
import jwt
from datetime import datetime

from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator


logger = logging.getLogger()


class ProtectedView(View):
    decorators = []

    @method_decorator(decorators)
    def dispatch(self, request, *args, **kwargs):
        self.session = request.session
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split(" ")
            if len(token) != 2 or token[0] != "Bearer":
                raise Exception()
            token = token[1]
        except Exception:
            return JsonResponse({
                "success": False,
                "msg": "token_error",
            }, status=400)
        try:
            jwt_decode = jwt.decode(
                token,
                os.environ.get('JWT_SECRET'),
                algorithms='HS256'
            )
        except Exception:
            return JsonResponse({
                "success": False,
                "msg": "jwt_decode_error",
            }, status=400)
        if jwt_decode['exp'] < datetime.now().timestamp():
            return JsonResponse({
                "success": False,
                "msg": "expired_login"
            })
        self.user = jwt_decode["user"]
        self.google_id = self.user['google_id']
        return super().dispatch(request, self.session, *args, **kwargs)
