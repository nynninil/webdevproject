from django.urls import path
from .views import *
from . import views
from django.urls import path
from CGM48FANS.views import *
from CGM48FANS.classview import *


CGM48FANS = ''
urlpatterns = [
    path('', views.page1, name='Home'),
    path('members/', views.members, name='members'),
    # path('informations/', views.members, name='members'),
    path('song/', views.song, name='song_index'),

    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', UserLoginView.as_view(), name='signin'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    path('home/', views.page1, name='home')


]