from django.urls import path

from api.views.auth import LoginView
from api.views.user import UserInfoView

urlpatterns = [
    path('user_info/', UserInfoView.as_view()),
    path('login/', LoginView.as_view()),
    # TODO add more endpoints
]
