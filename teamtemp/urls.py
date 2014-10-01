from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.conf import settings

from teamtemp.views import submit, register, result, CreateTeamTemperatureView

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^about$', TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^admin/([0-9a-zA-Z]{8})$', login_required(result), name='result'),
    url(r'^admin/$', login_required(CreateTeamTemperatureView.as_view()), name='admin'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/register/$', register, name='register'),
    url(r'^([0-9a-zA-Z]{8})$', submit, name='temp'),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
