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
