from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from tsnumber import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

urlpatterns = [
    url('^search/(\d+)/$',views.searchpage,name='searchpage'),
    url('^search/$',views.search,name='search'),
    url('^login/$',views.login,name='login'),
    url('^quit/$',views.quit,name='quit'),
    url('^verify/$',views.verifycode,name='verify'),
    # url('^main/$',views.main,name='main')
]
urlpatterns += staticfiles_urlpatterns()