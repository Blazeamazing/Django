from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='landing'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^create$', views.quotes, name='create'),
    url(r'^quotes$', views.quotes, name='quotes'),
    url(r'^add-quote/(?P<id>\d+)$', views.addQuote, name='add-quote'),
    url(r'^deleteQuote(?P<id>\d+)$', views.deleteQuote, name='deleteQuote'),
    url(r'^remove-Quote/(?P<id>\d+)$', views.removeQuote, name='remove-quote'),
    # need a catch all
    url(r'^', views.index, name='default'),
]