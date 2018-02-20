from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


# Create your urls here

urlpatterns = [
    url('^index/$',TemplateView.as_view(template_name='index.html')),
    url(r'^$', views.index, name='index'),
    url(r'^send_new', views.send_new, name='send_new'),
]
