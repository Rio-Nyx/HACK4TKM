from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sub',views.submit,name='submit'),
    path('login',views.login,name='login'),
    path('auth',views.auth,name='auth')
]