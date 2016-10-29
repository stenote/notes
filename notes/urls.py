from django.conf.urls import url

from . import views

app_name = 'notes'

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^add$', views.add, name='add'),
    url(r'^view/(?P<note_id>[0-9]+)/$', views.view, name='view')
]
