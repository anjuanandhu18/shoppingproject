from django.urls import path
from .import views
app_name='new2'

urlpatterns =[ path('log1/' ,views.log1, name='log1')]