from . import views

from django.urls import include, path
from django.views.generic import TemplateView

from .views import ContactFormView

from .views import HomeView

from . import views


"""urlpatterns = [
    
]"""

urlpatterns = [
    #path('home/', HomeView.as_view(), name='home_url'),

    path('', TemplateView.as_view(template_name='blog/about.html'), name='landing_page_url'),
    path('home/', TemplateView.as_view(template_name='blog/home.html'), name='home_url'),
    path('index/', TemplateView.as_view(template_name='blog/index.html'), name='index_url'),
    path('about/', TemplateView.as_view(template_name='blog/about.html'), name='about_url'),
    path('contact/', ContactFormView.as_view(), name='contact_url'),
    path('contact/success/', TemplateView.as_view(template_name='blog/contact_success.html'), name='contact_success_url'),
    path('post/', TemplateView.as_view(template_name='blog/post.html'), name='post_url'),
    path('signup/', views.signup , name='signup_url'),
    path('accounts/login', TemplateView.as_view(template_name='registration/login.html'), name='login_url'),
    path('postlist/', views.PostList.as_view(), name='post_list_url'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.post_new, name='postnew_url'),
    
]

"""
urlpatterns = [
    path('home/', HomeView.as_view(), name='home_url'),
]
"""