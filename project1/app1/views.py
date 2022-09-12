from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

@login_required(login_url='signin_url')
def addOrder(request):
    form = OrderForm()
    template_name = 'app1/add.html'
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='signin_url')
def showOrder(request):
    data = Order.objects.all()
    template_name = 'app1/show.html'
    context = {'data': data}
    return render(request, template_name, context)


def updateOrder(request, pk):
    upd = Order.objects.get(id=pk)
    form = OrderForm(instance=upd)
    template_name = 'app1/add.html'
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=upd)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def deleteOrder(request, pk):
    dlt = Order.objects.get(pk=pk)
    template_name = 'app1/confirm.html'
    if request.method == 'POST':
        dlt.delete()
        return redirect('show_url')
    context = {'dlt': dlt}
    return render(request, template_name, context)


@login_required(login_url='signin_url')
def index(request):
    template_name = 'app1/index.html'
    orders = Order.objects.all()  # fetching all post objects from database
    p = Paginator(orders, 1)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, template_name, context)
