from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200) #we use CharField when we want to store a small amt of text.
    date_added = models.DateTimeField(auto_now_add=True) #"auto_now_add=True": tells django to automatically set the current date and time whenever the user creates a new topic.
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #if the user is deleted all the topics associated with that user will be deleted.

    def __str__(self):
        """Return the String represention of the model."""
        return self.text
    
class Entry(models.Model): #inherits from Model class.
    """Something specific learning about a topic."""
    #foreign key is the reference to the other records in the db. This is a code that connects each entry to a specific topic. 
    #each topic has been assigned a key or an id when its created.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #"on_delete=models.CASCADE" if a topic is deleted, all the entries associated with that topic shoud be deleted.
    text = models.TextField() #for storing entries.
    date_added = models.DateTimeField(auto_now_add=True) #present the entries in the order they were created, and place the timestamp next to it.

    #nested class.
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        if len(self.text) < 50:
            return f"{self.text}"
        else:
            return f"{self.text[:50]}..."  #how much info. will be shown representing each entry.