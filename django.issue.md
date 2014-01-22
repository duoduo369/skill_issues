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

