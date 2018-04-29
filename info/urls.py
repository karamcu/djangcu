from django.conf.urls import  url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^info/plus/1/$', views.hours_ahead),
    url(r'^info/plus/2/$', views.hours_ahead),
    url(r'^info/plus/3/$', views.hours_ahead),
    url(r'^info/plus/4/$', views.hours_ahead),
]