from django.urls import path,include
from . import views



urlpatterns=[
    path('',views.home,name='home'),
    path('info/',views.info, name='info'),
    path('subscribe/',views.subscribe,name='subscribe'),
    path('blogposts/', views.blogs, name='blogs'),
    path('blogposts/<str:slug>',views.blogposts, name='blogpost'),
    path('search',views.search,name='search'),
    path('postcomment/',views.postcomment,name='postcomment'),

]
