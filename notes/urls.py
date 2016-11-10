from django.conf.urls import url

from . import views

app_name = 'notes'

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^add$', views.add, name='add'),
    url(r'^edit/(?P<note_ref>[0-9a-z-]+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<note_ref>[0-9a-z-]+)/$', views.delete, name='delete'),
    url(r'^view/(?P<note_ref>[0-9a-z-]+)/$', views.view, name='view')
]
