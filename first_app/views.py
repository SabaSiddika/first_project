from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

# Create your views here.
def index(request):
    #return HttpResponse("<em><b>hello world</b></eb>")
    #my_dict = {'insert_me' : "I am from first_app/index.html" }
    webpage_list = AccessRecord.objects.order_by('date')
    date_dic = {'access_records':webpage_list}
    return render(request,'first_app/index.html' , context = date_dic)
    
