from django.http import HttpResponse
from django.shortcuts import render


def index_page(request):
    return render(request, 'index_page.html')

def self_intro_page(request):
    return render(request, 'self_intro.html')


