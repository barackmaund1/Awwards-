from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView
from .models import Rating,Post
from .forms import PostForm,RatingForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from users.models import Profile
from django.http import JsonResponse
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



@login_required(login_url='login')
def project(request,project_id):
    current_user = request.user
    try:
        project = Post.objects.get(id=project_id)
    except Project.DoesNotExist:
        raise ObjectDoesNotExist()

   
    total_design = 0
    total_usability = 0 
    total_creativity = 0
    total_content = 0
    overall_score = 0

    ratings = Rating.objects.filter(project=project_id)

    if len(ratings) > 0:
        users = len(ratings)
    else:
        users = 1
    
    design = list(Rating.objects.filter(project=project_id).values_list('design',flat=True))
    usability = list(Rating.objects.filter(project=project_id).values_list('usability',flat=True))
    creativity = list(Rating.objects.filter(project=project_id).values_list('creativity',flat=True))
    content = list(Rating.objects.filter(project=project_id).values_list('content',flat=True))
    
    
    total_design=sum(design)/users
    total_usability=sum(usability)/users
    total_creativity=sum(creativity)/users
    total_content=sum(content)/users


    overall_score=(total_design+total_content+total_usability+total_creativity)/4

    project.design = total_design
    project.usability = total_usability
    project.creativity = total_creativity
    project.content = total_content
    project.overall = overall_score

    project.save()

    if request.method == 'POST':
        form = RatingForm(request.POST, request.FILES) 
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project= project
            
            if not Rating.objects.filter( project=project).exists():
                rating.overall_score = (rating.design+rating.usability+rating.creativity+rating.content)/4
                rating.save()
    else:
        form = RatingForm()
    return render(request, "awward/post_detail.html",{"project":project,
    "ratings":ratings,"form":form,  'total_design':total_design, 'total_usability':total_usability, 
    'total_creativity':total_creativity, 'total_content':total_content})
@login_required(login_url='login')
def search_project(request):
    if request.method == 'GET':
        title = request.GET.get("title")
        results = Post.objects.filter(title__icontains=title).all()
        
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'awward/results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'awward/results.html', {'message': message})

@login_required(login_url='login')
def upload(request):
    current_user = request.user
    profile =Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = current_user
            image.save()
            return redirect('projects')
    else:
        form = PostForm()
    return render(request, 'awward/post_form.html',  {'form': form,'profile':profile})


