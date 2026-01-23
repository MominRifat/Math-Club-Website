from . import views
from django.urls import path
urlpatterns = [
    path('resource/', views.resource),
]