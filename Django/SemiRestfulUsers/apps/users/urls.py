from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.users),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d+)$', views.show),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^(?P<id>\d+)/destroy$', views.destroy),
]