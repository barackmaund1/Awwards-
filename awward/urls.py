from django.urls import path
from . import views
from .views import PostListView,PostCreateView,PostDetailView,UserPostListView,PostUpdateView,PostDeleteView
urlpatterns = [
    path('', PostListView.as_view(), name='projects'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-projects'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='project-detail'),
    path('post/new/', PostCreateView.as_view(), name='project-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='project-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='project-delete'),
]