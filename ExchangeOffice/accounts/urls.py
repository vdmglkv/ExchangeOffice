from django.urls import path
from .views import office, register, edit
from django.contrib.auth.views import logout_then_login, LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='login'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
    path('', office, name='office'),
    path('edit/', edit, name='edit'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
