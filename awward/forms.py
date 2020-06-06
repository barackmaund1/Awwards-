from django import forms
from .models import Post
from pyuploadcare.dj.forms import ImageField

RATING= [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class PostForm(forms.ModelForm):
    photo = ImageField(label='')

    class Meta:
        model = Post
        fields = ( 'photo','title', 'url', 'description', 'technologies',)
