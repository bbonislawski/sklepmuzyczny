from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^accounts/login/$',  login),
    url(r'^accounts/register/', CreateView.as_view(
        template_name='registration.html',
        form_class=UserCreationForm,
        success_url='/'
    )),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^discs/(?P<disc_id>[0-9]+)/$', views.detail, name='disc-detail'),
]