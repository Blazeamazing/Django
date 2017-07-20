from django.conf.urls import url
from . import views

urlpatterns = [
    # go to my views file and go to my index method
    url(r'^$', views.index)
]
