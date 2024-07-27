# from django.urls import path
# # from .class_based_views import PostListCreateView, PostDetailView, CommentListCreateView

# urlpatterns = [
#     path('posts/', PostListCreateView.as_view(), name='post-list-create'),
#     path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
#     path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
# ]

from django.urls import path
from .views import register_user, create_post, get_list_post, get_update_detail, comment_list_create, delete_post

urlpatterns = [
    path('register/', register_user, name='register'),
    path('create_posts/', create_post, name='create'),
    path('list_post/', get_list_post, name='get_list_post'),
    path('update_detail/<int:id>/', get_update_detail, name='get_detail'),
    path('posts/<int:post_id>/comments/', comment_list_create, name='comment-list-create'),
    path('del_post/<int:id>/', delete_post, name='delete_post'),
]

