from django import forms
from .models import Post,Rating
from pyuploadcare.dj.forms import ImageField

RATING= [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['overall_score','profile','project']

class PostForm(forms.ModelForm):
    photo = ImageField(label='')

    class Meta:
        model = Post
        fields = ['photo', 'title', 'url', 'description', 'technologies']