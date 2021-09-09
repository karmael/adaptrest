import os
import jwt
from datetime import datetime, timedelta

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import HttpResponse

from google.oauth2 import id_token
from google.auth.transport import requests

from api.models import User


def create_or_save(user_def, to_update=None):
    try:
        user = User.objects.get(
            google_id=user_def['google_id']
        )
        for key, value in user_def.items():
            if to_update is not None:
                if key in to_update:
                    setattr(user, key, value)
        user.save(update_fields=to_update)
    except User.DoesNotExist:
        user = User(**user_def)
        user.save()
    return user


class LoginView(View):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        token = request.META.get('HTTP_OAUTH_TOKEN')
        idinfo = None
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), os.environ.get('CLIENT_ID'))
        except ValueError:
            return HttpResponse(status=400)
        if 'hd' not in idinfo:
            idinfo['hd'] = None
        user_def = {
            'google_id': idinfo['sub'],
            'username': idinfo['given_name'],
            'fullname': idinfo['given_name'],
            'picture': idinfo['picture'],
            'company': idinfo['hd'],
            'email': idinfo['email'],
        }
        data = {
            'user': user_def,
            'exp': datetime.now() + timedelta(hours=24)
        }
        encoded_jwt = jwt.encode(
            payload=data,
            key=os.environ.get('JWT_SECRET'),
            algorithm='HS256'
        )
        encoded_jwt = encoded_jwt.decode("utf-8")

        create_or_save(user_def)
        request.session['token'] = encoded_jwt
        return JsonResponse({
            "token": encoded_jwt,
            "user": user_def,
        })
