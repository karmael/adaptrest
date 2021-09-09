from django.urls import path

from api.views.auth import LoginView
from api.views.user import UserInfoView
from api.views.user_auth import RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, LogoutAllView, ForgotPasswordView
from api.views.todo import TodoAllView, TodoView, TodoDetailView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('user_info/', UserInfoView.as_view()),
    path('login_google/', LoginView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='auth_forgot_password'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
    path('todo/', TodoAllView.as_view()),
    path('todo/<int:todo_id>/', TodoView.as_view()),
    path('todo/<int:todo_id>/<int:item_id>/', TodoDetailView.as_view()),
]
