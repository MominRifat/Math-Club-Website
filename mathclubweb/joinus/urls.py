from . import views
from django.urls import path
app_name = 'joinus'
urlpatterns = [
    path('joinus/', views.joinus, name='joinus'),
]