from django import forms
from django.db.models import fields
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# /from posting import models
from . models import Article, Reply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('name', 'body')
        # widgets = {
        #     'post': forms.TextInput(attrs={'class': 'form-control'}),
        #     'body': forms.Textarea(attrs={'class': 'form-control'}),
        # }

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'Description', 'images', 'Post_category', 'slug', 'Editor')