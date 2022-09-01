from django.urls import path

from CRUDApp import views

urlpatterns = [
    path('', views.homeview, name='homeview'),
    path('loginview', views.loginview, name='loginview'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('userhome', views.userhome, name='userhome'),
    path('userregister', views.userregister, name='userregister'),
    path('logoutview',views.logoutview,name='logoutview'),
    path('profileupdate/<int:id>',views.profileupdate,name='profileupdate'),
    path('profiledelete/<int:id>',views.profiledelete,name='profiledelete'),
    path('userdelete/<int:id>',views.userdelete,name='userdelete')

]