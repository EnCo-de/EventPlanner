from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView

from django.http import HttpResponse

from .models import Order, Entertainment
from .forms import OrderForm

# Create your views here.
def index(request):
    return render(request, 'clients/index.html')


@login_required 
def dashboard(request):
    orders = Order.objects.filter(client=request.user, pending=True)
    context = {
        'orders': orders, 
        }
    return render(request, 'clients/dashboard.html', context=context)


@login_required 
def ordering(request):
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.client = request.user
            order.save()
            print('\n\n\t\t',order.real, form.cleaned_data.get('real'))
            print(request.POST)
            form.save_m2m()
            return redirect('dashboard')
    else:
        form = OrderForm()
    context = {
        'form': form, 
        }
    return render(request, 'clients/ordering.html', context=context)


class OrderCreateView(LoginRequiredMixin, CreateView):
    # Submit your requirements for the event
    model = Order
    fields = ['shows', 'category', 'venue', 'date', 'budget_min', 'budget_max', 'participants', 'children', 'corporate', 'company']
    template_name = 'clients/ordering.html'
    success_url = reverse_lazy('dashboard')


def success(request):
    return HttpResponse("Submission success, event details ")