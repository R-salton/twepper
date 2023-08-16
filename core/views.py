from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Profile
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
    return render(request, 'home.html')


def profile_list(request, massege=None):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {'profiles': profiles})
    else:
        messages.success(request, 'You Must First Log in to continue..!')

        return HttpResponseRedirect('/')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        return  render(request, 'profile.html', {"profile": profile})
    else:
        messages.success(request, 'You Must First Log in to continue..!')

        return HttpResponseRedirect('/')