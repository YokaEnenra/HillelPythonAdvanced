from django.http import HttpResponse, JsonResponse

from student.models import Person


def home_page(request):
    return HttpResponse("Hello World!")


def general_page(request):
    return HttpResponse('This is not the page you are looking for(try "/home" page)')


def bonus_page(request):
    return HttpResponse("Hey, what are you looking here")


def persons_json(request):
    persons = Person.objects.all()
    return JsonResponse({'hey fellows': persons})
