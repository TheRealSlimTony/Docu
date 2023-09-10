from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

# Create your views here.


def home(request):
    return render(request, "home_chat.html")
