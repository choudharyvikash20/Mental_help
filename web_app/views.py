from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,authenticate,logout
from django.utils import timezone

def homepage(request):
    return render(request,'index.html')