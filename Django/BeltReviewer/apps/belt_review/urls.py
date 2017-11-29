from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.users),
    url(r'^register$', views.create),
    url(r'^login$', views.login),
    url(r'^user/(?P<id>\d+)$', views.show_user),
    url(r'^books$', views.home),
    url(r'^logout$', views.logout),
    url(r'^books/add$', views.add),
    url(r'^books/create$', views.book_create),
    url(r'^books/(?P<id>\d+)$', views.show),
    url(r'^books/(?P<id>\d+)/create$', views.review_create),
    url(r'^delete/(?P<id>\d+)$', views.review_delete),
]