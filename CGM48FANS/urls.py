from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1, name='Home'),
    path('members/', views.members, name='members'),
    # path('informations/', views.members, name='members'),
    path('song/', views.song, name='song'),
]