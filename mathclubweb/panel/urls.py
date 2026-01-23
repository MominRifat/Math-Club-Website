from . import views
from django.urls import path
app_name = 'panel'
urlpatterns = [
    path('panel/', views.panel, name='panel'),
]