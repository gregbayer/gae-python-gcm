################################################################################
# urls.py
# Greg Bayer <greg@gbayer.com>.
################################################################################

import os, logging
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # All urls from gae_python_gcm.urls are mapped to /gae_python_gcm/*
    (r'^gae_python_gcm/', include('gae_python_gcm.urls')),   
)

