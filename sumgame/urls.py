from django.urls import path, include
from django.conf.urls import url


from . import views
from .views import HomePageView

urlpatterns = [
    url(r"^$", HomePageView.as_view(), name="home"),
    # path('', views.index, name='index'),
    path('hobby_riddle', views.hobby_riddle, name='hobby_riddle'),
    path('login', views.login, name='login'), # path: 'login'?
    path('accounts/', include('django.contrib.auth.urls')),

]