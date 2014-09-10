
切换活内豆瓣源
---
    pip 或者easy_install安装的时候会用国外的源，这个
    东西不时会被墙掉，因此换豆瓣的源

    linux下,修改~/.pip/pip.conf，如果没这文件则创建。
    windows下，修改%HOMEPATH%\pip\pip.ini。
    内容为：
    [global]
    index-url = http://pypi.douban.com/simple

virtualenv
---
    http://www.virtualenv.org
    类似虚拟机的一种环境，控制你python安装的好东西

    保持你python的版本干净，例如一次开发,项目一django
    使用1.5.0版本，项目二版本是用1.6，你同时负责这两个
    项目的时候会非常痛苦，传统的方式可以说是无解的(莫非
    装了卸卸了装？) 而用virtualenv可以完美解决这个问题，
    虚拟环境1用1.5.0,虚拟环境二使用1.6，需要用那个环境
    直接切过去就ok～

    安装
    sudo pip install virtualenv

    新建总的虚拟环境文件夹
    mkdir ~/python_env
    sudo ln -s ~/python_env /opt

    cd到你python虚拟环境的文件夹下
    cd /opt/python_env

    virtualenv ENV # 新建名字叫ENV的虚拟环境
    virtualenv django1.6.1  # 新建名字叫django1.6.1的虚拟环境

    例如我想用django这个环境
    source django1.6.1/bin/activate

    结束使用
    deactivate

    参考自
    http://docs.python-guide.org/en/latest/dev/virtualenvs/

pip安装
---
    requirements.txt里面有一行一行的需要的代码
    # 例如 
    Django==1.6
    MySQL-python==1.2.4
    South==0.8.2
    djangorestframework==2.3.9
    ipython==1.1.0

    pip install -r requirements.txt

    pip freeze > ~/requirements.txt # 导出已将安装的requirements


PIL 安装
---

    sudo apt-get install libjpeg62 libjpeg62-dev libfreetype6 libfreetype6-dev
    sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/
    sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib/
    sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/

    pip install PIL  --allow-unverified PIL --allow-all-external


用交互模式执行脚本
---
python -i XXX.py
ipython -i XXX.py
或者开启ipython后 %run 脚本路径

pylint代码评估
---
    pylint 比pep8要求更高的python代码分析

    pip install pylint
    pip install pylint-django # django插件
    pylint --load-plugins pylint_django tasks.py # 启用django插件
    # 配置法启用pylint_django
    pylint --generate-rcfile > ~/.pylintrc
    vim ~/.pylintrc
    找到 load-plugins= 填上插件名字pylint_django

    disable=E1101,R0904,W0142,W0622,R0201,E1103,E0712


    pylint task.py # 此时启用了插件

    ps: 如果你的~/为root，需要将~/.pylintrc cp到/etc/pylintrc

ipython
---
    * store 保存变量，下次直接载入，方便调试

    In [1]: l = ['hello',10,'world']
    In [2]: %store l
    In [3]: exit

    (IPython session is closed and started again...)

    ville@badger:~$ ipython
    In [1]: l
    NameError: name 'l' is not defined
    In [2]: %store -r
    In [3]: l
    Out[3]: ['hello', 10, 'world']

    * save file X-Y
    保存X-Y行

    * python/ipython交互模式历史记录搜索
    $cat ~/.inputrc
    ## arrow up
    "\e[A":history-search-backward
    ## arrow down
    "\e[B":history-search-forward

* Inspect variables and functions

IPython:

```python
In [7]: def a():
...:     """ python docs goes here """
...:     print 'Hi'
...:
```

1. `?`, look up the docs
    i.e.
    ``` python
    In [8]: a?
    Type:        function
    String form: <function a at 0x101b7be60>
    File:        /Users/ldong/GDrive/github/icebucket/ui/app/assets/<ipython-input-7-d7491bd3f1a8>
    Definition:  a()
    Docstring:   python docs goes here
    ```

2. `??`, look up the source code
    i.e.
    ``` python
    In [10]: a??
    Type:        function
        String form: <function a at 0x101b7be60>
        File:        /Users/ldong/GDrive/github/icebucket/ui/app/assets/<ipython-input-7-d7491bd3f1a8>
        Definition:  a()
        Source:
        def a():
            """ python docs goes here """
            print 'Hi'
        ```
* Reuse variables

