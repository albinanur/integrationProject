from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name = 'index'),
    url(r'^courses$',views.create, name ='courses' ),
    url(r'^delete/(\d+)$', views.delete, name ='delete'),
    url(r'^destroy$', views.destroy, name = 'destroy'),
    url(r'^adduser$', views.addusertocourse, name ='adduser'),

]
