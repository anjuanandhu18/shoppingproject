from django.urls import path
from . import views

app_name = 'restapi'
urlpatterns = [
    path('', views.apiview, name='apiview'),
    path('api_detail/<int:pk>', views.api_detail),
]
