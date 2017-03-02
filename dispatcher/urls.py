from django.conf.urls import url
from dispatcher import views

urlpatterns = [
    url(r'^$', views.load_main, name='main'),
    url(r'^sort-(?P<param>[А-Я])/$', views.sort, name='sort'),
    url(r'^lab-requests/$', views.lab_request, name='lab_req'),
    url(r'^lab-requests/sort-(?P<param>[_a-z]+)/$', views.sort_lab_request, name='sort_lab_req'),
    url(r'^med-requests/$', views.med_request, name='med_req'),
    url(r'^med-requests/sort-(?P<param>[_a-z]+)/$', views.sort_med_request, name='sort_med_req'),

]