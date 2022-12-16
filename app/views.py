from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from django.db.models import Q
from app.models import *
def display_topics(request):
    LTO=Topic.objects.all()
    d={"LTO":LTO}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(topic_name='circket')
    LWO=Webpage.objects.filter(topic_name='Cricket')   
    LWO=Webpage.objects.exclude(topic_name='Cricket')
    LWO=Webpage.objects.all()[2:5:]
    LWO=Webpage.objects.all().order_by('name')
    #LWO=Webpage.objects.filter(topic_name='Cricket').order_by('-name')
    #LWO=Webpage.objects.all().order_by(Length('name'))
    #LWO=Webpage.objects.all().order_by(Length('name').desc())
    #LWO=Webpage.objects.filter(name__startswith='m')
    #LWO=Webpage.objects.filter(name__endswith='a')
    #LWO=Webpage.objects.filter(name__contains='O')
    #LWO=Webpage.objects.filter(name__in=('ronaldo','viratkohli'))
    #LWO=Webpage.objects.filter(name__regex='^k\w{6}')
    #LWO=Webpage.objects.all()
    #LWO=Webpage.objects.filter(Q(topic_name='football') & Q(name__startswith='r'))
    #LWO=Webpage.objects.all()
    #LWO=Webpage.objects.filter(Q(topic_name='Foot Ball') | Q(url__endswith='com'))
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)
def display_access(request):
    LAO=AccessRecords.objects.all()
    LAO=AccessRecords.objects.all()
    #LAO=AccessRecords.objects.filter(date='2022-12-13')    
    #LAO=AccessRecords.objects.filter(date__year='2022')
    #LAO=AccessRecords.objects.filter(date__month='4') 
    #LAO=AccessRecords.objects.filter(date__day='14')    
    #LAO=AccessRecords.objects.filter(date__lte='2021-8-13')
    d={'LAO':LAO}
    return render(request,'display_access.html',d)
