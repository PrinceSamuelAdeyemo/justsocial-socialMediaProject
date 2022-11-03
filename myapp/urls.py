from urllib.parse import urlparse
from django.urls import path
from . import views


urlpatterns = [
    # Normal urls
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('', views.homepage, name='homepage'),
    path('settings', views.settings, name='settings'),
    # path('profile/<str:pk>', views.profile, name = 'profile')
    # path('header', views.header, name='header'),
    path('logout', views.logout, name='logout'),
    path('profile/<str:pk>', views.profile, name = 'profile'),
    
    #Submitted data
    path('uploadpost', views.uploadpost, name='uploadpost'),
    path('like-post', views.like_post, name="like-post"),
    path('follow', views.follow, name="follow"),
    path('search_profile', views.search_profile, name="search_profile"),
    
]
