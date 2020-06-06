from django.db import models
from pyuploadcare.dj.models import ImageField
import datetime as dt
from django.contrib.auth.models import User
from users.models import Profile
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=200, blank=True)
    photo = ImageField(manual_crop='1280x720')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def delete_post(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()

    def save_post(self):
        self.save()

class Rating(models.Model):
    CHOICES= (1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)

    design = models.IntegerField(choices=CHOICES,blank=True,default=0)
    usability = models.IntegerField(choices=CHOICES, blank=True,default=0)
    creativity = models.IntegerField(choices=CHOICES, blank=True,default=0)
    content = models.IntegerField(choices=CHOICES, blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)
    project = models.ForeignKey(Post, null=True,on_delete=models.CASCADE, related_name='rater')
    
    def save_rating(self):
        self.save()

    def __str__(self):
        return self.design