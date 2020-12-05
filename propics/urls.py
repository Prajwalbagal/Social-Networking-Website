from django.urls import path
from . import views

app_name = 'propics'

urlpatterns = [

    path('newpic/', views.ProfileView.as_view(), name='create'),
    path('list/', views.ProfileList.as_view(), name='list'),

]
