from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	context = {}
	template = 'loginapp/base.html'
	return render(request, template, context)