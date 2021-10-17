from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Topic, Webpage, AccessRecord
# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    #my_dict = {'insert_me': "Welcome to the Help Page"}
    date_dict = {'access_records': webpages_list}
    #return render(request, 'index.html', context=my_dict)
    return render(request, 'index.html', context=date_dict)


# Django LAB 1:
#    return HttpResponse("My Second App")