from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),

        #/DataStructuresAndAlgorithms/12
        url(r'^(?P<topic_id>[0-9]+)/$', views.detail, name='detail'),

        #/DataStructuresAndAlgorithms/arrays
        url(r'^arrays/$', views.arrays, name='arrays'),

        #/DataStructuresAndAlgorithms/queues
        url(r'^queues/$', views.arrays, name='queues'),

        #/DataStructuresAndAlgorithms/stacks
        url(r'^stacks/$', views.arrays, name='stacks'),

    ]
