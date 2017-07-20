from django.conf.urls import patterns, url
from django.shortcuts import render_to_response
from django.http import HttResponseRedirect
from django.utils import timezone
# from django.contrib.auth import authenticate, login
# from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
  # context = {
  # "time":"display"
  # }
  return render(request,'time_display/index.html')
