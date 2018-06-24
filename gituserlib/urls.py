from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from gituserlib import views

urlpatterns = [
    url(r'^users$', views.UserSearch.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
