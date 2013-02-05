# About

gae-python-gcm is a simple implementation of [Google Cloud Messaging](http://developer.android.com/google/gcm/index.html) for [Google App Engine](https://developers.google.com/appengine/docs/python/overview) in Python.

This module is designed to take care of everything you have to think about when working with Android GCM messages on the server:

* Takes advantage of App Engine's task queues to make retries asyncronous
* Uses App Engine's memcache to collect error statistics
* Provides two hook functions, **delete_bad_token** and **update_token**, which can be overridden or configured from a settings files to implement these actions in your environent.
* Example django settings and testing / debug handlers.

# Implementation with / without django

gae-python-gcm can be used with or without [Django](https://www.djangoproject.com). The provided example was taken from a [django-nonrel](https://github.com/django-nonrel/django-nonrel) enviroment and is based on the way we use it at [Pulse](http://www.pulse.me). If you want to use it with App Engine's built-in Django or without Django at all, it should be relatively simple to take the core functionality in /gae-python-gcm/gcm.py and leave the rest. Feel free to contact me if you have any quesitons ([@gregbayer](https://twitter.com/gregbayer)).

# Why not use Google's GCM Server referance implmentation

We prefer to keep everything in Python instead of using the [GCM server referance implmentation](http://developer.android.com/google/gcm/demo.html) in Java.

# Example

```python
from gae_python_gcm.gcm import GCMMessage, GCMConnection

gcm_message = GCMMessage(push_token, android_payload, android_collapse_id)
gcm_conn = GCMConnection()
gcm_conn.notify_device(gcm_message)
```

# Getting started

To add gae-python-gcm to your AppEngine project without Django:

1. git clone git://github.com/gregbayer/gae-python-gcm.git
2. Add entries to your app.yaml and queue.yaml based on included files.
3. Copy the gae-python-gcm directory into your appengine project
4. Make sure you set YOUR-GCM-API-KEY in /gae_python_gcm/gcm.py or in the settings module.


To add gae-python-gcm to your AppEngine project with Django:

1. git clone git://github.com/gregbayer/gae-python-gcm.git
2. Add entries to your app.yaml and queue.yaml based on included files.
3. Copy the gae-python-gcm directory into your appengine project
4. Configure your project as appropriate. You may find the urls.py and settings.py examples in the example_django_files directories useful. 
5. Make sure you set YOUR-GCM-API-KEY in /gae_python_gcm/gcm.py or in the settings module.



