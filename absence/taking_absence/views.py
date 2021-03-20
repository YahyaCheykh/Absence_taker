from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserForm
# Create your views here.


def welcome_page(request):
    return render(request, "taking_absence/landing_page.html")


def create_school(request):
    return render(request, "taking_absence/create_school_page.html", {"form": UserForm})


def create_school_logic(request):
    if request.method == 'POST':
        user_name = request.POST['name']
        user_email = request.POST['email']
        user_password = request.POST['password']
    return HttpResponse("Create school by "+user_name)


def log_in(request):

    if request.method == 'POST':
        user_email = request.POST['email']
        user_password = request.POST['password']
        user = User.objects.create_user(user_email, user_password)
        user.save()
    return render(request, "taking_absence/login_page.html", {"form": UserForm})
