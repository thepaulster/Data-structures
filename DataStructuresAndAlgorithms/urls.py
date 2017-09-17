from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),

        #/DataStructuresAndAlgorithms/12
        url(r'^(?P<topic_id>[0-9]+)/$', views.detail, name='detail'),
    ]
