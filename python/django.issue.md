django issue
===

awesome系列
---

https://github.com/rosarior/awesome-django

引入静态文件
---
django 1.6项目新建后static配置不需要更改

[文档](https://docs.djangoproject.com/en/1.6/howto/static-files/)

url.py

    from django.conf.urls import patterns, include, url
    from django.conf import settings
    from django.conf.urls.static import static

    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'tech_dict.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),

        url(r'^admin/', include(admin.site.urls)),
        url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

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

简单的将log重定向到某文件
---

    配一下log https://docs.djangoproject.com/en/1.7/topics/logging/

    需要将标准错误重定向到标准输出 2>$1

    ./manage.py runserver 0.0.0.0:11222 >> /var/log/youlog.log 2>&1 &

django i18n
---
django会从文件中提出`_()`这种需要翻译的东西丢到po文件中，然后翻译后可以讲po编译为mo.
以中文为例

    # 时区为上海
    TIME_ZONE = 'Asia/Shanghai'
    # 默认中文
    LANGUAGE_CODE = 'zh-CN'
    # 语言切换只能从下面的列表选择, 这里是英文和中文
    LANGUAGES = (
        ('en', 'English'),
        ('zh-cn', 'Simplified Chinese'),
    )
    # po, mo文件地址
    LOCALE_PATHS = (
        os.path.join(BASE_DIR, 'locale'),
    )

需要手动在项目根目录下建立locale文件夹

建立po文件,注意源码中一定要有`from django.utils.translation import ugettext as _`的需要翻译的东西，否则会报错

当没有任何po时 `./manage.py makemessages -l zh_CN`,建立中文po

更新已有po `./manage.py makemessages -a`

根据翻译后的po生成`./manage.py compilemessages`

Beautiful Code in Django
---

* Fat Models, Utility Modules, Thin Views, Stupid Templates
* 变量balance_sheet_decrease 而不是bsd或者bal_s_d
* import 按照 1.标准库 2.django库 3.三方库 4.本地app模块的顺序导入

class里面method怎么打装饰器
---
一个正常的装饰器是需要用method_decorator才能打在class上的
from django.utils.decorators import method_decorator


django单测让request过middleware
---

    from django.contrib.auth.models import AnonymousUser
    from django.contrib.sessions.middleware import SessionMiddleware
    from django.test import TestCase, RequestFactory
    from .views import cheese_flavors

    def add_middleware_to_request(request, middleware_class):
        middleware = middleware_class()
        middleware.process_request(request)
        return request

    def add_middleware_to_response(request, middleware_class):
        middleware = middleware_class()
        middleware.process_request(request)
        return request


    class SavoryIceCreamTest(TestCase):

        def setUp(self):
            # Every test needs access to the request factory.
            self.factory = RequestFactory()

        def test_cheese_flavors(self):
            request = self.factory.get('/cheesy/broccoli/')
            request.user = AnonymousUser()
            # Annotate the request object with a session
            request = add_middleware_to_request(request, SessionMiddleware)
            request.session.save()
            # process and test the request
            response = cheese_flavors(request)
            self.assertContains(response, "bleah!")


django1.8的bug
---

django 1.8.8有个严重的bug
当你第一次migrate的时候，由于没有user表其他有user外键的表先跑会抛异常

    django.db.utils.IntegrityError: (1215, 'Cannot add foreign key constraint')

需要先跑auth的migrate

  python manage.py migrate auth
  python manage.py migrate

更新上面说的话，其实并不是，需要全部先makemigration一次就好了


继承抽象类后修改某个字段
----

    class BaseMessage(models.Model):
        is_public = models.BooleanField(default=False)
        # some more fields...

        class Meta:
            abstract = True

    class Message(BaseMessage):
        # some fields...
    Message._meta.get_field('is_public').default = True


south migrate的默认值问题
----

当你添加一列并且设置default的时候，如果多台机器上线会出问题，因为django
处理default是用python的方式做的，而不是数据表上有这个default

例如, 下面是south migration一个脚本的一行，他是添加了floor_number并且设置默认值为0

      db.add_column('bbs_comment', 'floor_number',
                    self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                    keep_default=False)

执行后发现mysql的列里面floor_number并没有默认值，多台机器上线时未上线机器用到这张表存记录的
时候会报错。

解决方案 `keep_default=True`,会给数据库设置默认值

django date字段 跟python字段相减
---
TypeError: can't subtract offset-naive and offset-aware datetimes


django 请求多个同名 key 的问题
----

QueryDict 由于是用 MultiValueDict 实现的，当同名 param 传递多次时，使用 getlist 可以取出来
```
    >>> d = MultiValueDict({'name': ['Adrian', 'Simon'], 'position': ['Developer']})
    >>> d['name']
    'Simon'
    >>> d.getlist('name')
    ['Adrian', 'Simon']
    >>> d.getlist('doesnotexist')
    []
```

手写 django migration
---

[文档](https://docs.djangoproject.com/en/1.11/ref/migration-operations/#runpython)

[demo](https://github.com/edx/edx-val/blob/master/edxval/migrations/0002_data__default_profiles.py)


    # -*- coding: utf-8 -*-
    from __future__ import unicode_literals

    from django.db import migrations, models


    DEFAULT_PROFILES = [
        "desktop_mp4",
        "desktop_webm",
        "mobile_high",
        "mobile_low",
        "youtube",
    ]


    def create_default_profiles(apps, schema_editor):
        """ Add default profiles """
        Profile = apps.get_model("edxval", "Profile")
        for profile in DEFAULT_PROFILES:
            Profile.objects.get_or_create(profile_name=profile)


    def delete_default_profiles(apps, schema_editor):
        """ Remove default profiles """
        Profile = apps.get_model("edxval", "Profile")
        Profile.objects.filter(profile_name__in=DEFAULT_PROFILES).delete()


    class Migration(migrations.Migration):

        dependencies = [
            ('edxval', '0001_initial'),
        ]

        operations = [
            migrations.RunPython(create_default_profiles, delete_default_profiles),
        ]

django orm使用 in 的顺序排序 order by with in
---

https://chriskief.com/2015/01/13/sort-django-query-order-by-using-values-within-in/

    In [46]: ids=[3,2,1,5]

    In [47]: users =User.objects.filter(id__in=ids).extra(
        ...:     select={'manual': 'FIELD(id,%s)' % ','.join(map(str, ids))},
        ...:     order_by=['manual']
    ...: )

单表支持emoji
---
utf8mb4

https://exana.io/community/a-helping-hand/2016/08/23/django-utf8mb4-selected-columns.html
```
class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20180508_2235'),
    ]   

    operations = [ 
        migrations.RunSQL(
                sql = [ 
                    'ALTER TABLE message_messagecontent MODIFY content longtext CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci'
                ],  
            reverse_sql=['ALTER TABLE message_messagecontent MODIFY content longtext']
        )
    ]
```
