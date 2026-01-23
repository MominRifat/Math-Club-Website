from . import views
from django.urls import path
urlpatterns = [
    path('panel/', views.panel),
]