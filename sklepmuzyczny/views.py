from django.shortcuts import render
from .models import Disc, Cart, CartEntry
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def index(request):
	discs = Disc.objects.all()
	return render(request, 'sklepmuzyczny/discs_list.html', {'discs': discs})

def detail(request, disc_id):
	disc = Disc.objects.get(pk=disc_id)
	return render(request, 'sklepmuzyczny/disc_show.html', {'disc': disc})

def cart_detail(request):
    cart = request.user.cart_set.last()
    return render(request, 'sklepmuzyczny/cart_show.html', {'cart': cart, 'cart_entries': cart.cartentry_set.all()})

def remove_entry(request, entry_id):
    CartEntry.objects.get(pk=entry_id).delete()
    cart = request.user.cart_set.last()
    messages.success(request, 'Disc removed from cart succesfully.')
    return render(request, 'sklepmuzyczny/cart_show.html', {'cart': cart, 'cart_entries': cart.cartentry_set.all()})

def add_to_cart(request, disc_id):
    if request.method == 'POST':
        disc = Disc.objects.get(pk=disc_id)
        cart = Cart.objects.get_or_create(user=request.user)[0]
        entry = CartEntry.objects.create(disc=disc, cart=cart, count=1)
        messages.success(request, 'Disc added to cart succesfully.')
        return render(request, 'sklepmuzyczny/cart_show.html', {'cart': cart, 'cart_entries': cart.cartentry_set.all()})

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