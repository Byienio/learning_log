from django.shortcuts import render
from .models import Topic
# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    name = Topic.objects.order_by('date_added')
    content = {'topics': name}
    return render(request, 'learning_logs/topics.html', content)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    content = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', content)