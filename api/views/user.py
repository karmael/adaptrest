from django.http import JsonResponse

from api.views.base import ProtectedView


class UserInfoView(ProtectedView):
    def get(self, request, session):
        return JsonResponse(self.user)
