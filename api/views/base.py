# import logging

# import os
# import jwt
# import json
# from datetime import datetime

# from django.views import View
# from django.http import JsonResponse
# from django.utils.decorators import method_decorator


# logger = logging.getLogger()


# class ProtectedView(View):
#     decorators = []

#     @method_decorator(decorators)
#     def dispatch(self, request, *args, **kwargs):
#         self.session = request.session
#         token = request.META.get('HTTP_ADAPT_TOKEN')
#         jwt_decode = jwt.decode(
#             token,
#             os.environ.get('JWT_SECRET'),
#             algorithm='HS256'
#         )
#         if jwt_decode['exp'] < datetime.now().timestamp():
#             return JsonResponse({
#                 "success": False,
#                 "msg": "expired_login"
#             })
#         self.user = jwt_decode["user"]
#         self.google_id = self.user['google_id']
#         if request.body:
#             self.payload = json.loads(request.body)
#         return super().dispatch(request, self.session, *args, **kwargs)
