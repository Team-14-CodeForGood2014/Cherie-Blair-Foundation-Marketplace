from django.conf.urls import url

from searchEngine import views

urlpatterns = [
    url(r'^$', views.results, name='results'),
]
