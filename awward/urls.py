from django.urls import path
from . import views
from .views import PostListView,UserPostListView
urlpatterns = [
    path('', PostListView.as_view(), name='projects'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-projects'),
    path('project/<int:project_id>', views.project, name='project'),
    path('post/new/', views.upload, name='project-create'),
    path('search/', views.search_project, name='search'),
    
   
]