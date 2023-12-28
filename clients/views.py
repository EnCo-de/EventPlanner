from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
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

@login_required 
def discard_order(request, pk):
    order = get_object_or_404(Order, client=request.user, pk=pk, pending=True)
    if request.method=='POST':
        print(request.POST)
        order_pk = int(request.POST.get('discard'))
        if request.POST.get('confirmation', False) and order_pk == pk == order.pk:
            order.pending = False
            order.save()
        return redirect('dashboard')
    context = {
        'order': order, 
        }
    return render(request, 'clients/discard_order.html', context=context)

def success(request):
    return HttpResponse("Submission success, event details ")