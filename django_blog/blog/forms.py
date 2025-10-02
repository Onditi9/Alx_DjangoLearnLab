from django import forms
from .models import Post


class PostForm(forms.ModelForm):
class Meta:
model = Post
fields = ['title', 'content']
widgets = {
'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post title'}),
'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Write your post here...'}),
}


def clean_title(self):
title = self.cleaned_data.get('title', '')
if len(title.strip()) == 0:
raise forms.ValidationError('Title cannot be empty.')
return title