from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Topics

# Create your views here.


def index(request):
    all_topics = Topics.objects.all()
    context = {'all_topics': all_topics}
    return render(request, 'file/index.html' ,context)
    
def detail(request, topic_id):
    try:
        topic = Topics.objects.get(pk=topic_id)
    except Topics.DoesNotExist:
        raise Http404("Topic doesnt exist")
    return render(request, 'file/detail.html', {'topic': topic})

def arrays(request):
    return render(request, 'file/arrays.html')

def queues():
    return render(request, 'file/queues.html')

def stacks():
    return render(request, 'file/stacks.html')
