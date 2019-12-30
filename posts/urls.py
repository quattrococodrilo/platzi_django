from django.urls import path
from posts import views

urlpatterns = [
    path('', views.PostsFeedView.as_view(), name='feed'),
    path('posts/new/', views.CreatePostView.as_view(), name='create_post'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='detail')
]
