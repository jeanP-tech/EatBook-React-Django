from django.urls import path, include

from . import views
from .views import RegistrationAPI, LoginAPI, UserAPI

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailReview.as_view()),
    path('auth/register/', RegistrationAPI.as_view()),
    path('auth/login/', LoginAPI.as_view()),
    path('auth/user/', UserAPI.as_view()),
]
