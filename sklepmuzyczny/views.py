from django.shortcuts import render
from .models import Disc
from .models import Cart
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def index(request):
	discs = Disc.objects.all()
	return render(request, 'sklepmuzyczny/discs_list.html', {'discs': discs})

def detail(request, disc_id):
	disc = Disc.objects.get(pk=disc_id)
	return render(request, 'sklepmuzyczny/disc_show.html', {'disc': disc})

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