from django.urls import path
from .import views
app_name='new'

urlpatterns =[
    path('register',views.register,name='register'),
    path('delete/<int:id>',views.delete),
    ]