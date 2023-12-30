from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import warning, info, success
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ClientUserModel
from .forms import ClientCreationForm


# Create your views here.
def client_create(request):
    form = ClientCreationForm()
    if request.method=='POST':
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            client = form.save()
            html_message = '''<strong>Շնորհավորանքներ !</strong> 
                <br>Ձեր գրանցման դիմումը հաջողությամբ ընդունվել է: 
                Փորձեք մուտք գործել: 
                '''
            success(request, html_message)
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
                html_message = '''<strong>Նշված օգտագործողի հավատարմագրերը սխալ են:</strong> 
                    <br>Փոխեք օգտվողի հավատարմագրերը ապա փորձեք կրկին մուտք գործել 
                    '''
                warning(request, html_message)
    return render(request, 'customauth/login.html')

@login_required
def client_edit(request):
    model = ClientUserModel
    form = ClientCreationForm()
    return render(request, 'customauth/client_edit.html', {'form': form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        html_message = f'''<strong>Դուք դուրս եք եկել:</strong> 
            <br>Կրկին փորձեք <a href="{reverse('login')}" class="alert-link">մուտք գործել </a>
            '''
        info(request, html_message)
    return redirect('index')
