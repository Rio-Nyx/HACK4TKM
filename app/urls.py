from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sub',views.submit,name='submit'),
    path('login',views.login,name='login'),
    path('auth',views.auth,name='auth'),
    path('compute',views.compute,name='compute'),
    path('dist', views.dist, name='dist'),
    path('optimal', views.optimal, name='optimal'),
    path('opt', views.opt, name='opt'),

]