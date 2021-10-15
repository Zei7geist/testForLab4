from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    my_dict = {'insert_me': "Welcome to the Help Page"}
    return render(request, 'index.html', context=my_dict)

# Django LAB 1:
#    return HttpResponse("My Second App")