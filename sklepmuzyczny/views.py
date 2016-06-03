from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# def discs_list(request):
# 	return render(request, 'sklepmuzyczny/discs_list.html', {})
# Create your views here.
