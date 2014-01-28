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

