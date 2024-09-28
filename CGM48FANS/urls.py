from django.urls import path
from . import views


CGM48FANS = ''
urlpatterns = [
    path('', views.page1, name='Home'),
    path('members/', views.members, name='members'),
    # path('informations/', views.members, name='members'),
    path('song/', views.song, name='song'),
    path('signup/',views.signup, name='signup'),
    path('signin/',views.signin, name='signin')   
]