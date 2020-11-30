from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def  index(request):
	return HttpResponse("Hello World")

def  diff(request):
	return HttpResponse("teda akkad")

def  show_a(request):
	return HttpResponse("a")


def page(request):
	my_dict = {'insert_here':'Hello everyone. I am outcome of dynamic variable in HTML.'}
	return render(request,'first_app/index.html',context=my_dict)

def help_func(request):
	return render(request,'help.html')