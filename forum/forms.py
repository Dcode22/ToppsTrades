from .models import *
from django import forms
from django.forms import ModelForm
from django.http import request

class ThreadCreateForm(ModelForm):
    # profile = forms.IntegerField(initial=request.user.profile.id)
    class Meta:
        model = Thread
        fields = ('title',)

class PostCreateForm(ModelForm):
    # thread = forms.IntegerField(initial=request.thread.id)
    # profile = forms.IntegerField(initial=request.user.profile.id)
    class Meta:
        model = Post
        fields = ('title', 'text',)
    
class ResponseCreateForm(ModelForm):
    # post = forms.IntegerField(initial=request.post.id)
    # profile = forms.IntegerField(initial=request.user.profile.id)
    class Meta: 
        model = Response
        fields = ('text',)