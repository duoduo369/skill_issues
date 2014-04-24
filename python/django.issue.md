django issue
===

south
----
    1. 将south加入INSTALLED_APPS
    2. ./manage.py syncdb 安装south

    3. 如果对于数据库里面已有的app(myapp)
       ./manage.py convert_to_south myapp
       如果是数据库没有的app(安装south后 startapp 加入setting的)
       ./manage.py schemamigration --initial myapp

       然后运行
       ./manage.py migrate newapp
    4. 修改models后运行
       ./manage.py schemamigration --auto myapp
       ./manage.py migrate newapp

curl测试api
---
    curl -H 'Accept: application/json; indent=4' -u admin:password
    http://127.0.0.1:8000/users/


django加速单元测试
---
    测试时使用内存数据库 sqlite
    在DATABASES参数下面加上如下几行，当单元测试的时候使用内存数据库
    if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
    }

django rest
--- 
    django 是MVT的，rest不需要写template,rest中是mv,MVC
    在django里对应的是MTV

    model定义数据，view处理数据，加了一步就是serializers

    用户url访问 -> 查找路由表urls.py -> 对应的views ->

           models ————> django的model，定义数据库(south)
         /     |
    views      |
      |  \     |
      |   serializers ————> 为了方便的将数据转换为json
      |
      |      —— post, put, get, delete ——> CURD
      |    /
       ————  —— 自定义其他方法处理逻辑,或者在别的py里面添加处理逻辑方法
           \
             —— permission_classes 控制权限

QuerySet
---
    像Entry.Objects.all(),这些操作返回的是一个QuerySet对象，这个对象
    比较特别，并不是执行Objects.all(),或者filter之后就会与数据库交互，
    具体参看官方文档,与数据库交互的情况：

    https://docs.djangoproject.com/en/dev/ref/models/querysets/

    Internally, a QuerySet can be constructed, filtered, sliced, and generally passed around without actually hitting the database. No database activity actually occurs until you do something to evaluate the queryset.

    可以print queryset对象的query属性查看具体sql

    1. list(Entry.Objects.all())
    2. for e in Entry.Objects.all():pass  
    # 便利第一个元素的时候会触发数据库操作
    3. Entry.Objects.all()[2:10] 
    # 这种情况不会返回所有元素，sql中会加上limit的，分页可以利用这一点


Q和F
---

    F class

    from django.db.models import F

    Instances of F() act as a reference to a model field within a query. These references can then be used in query filters to compare the values of two different fields on the same model instance.

    这就是说F是专门取对象中某列值的，例子： 'QuerySet 判断一个model两个字段是否相等'


    Q class

    from django.db.models import Q

    Keyword argument queries – in filter(), etc. – are “AND”ed together. If you need to execute more complex queries (for example, queries with OR statements), you can use Q objects.

    从文档把Q放在Complex lookups with Q objects,下就可以看出，Q是做复杂查询的
    and --> XX.objects.filter(Q(f=1),Q(f=2))  # 肯定木有结果 f == 1 and f == 2
    or --> XX.objects.filter(Q(f=1) | Q(f=2)) # f ==1 | f == 2
    not --> XX.objects.filter(~Q(f=1),Q(f=2))  # f != 1 and f == 2

判断某字段是否为null
---
    _tasks = tasks.exclude(group__isnull=True)

    各种双下滑线对应的各种方法,参看文档 querysets field lookup
    https://docs.djangoproject.com/en/1.6/ref/models/querysets/#field-lookups


QuerySet !=
---
    例如model 有两列 一列叫做user,一列叫做assigned_user,
    需求是取出user!=1的记录,django里面不能使用!=,需要用Q


    from django.db.models import Q
    direct_comment = _tasks.filter(~Q(user=1))

    Q还可以这样,user = 1或者2的元素
    direct_comment = _tasks.filter(Q(user=1) | Q(user=2))

QuerySet 判断一个model两个字段是否相等
---
    from django.db.models import F

    例如model 有两列 一列叫做user,一列叫做assigned_user,
    需求是取出user=assigned_user的记录

    direct_comment = _tasks.filter(user=F('assigned_user'))

django group_by
---
    对某些取到的QuerySet分组还是很常见的

    def group_by(query_set, group_by):
        '''util:django 获取分类列表'''
        assert isinstance(query_set, QuerySet)
        django_groups = query_set.values(group_by).annotate(Count(group_by))
        groups = []
        for dict_ in django_groups:
            groups.append(dict_.get(group_by))
        return groups

    例如:
    assign_to = _tasks.exclude(user=F('assigned_user'))
    groups = group_by(assign_to, 'group')
    取出的是一个列表groups = [1L, 3L, 4L]

django admin使用自己的用户系统
---

两部即可

1. 首先实现自己的User class, 继承AbstractBaseUser, 和BaseUserManager
2. settings中添加 AUTH_USER_MODEL = 'myauth.User'

