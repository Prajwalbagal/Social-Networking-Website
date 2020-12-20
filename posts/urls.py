from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('by/<username>/', views.UserPost.as_view(), name='for_user'),
    path('by/<username>/<int:pk>', views.PostDetail.as_view(), name='single'),
    path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete'),
path('users_search/?search=<str:username>', views.SearchView.as_view(), name='user_search'),
    path('like/<int:pk>', views.likepost, name='like'),
    path('new/<int:pk>', views.dislikepost, name='dislike'),
]
