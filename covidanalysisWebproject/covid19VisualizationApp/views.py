import json

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from analysis.food import Restaurant
from analysis.preprocess import preprocess


def index(request):
    context ={
        's_section' :'gamgi.html',
        'c_section' :'openingclosing.html',
    }
    return render(request, 'index.html',context);

def gamgi(request):
    return render(request, 'gamgi.html');
def gamgis(request):
    data = preprocess().gamgi();
    return HttpResponse(json.dumps(data), content_type='applicaiton/json');
def gamgi_new(request):
    return render(request, 'gamgi_new.html');
def gamgi_news(request):
    data = preprocess().gamgi_new();
    return HttpResponse(json.dumps(data), content_type='applicaiton/json');
def chunsik(request):
    return render(request, 'chunsik.html');
def chunsiks(request):
    data = preprocess().chunsik();
    return HttpResponse(json.dumps(data), content_type='applicaiton/json');
def openingclosings(request):
	data = Restaurant().OpeningClosing()
	return HttpResponse(json.dumps(data), content_type='application/json');