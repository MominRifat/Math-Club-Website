from . import views
from django.urls import path
urlpatterns = [
    path('joinus/', views.joinus),
]