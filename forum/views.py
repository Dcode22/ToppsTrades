from django.shortcuts import render, redirect
from django.http import request
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def forum(request):
    return render(request, "forum_home.html", {'threads': Thread.objects.all()})


def thread(request, thread_id):
    return render(request, "thread.html", {'thread': Thread.objects.get(id=thread_id)})


@login_required
def addThread(request):
    form = ThreadCreateForm()
    if request.method =="POST":
        form = ThreadCreateForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.profile = request.user.profile
            thread.save()
            messages.success(request, "Thread created successfully!")
            return redirect('thread', thread.id)
        else:
            return render(request, "add_thread.html", {'form': form})
    if request.method == "GET":
        return render(request, "add_thread.html", {'form': form})

def deleteThread(request, thread_id):
    Thread.objects.filter(id=thread_id).delete()
    messages.success(request, "Thread deleted successfully")
    return redirect('forum')

@login_required
def addPost(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    form = PostCreateForm()
    if request.method =="POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.profile = request.user.profile
            post.save()
            messages.success(request, "Post added successfully!")
            return redirect('thread', thread.id)
        else:
            return render(request, "add_post.html", {'form': form, 'thread': thread})
    if request.method == "GET":
        return render(request, "add_post.html", {'form': form, 'thread': thread})

def deletePost(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    messages.success(request, "Post deleted successfully")
    return redirect('thread', post.thread.id)

@login_required
def addResponse(request, post_id):
    post = Post.objects.get(id=post_id)
    form = ResponseCreateForm()
    if request.method =="POST":
        form = ResponseCreateForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.post = post
            response.profile = request.user.profile
            response.save()
            messages.success(request, "Response added successfully!")
            return redirect('thread', post.thread.id)
        else:
            return render(request, "add_response.html", {'form': form, 'post': post})
    if request.method == "GET":
        return render(request, "add_response.html", {'form': form, 'post': post})

# def deleteResponse(request, response_id):
#     respnse = Response.objects.get(id=response_id)
#     post.delete()
#     messages.success(request, "Response deleted successfully")
#     return redirect('thread', post.thread.id)

