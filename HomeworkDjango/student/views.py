from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def home_page(request):
    return HttpResponse("Hello World!")


def general_page(request):
    return HttpResponse('This is not the page you are looking for(try "/home" page)')


def bonus_page(request):
    return HttpResponse("Hey, what are you looking here")


def get_email_verification(request):
    return render(request, "email_verification.html")


def get_reset_password(request):
    return render(request, "reset_password.html")


def welcome_page(request):
    return render(request, "welcome_email.html")
