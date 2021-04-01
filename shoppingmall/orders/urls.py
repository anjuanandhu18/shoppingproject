from django.urls import path
from .import views
app_name='orders'

urlpatterns =[
    path('',views.crudhome,name='crudhome'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('education',views.education,name='education'),
    path('edit/<int:pk>',views.edit,name='edit'),

    ]
