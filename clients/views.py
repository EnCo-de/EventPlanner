from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'clients/index.html')

def dashboard(request):
    return render(request, 'clients/dash.html')

@login_required 
def requirements(request):
    return HttpResponse("Submit your requirements for the event")
 
def success(request):
    return HttpResponse("Submission success, event details ")