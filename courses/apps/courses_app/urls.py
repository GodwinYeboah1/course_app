from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.main),
    url(r'^addCourse$',views.newCourse),
    url(r'^course/destory/(?P<id>\d+)$',views.remove),
    url(r'^delete/(?P<id>\d+)$',views.destory),
]
