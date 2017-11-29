from django.conf.urls import url
import views

urlpatterns=[
	url(r'^$', views.courses),
	url(r'^create$', views.create),
	url(r'^destory/(?P<id>\d+)$', views.confirm),
	url(r'^destory/(?P<id>\d+)/remove$', views.remove),
    url(r'^(?P<id>\d+)/comments$', views.comments),
	url(r'^(?P<id>\d+)/comments/create$', views.create_comments),
]