from django import forms
from .models import Topics, Discutii

class NewTopicForm(forms.ModelForm):
    reteta = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Topics
        fields = ['subject', 'reteta',]


class NewCommentForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Discutii
        fields = ['message',]