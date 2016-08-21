from __future__ import absolute_import

import os
from datetime import timedelta
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'summer.settings')

from django.conf import settings  # noqa

app = Celery('summer',
            broker='amqp://',
            # backend='amqp://',
            )

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_RESULT_BACKEND = 'rpc://',
    CELERY_RESULT_PERSISTENT = False,
    CELERYBEAT_SCHEDULE = {
        #'add-every-2-seconds':{
        #    'task':'ribao.tasks.add',
        #    'schedule':timedelta(seconds=2),
        #    'args':(16,16)
        #    },
        'check-every-2-seconds':{
            'task':'ribao.tasks.check',
            'schedule':timedelta(seconds=2),
            'args':(1,),
            },
        },
    CELERY_TIMEZONE = 'UTC',
)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
