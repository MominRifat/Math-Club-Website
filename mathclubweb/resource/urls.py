from . import views
from django.urls import path
app_name = 'resource'
urlpatterns = [
    path('resource/', views.resource, name='resource'),
]