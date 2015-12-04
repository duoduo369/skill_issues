celery && django-celery
===

写在前面
---
在使用celery前，首先要对amqp有一个理解，比如什么是exchange,生产者，消费者，worker,
exchange的类型，queue，等等各种名词要有概念。

链接,部分连接请自备梯子，尤其是几个ppt，确实精彩
---

[django-celery-demo github代码](https://github.com/duoduo369/django_celery_demo)

[django-celery ppt](http://www.slideshare.net/matclayton/django-celery#)

[life-in-a-queue-using-message-queue-with-django ppt](http://www.slideshare.net/tarequeh/life-in-a-queue-using-message-queue-with-django#)

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
这个东西的概念是激活一个摄像头，默认是每隔30秒写入django mysql

python manage.py celerycam
With celerycam running, the Django admin interface is updated as Celery tasks are executed:

CELERY_QUEUES 使用更多的queue（不要只用默认的）
---

    CELERY_ROUTES = {
        'my_taskA': {'queue': 'for_task_A', 'routing_key': 'for_task_A'},
        'my_taskB': {'queue': 'for_task_B', 'routing_key': 'for_task_B'},
    }

注意定义CELERY_ROUTES时可以只在这个dict中定义key,例如下面的my_taskA，它
的queue, routing_key都会默认置为my_taskA

    CELERY_ROUTES = {
        'my_taskA': {},
        'my_taskB': {},
    }

最后再为每个task启动不同的workers,一个队列一个worker(或者几个worker)

    celery worker -E -l INFO -n workerA -Q for_task_A celery worker -E -l INFO -n workerB -Q for_task_B


@task 装饰器
---

`@task(bind=True)`,就会给这个方法添加一个self(指定此task对象)

    示例代码作用讲解:大多数任务并没有使用错误处理，如果任务失败，那就失败了。在一些情况下这很不错，但是作者见到的多数失败任务都是去调用第三方API然后出现了网络错误，或者资源不可用这些错误，而对于这些错误，最简单的方式就是重试一下，也许就是第三方API临时服务或者网络出现问题，没准马上就好了，那么为什么不试着重试一下呢？

    @app.task(bind=True, default_retry_delay=300, max_retries=5)
    def my_task_A():
        try:
            print("doing stuff here...")
        except SomeNetworkException as e:
            print("maybe do some clenup here....")
            self.retry(e)

`@task(queue='队列名字')`,会指定某一个队列来执行,否则使用default队列

    两个任务会在同一个队列(default)中执行

    @app.task()
    def my_taskA(a, b, c):
        print("doing something here...")

    @app.task()
    def my_taskB(x, y):
        print("doing something here...")

`@task(exchange='exchange name'),指定具体的exchange, 因为一个队列中可能有多个exchange,不制定也用默认的

celery beat
---

    如果有定时任务需要启动celery beat

使用flower
---

使用[flower](https://github.com/mher/flower)来监控你celery的情况

Real-time monitor and web admin for Celery distributed task queue.

./manage.py celery flower --port=5555

有的时候需要某个特定的版本
https://github.com/mher/flower/issues/282
flower==0.7.3 tornado==3.2.2

启用rabbitmq的可视化管理页面
---
    rabbitmq-plugins list
    rabbitmq-plugins enable rabbitmq_management
    rabbitmq-plugins enable rabbitmq_management_agent
    rabbitmq-plugins enable rabbitmq_management_visualiser
    rabbitmqctl set_user_tags 你的用户 administrator

浏览器打开`http://ip:15672/visualiser/`,用你的用户名密码登陆
