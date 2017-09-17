from django.http import HttpResponse
from django.shortcuts import render
from .models import Topics

# Create your views here.


def index(request):
    all_topics = Topics.objects.all()
    context = {'all_topics': all_topics}
    return render(request, 'file/index.html' ,context)
    
def detail(request, topic_id):
    return HttpResponse("<h2>Other topic pages: "+str(topic_id)+"</h2>")
