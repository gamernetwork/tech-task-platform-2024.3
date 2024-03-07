# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import DetailView, ListView

from cms.models import Post

# Create your views here.

class PostView(DetailView):
    model = Post
    template_name = 'youreagamer/post.html'


class IndexView(ListView):
    model = Post
    template_name = 'youreagamer/index.html'


