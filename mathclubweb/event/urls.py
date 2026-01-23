from . import views
from django.urls import path
app_name = 'event'
urlpatterns = [
    path('event/', views.event, name='event'),
]