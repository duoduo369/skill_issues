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
