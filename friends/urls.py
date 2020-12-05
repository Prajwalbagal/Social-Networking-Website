from django.urls import path
from . import views
from django.conf.urls import url
app_name='friends'

urlpatterns=[
url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.friendoperation, name='friendoperation'),
url(r'^friendslist/$',views.listfriends,name='listfriends'),
]
