from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

def home(request):

    return render(request, 'home.html', {'posts': all_posts})
