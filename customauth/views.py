from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import warning, info
from django.shortcuts import render, redirect
from .models import ClientUserModel
from .forms import ClientCreationForm


# Create your views here.
def client_create(request):
    form = ClientCreationForm()
    if request.method=='POST':
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('login')
    return render(request, 'customauth/create.html', {'form': form})

def customlogin(request):
    if request.method=='POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
                login(request, user)
                # Redirect to a success page.
                ...
                return redirect('dashboard')
        else:
                # Return an 'invalid login' error message.
                warning(request, 'Նշված օգտագործողի հավատարմագրերը սխալ են: \n Փոխեք օգտվողի հավատարմագրերը: Կրկին փորձեք մուտք գործել \n Wrong user login credentials. Try again')
    return render(request, 'customauth/login.html')

@login_required
def client_edit(request):
    model = ClientUserModel
    form = ClientCreationForm()
    return render(request, 'customauth/client_edit.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    info(request, 'Դուք դուրս եք եկել: \n Կրկին փորձեք մուտք գործել \n You logged out from your account.')
    return redirect('index')
