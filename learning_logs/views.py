from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    """The homepage for learning_logs."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics."""
    #When a user is logged in, the request object has a request.user attribute set, which contains information about the user
    topics = Topic.objects.filter(owner = request.user).order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all it's entries."""
    topic = Topic.objects.get(id = topic_id)
    #Make sure the topic belongs to the current user.
    check_topic_owner(request, topic)
    """if topic.owner != request.user:
        raise Http404"""
    
    entries = topic.entry_set.order_by('-date_added') #-date_added: the minus sign sorts the result in reverse order, recently added first.
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = TopicForm()  #we included no arguments when instantiating TopicForm, Django creates a blank form that the user can fill out.
    else:
        #POST data submitted; process data.
        form = TopicForm(data = request.POST) # pass it the data entered by the user, which is assigned to request.POST.
        if form.is_valid(): #The is_valid() method checks that all required fields have been filled in (all fields in a form are required by default) and that the data entered matches the field types expected
            new_topic = form.save(commit=False) #false because we have to modify the new topic before saving it to the database.
            new_topic.owner = request.user #set owner att to the current user.
            new_topic.save()
            return redirect('learning_logs:topics') #we'll redirect the user back to the topics page after they submit their topic.
        
    #Display a blank or invalid form.
    context =  {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a perticular topic."""
    topic = Topic.objects.get(id = topic_id)
    check_topic_owner(request, topic)

    if request.method != 'POST':
        #No data submitted, create a blank form.
        form = EntryForm()
    else:
        #POST data submitted; process the data.
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)
        
    #display a blank or invalid form.
    context  = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)
    """if topic.owner != request.user:
        raise Http404"""

    if request.method != 'POST':
        #Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry) #this arg tells djando to prefill the info from the existing entry object.
    else:
        #POST data submitted ; process data.
        form = EntryForm(instance=entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404