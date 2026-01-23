from . import views
from django.urls import path
urlpatterns = [
    path('formerpresi/', views.president),
]