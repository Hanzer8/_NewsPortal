from datetime import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from .models import Post
from .filters import PostFilter


# Create your views here.
class PostsList(ListView):
   model = Post
   ordering = 'author'
   template_name = 'posts.html'
   context_object_name = 'posts'
   paginate_by = 2

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['filterset'] = self.filterset
      return context

   def get_queryset(self):
      queryset = super().get_queryset()
      self.filterset = PostFilter(self.request.GET, queryset)
      return self.filterset.qs


class PostDetail(DetailView):
   model = Post
   template_name = 'post.html'
   context_object_name = 'post'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['time_no2w'] = datetime.utcnow()
      return context

class PostCreate(LoginRequiredMixin, CreateView):
   raise_exception = True
   form_class = PostForm
   model = Post
   template_name = 'post_create.html'


class PostUpdate(LoginRequiredMixin, UpdateView):
   raise_exception = True
   form_class = PostForm
   model = Post
   template_name = 'post_edit.html'


class PostDelete(LoginRequiredMixin, DeleteView):
   raise_exception = True
   model = Post
   template_name = 'post_delite.html'
   success_url = reverse_lazy('posts')
