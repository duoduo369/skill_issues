celery && django-celery
===

链接
---
[django-celery ppt](http://www.slideshare.net/matclayton/django-celery#)
[an-introduction-to-celery ppt](http://www.slideshare.net/idangazit/an-introduction-to-celery)
[重要的amqp概念](https://www.rabbitmq.com/tutorials/amqp-concepts.html)
[介绍1](http://docs.dotcloud.com/tutorials/python/django-celery/)
[celerycam](http://blog.endpoint.com/2012/03/debugging-celery-tasks-in-django.html)
[AMQP协议介绍](http://my.oschina.net/scalewing/blog/169471)
[django-celery配置](http://www.dongwm.com/archives/shi-yong-celeryzhi-shen-ru-celerypei-zhi/)
[django-celery supervisor](http://www.dongwm.com/archives/shi-yong-celeryzhi-liao-jie-celery/)
[celery最佳实践](http://my.oschina.net/siddontang/blog/284107)

google关键词
---
###django celery exchange
会显示route相关信息

default exchange
---

The default exchange is a direct exchange with no name (empty string) pre-declared by the broker. It has one special property that makes it very useful for simple applications: every queue that is created is automatically bound to it with a routing key which is the same as the queue name.

For example, when you declare a queue with the name of "search-indexing-online", the AMQP broker will bind it to the default exchange using "search-indexing-online" as the routing key. Therefore, a message published to the default exchange with the routing key "search-indexing-online" will be routed to the queue "search-indexing-online". In other words, the default exchange makes it seem like it is possible to deliver messages directly to queues, even though that is not technically what is happening.


celeryd -E 启动worker
---

[link](http://www.mechanicalgirl.com/post/scheduling-periodic-tasks-celery-233-and-django-14/) `celery: python manage.py celeryd --events --loglevel=INFO -c 5 --settings=settings -B`

Just be sure to add '-B' so that celerybeat starts with celery, and the scheduler will handle things from there.



Running the Workers

With Django-Celery the Celery workers are launched using manage.py from the root of the application, with the command:

`python minestrone/manage.py celeryd -E -l info -c 2`

Here is what each command switch does:

-E activates events, this tells the workers to send notifications of what they are doing (started/finished a task, etc.);
-l info asks the workers to log every messages that have a priority superior or equal to “info”;
-c 2 launches two workers (“c” as in “concurrency”).
We will see how to automatically run this on dotCloud when



celerycam 激活django admin
---
python manage.py celerycam
With celerycam running, the Django admin interface is updated as Celery tasks are executed:
