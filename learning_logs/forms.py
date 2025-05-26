from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        #we specify that that the form should be based on the Topic model.
        model = Topic
        fields = ['text'] #it should only inlude a text field.
        labels = {'text': ''} #the empty string i the labels dictionary tells django to not generate a label for the textfield.
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text' : forms.Textarea(attrs= {'cols': 80})} #A widget is an HTML form element, such as a single-line text box, multiline text area, or dropdown list
        