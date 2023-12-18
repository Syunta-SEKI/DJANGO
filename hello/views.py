from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.views import generic

class IndexView(generic.ListView):
    model = Article
    template_name = "hello/index.html"



