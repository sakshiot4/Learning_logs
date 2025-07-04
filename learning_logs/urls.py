"""Defines the url patterns for learning_logs."""
from django.urls import path #needed when mapping urls to view.
from . import views

app_name = 'learning_logs'

#incudes the list of individual pages that can be requested from the learning_log app.
urlpatterns = [
    #home page.
    path('', views.index, name = 'index'),
    #page that shows all topics.
    path('topics/', views.topics, name='topics'),
    #detailed page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #page for adding new topic.
    path('new_topic/', views.new_topic, name = 'new_topic'),
    #page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name= 'new_entry'),
    #page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name= 'edit_entry'),
]