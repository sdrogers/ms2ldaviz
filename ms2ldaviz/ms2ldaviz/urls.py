from django.conf.urls import patterns, include, url
from django.contrib import admin
import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^people/', views.people, name='people'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^basicviz/', include('basicviz.urls')),
    url(r'^annotation/', include('annotation.urls')),
    url(r'^massbank/', include('massbank.urls')),
    url(r'^options/', include('options.urls')),
    url(r'^registration/', include('registration.urls')),
    url(r'^uploads/', include('uploads.urls')),
]