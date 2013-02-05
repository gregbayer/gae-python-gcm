################################################################################
# gae_python_gcm/urls.py
# Greg Bayer <greg@gbayer.com>
################################################################################

from django.conf.urls.defaults import patterns

urlpatterns = patterns('gae_python_gcm.views',
    (r'^send_request', 'send_request_handler'),
    (r'^debug', 'debug_handler'),
    )

