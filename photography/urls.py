
from django.contrib import admin
from django.conf.urls import url
from photography import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.base, name='mainpage'),
    url(r'^wedding/$', views.wedding, name='wedding'),
    url(r'^corporate/$', views.corporate, name='corporate'),
    url(r'^couple/$', views.couple, name='couple'),
    url(r'^baby/$', views.baby, name='baby'),
    url(r'^fashion/$', views.fashion, name='fashion'),
    url(r'^party/$', views.party, name='party'),
]
