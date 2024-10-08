from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


CGM48FANS = ''
urlpatterns = [
    # path('', views.page1, name='Home'),
    path('', login_required(views.page1), name='Home'),
    path('members/', login_required(views.members), name='members'),
    # path('informations/', views.members, name='members'),
    path('song/', login_required(views.song), name='song'),
    path('signup/',views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),   
]