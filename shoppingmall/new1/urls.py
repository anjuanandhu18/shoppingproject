from  django.urls import path
from .import views
app_name='new1'

urlpatterns =[
    path('log/',views.log,name='log'),
    ]