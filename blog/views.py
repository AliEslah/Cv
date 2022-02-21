from curses.ascii import HT
from django.http import HttpResponse
from django.shortcuts import render

def post_list(request):
    return HttpResponse("Post List Page")

def categories_list(request):
    return HttpResponse("Categories List Page")

