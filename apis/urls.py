from django.urls import path

from .views import ListProfile,DetailProfile

urlpatterns = [
    path('', ListProfile.as_view(),name='apis'),
    path('<int:pk>/', DetailProfile.as_view()),
]