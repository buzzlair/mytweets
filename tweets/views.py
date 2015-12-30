from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	if request.method == 'GET':
		return HttpResponse('Finally got this stuff up and running. Damn it!')
	elif request.method == 'POST':
		return HttpResponse('This is post request')