from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'clients/index.html')
 
def dashboard(request):
    return HttpResponse("Client dashboard, events")
 
def requirements(request):
    return HttpResponse("Submit requirements")
 
def success(request):
    return HttpResponse("Submission success, event details ")