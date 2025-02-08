from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm
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

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    contex = {'form': form}
    return render(request, 'learning_logs/new_topic.html',contex)