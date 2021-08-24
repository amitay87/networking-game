from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hobby_riddle', views.hobby_riddle, name='hobby_riddle'),
    path('', views.login, name='login') # path: 'login'?
]