Type `_iline#` to reuse the **input** of that variable.

    i.e.
    ```python
    In [18]: _i7
    Out[18]: u'def a():\n    """ python docs goes here """\n    print \'Hi\'\n'

    In [11]: a = 1

    In [12]: _i11
    Out[12]: u'a = 1'
    ```

fabric(ssh工具)
---

突然发现了一篇好[博客](http://wklken.me/posts/2013/03/25/python-tool-fabric.html)

fabric命令需要在一个module里面,因此在文件夹里需要有__init__.py

fab 命令默认找此模块下的`fabfile.py文件`,如果没有这个文件需要使用
-f 指明脚本路径

    fab_module
      ├── fabfile.py
      ├── fabfile.pyc
      └── __init__.py

fabfile.py

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    def hello():
        print("Hello world!")

可以直接`fab hello`,执行fabfile.py里面的hello方法
如果没有fabfile.py而是有一个hello.py 则`fab hello -f hello.py`

如果有多个参数得话用`,`隔开,可以直接指明参数,例如下面的代码

    def hello(name='name', say='hi'):
        print("{name} say:{say}".format(name=name, say=say))

可以
    fab hello:name=1,say=2
    fab hello:1,2
    fab hello:1,say=2 # 与python的用法一样，kwarg要在arg后面

demo

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    # 本地命令使用local
    # 远程命令使用run
    #
    from fabric.api import *

    env.roledefs = {
        'test_crm_server': ['usename@ip:port',],
    }

    # env.password='xxxxxx' # 如果所有host秘密都相同，用这个参数

    env.passwords = {
        'usename@ip:port': 'password',
    }

    COMAND = 'ls -l | wc'

    @roles('test_crm_server')
    def test_remote():
        run(COMAND)

    def test_local():
        local(COMAND)

    @roles('test_crm_server')
    def download(remote_path, local_path='~/download'):
        get(remote_path, local_path)

    def do():
        execute(test_local)
        execute(test_remote)

supervisor
---
[supervisor中文博客](http://blog.yangyubo.com/2009/05/14/supervisor-introduce/)
[unix domian socket](http://zh.wikipedia.org/wiki/Unix_domain_socket)

supervisor配置文件,[文档](http://supervisord.org/configuration.html)

    注释用;

    [unix_http_server]
    file=/home/duoduo/supervisor/supervisor.sock   ; (the path to the socket file)

        文档中有这一句

        If the configuration file has no [unix_http_server] section,
        a UNIX domain socket HTTP server will not be started.

    [supervisord]
    定义这个supervisord的pid log等

    [rpcinterface:supervisor](使用supervisorctl需要copy此段)
    supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

    [supervisorctl](想用supervisorctl的话必填)

        注意serverurl应与unix_http_server的file地址对应
        这样使得supervisorctl可以与supervisord通过相同的socket通信
        (unix domain socket, 见上方链接)

    serverurl=unix:///home/duoduo/supervisor/supervisor.sock

    [program:name] 定义一个program，配置是自解释的



###demo(用了python的SimpleHTTPServer)

####文件结构

    ├── demo
    │   ├── stderr.log
    │   └── stdout.log
    ├── supervisord.conf
    └── supervisord.log


####supervisord.conf

    [unix_http_server]
    file=%(here)s/supervisor.sock ; (the path to the socket file)
    chmod=0700                       ; sockef file mode (default 0700)

    [supervisord]
    logfile=%(here)s/supervisord.log ; (main log file;default $CWD/supervisord.log)
    pidfile=%(here)s/supervisord.pid ; (supervisord pidfile;default supervisord.pid)
    childlogdir=/var/log/supervisor            ; ('AUTO' child log dir, default $TEMP)


    [rpcinterface:supervisor]
    supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

    [supervisorctl]
    serverurl=unix://%(here)s/supervisor.sock

    [program:learn_demo]
    command=python -m SimpleHTTPServer 5678
    numprocs=1
    stdout_logfile=%(here)s/demo/stdout.log
    stderr_logfile=%(here)s/demo/stderr.log
    autostart=true
    autorestart=true
    startsecs=5
    priority=999

####用法

在这个目录下运行supervisord,会发现多出几个文件
运行supervisorctl,进入交互模式，输入help可以看到能用的指令

###另一个长一点的配置文件

    ; supervisor config file

    [unix_http_server]
    file=/home/duoduo/supervisor/supervisor.sock   ; (the path to the socket file)
    chmod=0700                       ; sockef file mode (default 0700)

    [supervisord]
    logfile=/home/duoduo/supervisor/supervisord.log ; (main log file;default $CWD/supervisord.log)
    pidfile=/home/duoduo/supervisor/supervisord.pid ; (supervisord pidfile;default supervisord.pid)
    childlogdir=/var/log/supervisor            ; ('AUTO' child log dir, default $TEMP)

    [rpcinterface:supervisor]
    supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

    [supervisorctl]
    serverurl=unix:///home/duoduo/supervisor/supervisor.sock


    [include]
    files = /etc/supervisor/conf.d/*.conf

    [program:api_celerybeat]
    command=python manage.py celerybeat --loglevel=DEBUG
    directory=/home/duoduo/project_api/
    numprocs=1
    stdout_logfile=/home/duoduo/project_log/celery_beat.log
    stderr_logfile=/home/duoduo/project_log/celery_beat.log
    autostart=true
    autorestart=true
    startsecs=5
    priority=999
    environment=PATH="/home/duoduo/project_env/bin/"

    [program:api_celerycam]
    command=python manage.py celerycam -F 30
    directory=/home/duoduo/project_api/
    numprocs=1
    stdout_logfile=/home/duoduo/project_log/celery_cam.log
    stderr_logfile=/home/duoduo/project_log/celery_cam.log
    autostart=true
    autorestart=true
    startsecs=5
    priority=999
    environment=PATH="/home/duoduo/project_env/bin/"

    [program:api_celeryd_publish]
    command=python manage.py celeryd -E --loglevel=INFO -Q publish -c 2
    directory=/home/duoduo/project_api/
    numprocs=1
    stdout_logfile=/home/duoduo/project_log/celery_worker.log
    stderr_logfile=/home/duoduo/project_log/celery_worker.log
    autostart=true
    autorestart=true
    startsecs=5
    priority=999
    environment=PATH="/home/duoduo/project_env/bin/"

    [program:api_celeryd_backend_cleanup]
    command=python manage.py celeryd -E --loglevel=INFO -Q backend_cleanup -c 1
    directory=/home/duoduo/project_api/
    numprocs=1
    stdout_logfile=/home/duoduo/project_log/celery_worker.log
    stderr_logfile=/home/duoduo/project_log/celery_worker.log
    autostart=true
    autorestart=true
    startsecs=5
    priority=999
    environment=PATH="/home/duoduo/project_env/bin/"

蛋疼的lxml安装问题
---

碰到过不止一次了

  sudo apt-get install libxslt1-dev libxslt1.1 libxml2-dev libxml2 libssl-dev

  pip install lxml

watchdog监管文件变化
---

[watchdog](https://github.com/gorakhargosh/watchdog)

edx-platform/scripts/run_watch_data.py 中的例子

    #! /usr/bin/env python

    # This script requires that you have watchdog installed. You can install
    # watchdog via 'pip install watchdog'

    import sys
    import time
    import logging
    import os
    from subprocess import Popen
    from signal import SIGTERM
    from watchdog.observers import Observer
    from watchdog.events import LoggingEventHandler, FileSystemEventHandler

    # To watch more (or more specific) directories, change WATCH_DIRS to include the
    # directories you want to watch. Note that this is recursive. If you want to
    # watch fewer or more extensions, you can change EXTENSIONS. To watch all
    # extensions, add "*" to EXTENSIONS.

    WATCH_DIRS = ["../data", "common/lib/xmodule/xmodule/js", "common/lib/xmodule/xmodule/css"]
    EXTENSIONS = ["*", "xml", "js", "css", "coffee", "scss", "html"]

    WATCH_DIRS = [os.path.abspath(os.path.normpath(dir)) for dir in WATCH_DIRS]

    class DjangoEventHandler(FileSystemEventHandler):

        def __init__(self, process):
            super(DjangoEventHandler, self).__init__()

            self.process = process

        def on_any_event(self, event):
            for extension in EXTENSIONS:
                if event.src_path.endswith(extension) or extension == "*":
                    print "%s changed: restarting server." % event.src_path
                    os.system("touch lms/__init__.py")
                    break

    if __name__ == "__main__":
        event_handler = DjangoEventHandler(Popen(['rake', 'lms']))
        observer = Observer()
        for dir in WATCH_DIRS:
            observer.schedule(event_handler, dir, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

