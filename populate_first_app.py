import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic,Webpage,AccessRecord
from faker import Faker

fakegen = Faker()
topics =['Search','Social','Marketplace','News','Games']

def add_topics():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t


def populate(N):
    for entry in range(N):
        #get topic for the entry
        top = add_topics()

        #create fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create new webpage for entry

        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create fake access record for that webpage

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':

    print("populating script")
    populate(10)
    print("populating complete")

