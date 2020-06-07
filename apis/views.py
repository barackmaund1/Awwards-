from django.shortcuts import render
from rest_framework import generics
from users import models
from awward import models
from .serializers import ProfileSerializer,PostSerializer
# Create your views here.
class ListProfile(generics.ListCreateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer

class DetailProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileSerializer    

class ListPost(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer   
class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer         