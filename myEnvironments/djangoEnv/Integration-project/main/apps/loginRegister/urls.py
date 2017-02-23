from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index) ,
    url(r'^registration$', views.create_user),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    


]
