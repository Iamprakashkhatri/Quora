from django.urls import path
from .views import RegisterView
from .views import LoginView, RegisterView, DashboardView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register-view'),
    path('login/', LoginView.as_view(), name='login-view'),
    path('register/', RegisterView.as_view(), name='register-view'),
    path('dashboard/', DashboardView.as_view(), name='dashboard-view'),
    path('logout/', LogoutView.as_view(), name='logout-view')
]