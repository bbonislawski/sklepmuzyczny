from django.shortcuts import render
from .models import Disc
from .models import Cart

def index(request):
	discs = Disc.objects.all()
	return render(request, 'sklepmuzyczny/discs_list.html', {'discs': discs})
