from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.users),
    url(r'^register$', views.create),
    url(r'^login$', views.login),
    url(r'^success/(?P<id>\d+)$', views.show),
    url(r'^logout$', views.logout),
]