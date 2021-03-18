from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def welcome_page(request):
    return render(request, "taking_absence/landing_page.html")

