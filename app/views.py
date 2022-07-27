from django.shortcuts import render
import os
from django.conf import settings

def home(request):
    return render(request, 'home.html')
