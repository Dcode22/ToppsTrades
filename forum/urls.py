from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name="forum"),
    path('thread/<int:thread_id>/', views.thread, name="thread"),
    path('addthread/', views.addThread, name="add_thread"),
    path('5675934dfgys/<int:thread_id>/', views.deleteThread, name="delete_thread"),
    path('addpost/<int:thread_id>/', views.addPost, name="add_post"),
    path('598ejeyt63j/<int:post_id>/', views.deletePost, name="delete_post"),
    path('addresponse/<int:post_id>/', views.addResponse, name="add_response"),
    # path('5jsjer4764j/<int:response_id>/', views.deleteResponse, name="delete_response"),
]