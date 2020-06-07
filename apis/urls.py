from django.urls import path

from .views import ListProfile,DetailProfile,ListPost,DetailPost

urlpatterns = [
    path('', ListProfile.as_view(),name='apis'),
    path('<int:pk>/', DetailProfile.as_view()),
    path('project/', ListPost.as_view(),name='project-apis'),
    path('<int:pk>/', DetailPost.as_view()),
]