from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^blogs$', views.blogs),
#we need to have a , because it is a list
#we wanna go to comments and make a ()captured group().that's what the ()are for.
#(give this thing an i.e. name = ?P<id>\d+) \d+ = any number of digits
    url(r'^comments/(?P<id>\d)$', views.comments)
]