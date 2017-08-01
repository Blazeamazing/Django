from django.conf.urls import url
from . import views

urlpatterns = [
# here are my routes that render pages
#the new success page route is placed here 
    url(r'^$', views.index, name='success'),
    url(r'^create$', views.create, name='create-secret'),
    url(r'^like/(?P<id>\d+)$', views.like, name='like-secret'),
    url(r'^unlike/(?P<id>\d+)$', views.unlike, name='unlike-secret'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete-secret'),
    
    #url(r'^', views.index, name='default'),
]

#Named Route Notes:
#if I want to use named routes they look like this: name='register'
#   url(r'^register$', views.register, name='register'),
#so now if I want to use this in my html I am going to use a url helper, which looks like this:
#   <form action="{% url 'register' %}"....