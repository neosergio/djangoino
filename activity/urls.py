from .views import ActivityList, device_interaction
from django.conf.urls import url


urlpatterns = [
    url(r'^list/$', ActivityList.as_view()),
    url(r'^device/(?P<pk>[0-9]+)/$', device_interaction),
]