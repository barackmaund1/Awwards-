from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView
from .models import Rating,Post
from .forms import UploadForm
# Create your views here.
class PostListView(LoginRequiredMixin,ListView):
    model=Post
    context_object_name = 'projects'
    ordering = ['-date_posted']
   
class UserPostListView(ListView,LoginRequiredMixin):
    model = Post
    # <app>/<model>_<viewtype>.html image_list.html
    context_object_name = 'images'
    paginate_by = 7

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Image.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView,LoginRequiredMixin):
    model = Post 
    context_object_name = 'project'

    
     
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class=UploadForm
    # success_url = 'user/<str:username>'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class=UploadForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