ps: 可以关注下这个项目 https://github.com/yueyoum/django-siteuser

    myauth模块下的models.py

    # -*- coding: utf-8 -*-
    from django.db import models
    from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

    import model_settings as config

    MAX_LENGTH = config.MAX_LENGTH_100


    class UserManager(BaseUserManager):

        def create_user(self, name, email, password=None):

            if not email:
                raise ValueError('Users must have an email address')

            user = self.model(
                name=name,
                email=UserManager.normalize_email(email),
            )

            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_superuser(self, name, email, password=None):

            user = self.create_user(name, email, password)
            user.is_admin = True
            user.save(using=self._db)
            return user


    class User(AbstractBaseUser):
        '''用户表'''

        name = models.CharField(max_length=MAX_LENGTH, unique=True)
        email = models.EmailField(max_length=MAX_LENGTH, unique=True)
        avatar = models.URLField(blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        is_delete = models.BooleanField(default=False)
        is_active = models.BooleanField(default=True)
        is_admin = models.BooleanField(default=False)
        access_token = models.CharField(max_length=MAX_LENGTH, blank=True)
        refresh_token = models.CharField(max_length=MAX_LENGTH, blank=True)
        expires_in = models.BigIntegerField(max_length=MAX_LENGTH, default=0)

        objects = UserManager()

        USERNAME_FIELD = 'name'
        REQUIRED_FIELDS = ('email',)

        class Meta:
            ordering = ('-created_at',)

        def __unicode__(self):
            return self.name

        def get_full_name(self):
            return self.email

        def get_short_name(self):
            return self.name

        def has_perm(self, perm, obj=None):
            return True

        def has_module_perms(self, app_label):
            return True

        @property
        def is_staff(self):
            return self.is_admin

发送邮件
---
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'duoduodev@gmail.com' # google帐号
    EMAIL_HOST_PASSWORD = '你的密码'

    from django.core.mail import EmailMessage
    email = EmailMessage('主题', '正文', to=['duoduo3369@gmail.com'])
    email.send()

django celery
---
[简单blog](http://simondlr.com/post/24479818721/basic-django-celery-and-rabbitmq-example)

### 安装依赖
ubuntu下直接用包管理器安装 erlang rabbitmq-server

    sudo apt-get install erlang rabbitmq-server

### rabbitmq 配置

    rabbitmqctl  add_vhost  duoduo_host # 添加一个host
    rabbitmqctl  add_user  duoduo duoduo # 添加一个用户，用户名 密码
    rabbitmqctl  set_permissions -p duoduo_host duoduo  '.*'  '.*'  '.*'

### django celery使用

1. python manage.py celeryd # 启动celeryd服务
2. python manage.py celerybeat # 查看心跳

### django celery配置(settings文件下方)

    # ----------------------------  celery ------------
    import djcelery
    djcelery.setup_loader()

    # broker 用的rabbitmq
    #BROKER_URL = 'amqp://用户名:密码@127.0.0.1:5672/host'
    BROKER_URL = 'amqp://duoduo:duoduo@127.0.0.1:5672/duoduo_host'

    # 这是使用了django-celery默认的数据库调度模型,任务执行周期都被存在你指定的orm数据库中
    CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

    CELERYD_CONCURRENCY = 2  # celery worker的并发数 也是命令行-c指定的数目
    CELERYD_PREFETCH_MULTIPLIER = 1  # celery worker 每次去rabbitmq取任务的数量
    CELERYD_MAX_TASKS_PER_CHILD = 100 # 每个worker执行了多少任务就会死掉

    CELERY_RESULT_BACKEND = "amqp" # 官网优化的地方也推荐使用c的librabbitmq
    CELERY_RESULT_SERIALIZER = 'json' # 默认是pickle
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_DEFAULT_QUEUE = 'default' # 默认队列名称
    CELERY_DEFAULT_EXCHANGE = 'default'  # 默认交换
    CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'  # 默认交换类型
    CELERY_DEFAULT_ROUTING_KEY = 'default'  # 默认路由key

    CELERY_IGNORE_RESULT = True
    CELERY_STORE_ERRORS_EVEN_IF_IGNORED = False
    CELERY_AMQP_TASK_RESULT_EXPIRES = 18000

    CELERY_EXPIRES_TIME = 18000 # 过期时间 单位s

    CONN_MAX_AGE = 10

    CELERY_IMPORTS = ('paper_edu',) # celery会在那些模块中找@task
                                    # 需要是INSTALLED_APPS中安装的

    # 队列配置
    keys = list(CELERY_IMPORTS)
    keys.extend(['default', 'backend_cleanup'])
    CELERY_QUEUES = {}
    for key in keys:
        CELERY_QUEUES[key] = {
            'exchange': key,
            'exchange_type': 'direct',
            'routing_key': key,
        }

    class MyRouter(object):

        def route_for_task(self, task, args=None, kwargs=None):

            _mapper = {
                'paper_edu.tasks': {'queue': 'paper_edu'},
                # 自定义各种队列, 格式就是这种
                'celery.backend_cleanup': {'queue': 'backend_cleanup'},
            }

            queue = None
            for key in _mapper:
                if task.startswith(key):
                    queue = _mapper[key]
                    break

            if not queue:
                print 'DEFAULT_TASK_%s' % task

            return queue

    CELERY_ROUTES = (MyRouter(), )

### 具体的模块tasks编写

例如有个模块为paper_edu,新建tasks.py

    from celery.task import task

    @task
    def you_task_func():
        ...

### 用django admin管理tasks

在django admin会有Djcelery模块
从上倒下有Crontabs、Intervals、Periodic tasks、Tasks、Workers

#### 首先讲Workers, 点进去会看到有几个worker

只有celeryd && celerybeat都启动了而且还活着的时候才会显示online

#### Crontabs|Intervals

执行周期
    Crontabs 就是类似linux中Crontab的配置方式
    Intervals 比较人性化，每多少小时，天等等

#### Periodic tasks就是日常新建任务，由django管理的一个任务列表

点击右上角的新建,进入新建任务的表单

    name: 任务名字，虽然可以随便起，但是建议和registered的task同名
    Tasks(registered): 这个地方用的就是celery配置和各个模块tasks的任务
    Tasks(custom): 这个字段不要填
    enabled: 是否启用这个任务

    Schedule周期模块
    Interval, 或者Crontab二选一,一般用Interval

    Arguments模块
    tasks任务的方法里面可以传的参数

    Execution这个没有用到过

### 最后的建议

由于celery启用的守护进程比较多,建议使用supervisor来管理
supervisor的使用方式可以见 python_tools.issue.md中查看

