from django.shortcuts import render
from .models import *
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django import forms
from django.shortcuts import redirect

def index(request):
    discs = Disc.objects.all()
    request.user.cart_set.get_or_create(user=request.user, active=True)
    return render(request, 'sklepmuzyczny/discs_list.html', {'discs': discs})

def detail(request, disc_id):
	disc = Disc.objects.get(pk=disc_id)
	return render(request, 'sklepmuzyczny/disc_show.html', {'disc': disc})

def cart_detail(request):
    cart = request.user.cart_set.get_or_create(user=request.user, active=True)[0]
    return render(request, 'sklepmuzyczny/cart_show.html', {'cart': cart, 'cart_entries': cart.cartentry_set.all()})

def create_order(request):
    if request.method == 'GET':
        cart = request.user.cart_set.last()
        return render(request, 'sklepmuzyczny/create_order.html', {'cart': cart, 'cart_entries': cart.cartentry_set.all()})
    elif request.method == 'POST':
        cart = request.user.cart_set.last()
        form = OrderForm(request.POST)
        if form.is_valid():
            if cart.create_order(request.POST):
                messages.success(request, 'Zamowienie zostalo zlozone!')
                return redirect('index')
            else:
                messages.warning(request, 'Za malo plyt w magazynie.')
                return redirect('create-order')
     
        else:
            messages.warning(request, 'Blad w formularzu.')
            return redirect('create-order')

def remove_entry(request, entry_id):
    CartEntry.objects.get(pk=entry_id).delete()
    cart = request.user.cart_set.last()
    messages.success(request, 'Plyta usunieta z koszyka.')
    return render(request, 'sklepmuzyczny/cart_show.html', {'cart': cart, 'cart_entries': cart.cartentry_set.all()})

def add_to_cart(request, disc_id):
    if request.method == 'POST':
        disc = Disc.objects.get(pk=disc_id)
        if disc.available_count < 1:
            messages.error(request, 'Brak plyty w magazynie.')
            return render(request, 'sklepmuzyczny/disc_show.html', {'disc': disc})
        else:
            cart = Cart.objects.get_or_create(user=request.user, active=True)[0]
            entry = cart.cartentry_set.get_or_create(disc=disc, defaults={"count": 0})
            entry[0].count += 1
            entry[0].save() 
            cart.sum_price += disc.price
            cart.save()
            messages.success(request, 'Plyta dodana do koszyka.')
            return redirect('cart-detail')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })
class OrderForm(forms.Form):
    imie = forms.CharField(label='Imie', max_length=100)
    nazwisko = forms.CharField(label='Nazwisko', max_length=100)
    ulica = forms.CharField(label='Ulica', max_length=100)
    miasto = forms.CharField(label='Miasto', max_length=100)
    kodpocztowy = forms.CharField(label='Kod pocztowy', max_length=100)
    telefon = forms.CharField(label='Telefon', max_length=100)