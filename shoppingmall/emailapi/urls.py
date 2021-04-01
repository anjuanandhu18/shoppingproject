from django.urls import path
from . import views

app_name = 'emailapi'
urlpatterns = [
    path('sendemail/', views.send_email, name='sendemail'),

]