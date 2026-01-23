from . import views
from django.urls import path
app_name = 'formerpresi'
urlpatterns = [
    path('formerpresi/', views.president, name='formerpresi'),
]