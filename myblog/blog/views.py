from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views import generic
from .models import Post

from django.views.generic import TemplateView

from django.views.generic.edit import FormView
from .forms import ContactForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import PostForm

from django.utils import timezone


# Create your views here.

class HomeView(TemplateView):
    template_name = 'blog/home.html'

class ContactFormView(FormView):
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = 'success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home_url')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog/sidebar.html', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form}) 