import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_two.settings')


import django
django.setup()

import random
from AppTwo.models import AccessRecord, Topic, Webpage
from faker import Faker


fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']



def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    top = add_topic()

    fake_url = fakegen.url()
    fake_date = fakegen.date()
    fake_name = fakegen.company()

    webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]
    acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]



if __name__ == '__main__':
    print("population script!")
    populate(20)
    print("population complete")



#First step: int the view.py we import any model that we will need to use
#Second step: Use the view to query the model for data that we will need.
#Third step: Pass results from the model to the template
#Forth step: Edit the template so that it is ready to accept and display the data from the model.
#Fifth step: Map a url to the view

