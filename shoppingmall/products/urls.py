from django.urls import path
from .import views
app_name='products'


urlpatterns =[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('home',views.home,name='home'),
    path('login',views.login),
    path('reg',views.reg,name='reg'),
    path('onlineindex', views.onlineindex, name='onlineindex')
]