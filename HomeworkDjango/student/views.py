from django.http import HttpResponse

# Create your views here.


def home_page(request):
    return HttpResponse("Hello World!")


def general_page(request):
    return HttpResponse('This is not the page you are looking for(try "/home" page)')


def bonus_page(request):
    return HttpResponse("Hey, what are you looking here")
