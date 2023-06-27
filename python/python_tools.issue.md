
切换活内豆瓣源
---


    pip 或者easy_install安装的时候会用国外的源，这个
    东西不时会被墙掉，因此换豆瓣的源

    linux下,修改~/.pip/pip.conf，如果没这文件则创建。
    windows下，修改%HOMEPATH%\pip\pip.ini。
    内容为：
    [global]
    index-url = http://pypi.douban.com/simple

    [install]
    trusted-host=pypi.douban.com

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

virtualenvwrapper
===

sudo pip install virtualenvwrapper

vim ~/.zshrc

    export WORKON_HOME=~/venv
    export VIRTUALENVWRAPPER_PYTHON="/usr/bin/python"
    source /usr/local/bin/virtualenvwrapper.sh

即使之前 ~/venv下建立了对应的virtualenv也没关系,执行下面的命令会补全部分脚本

mkvirtualenv your_venv_name
workon your_venv_name

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

    pip install -e 指定本地路径


PIL 安装
---


    sudo apt-get install libjpeg62 libjpeg62-dev libfreetype6 libfreetype6-dev
    sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/
    sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib/
    sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/

    pip install PIL  --allow-unverified PIL --allow-all-external

pip 在zsh下tab补全
---

pip completion --zsh >> ~/.zprofile
source ~/.zprofile


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

    pylint升级后root用户有时候找不到配置,可以再zshch里面配置alias
    pylint --reports=y --load-plugins pylint_django --disable=E1101,R0904,W0142,W0622,R0201,,E1103,E0712

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

    In [7]: def a():
    ...:     """ python docs goes here """
    ...:     print 'Hi'
    ...:

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


用graphite diamond做监控
===

文章
---
开局先贴两个文章，值得一读

[很赞的blog](http://www.dongwm.com/archives/shi-yong-grafanahe-diamondgou-jian-graphitejian-kong-xi-tong/)

[另一篇介绍graphite的文章](https://kevinmccarthy.org/blog/2013/07/18/10-things-i-learned-deploying-graphite/)

恩怨
---
无论是什么系统，只要上线，就需要运维，这时候很想看一些监控的图表，graphite就很方便的实现了这个需求。

而graphite采用metrics的方式，又有很多其他的tool为他做支持，所监控的不仅仅是机器的一些东西，你可以监控你爬虫的指标，
log的INFO,ERROR频次，nginx网站的访问数量等等，基本是你需要监控什么，很容易的就可以做到。

我从2014年初就在自己的TODOList添加了要玩graphite, 陆续玩了3、4次都失败了，原因都是安装里面某些步骤失败，
这两天终于搞成功了，写个博客记录一下。

[graphite-web](https://github.com/graphite-project/graphite-web) 大部分的安装方式比较简单，都是用pip就可以安装，但是装完后有个坑,
[文档](http://graphite.readthedocs.org/en/latest/install-pip.html)中说使用`pip install graphite-web`,但是pip中的graphite-web太老了，
导致有个cairo,库在ubuntu下打死也装不上，在新的源码中此bug已经修复。我已经提了[issue 1004](https://github.com/graphite-project/graphite-web/issues/1004)

因为用的graphite-index,直接拿了他的几张图来看最终效果

![1](https://raw.github.com/duoduo369/skill_issues/master/imgs/blog/grapite/1.png)
![2](https://raw.github.com/duoduo369/skill_issues/master/imgs/blog/grapite/2.png)
![3](https://raw.github.com/duoduo369/skill_issues/master/imgs/blog/grapite/3.png)


安装
---

我用的是ubuntu, 写在最上面, 并且我假设你了解基本的python语法，用过pip, virtualenv, 没用过也没问题。

文档需要翻墙，因此贴出主要的安装步骤.
最好安装到python的virtualenv中，具体virtualenv的使用可以参考[这里](https://github.com/duoduo369/skill_issues/blob/master/python/python_tools.issue.md)
首先，查看graphite-web的[requirements.txt](https://github.com/graphite-project/graphite-web/blob/master/requirements.txt)，发现需要装一些系统的库, `sudo apt-get install libcairo2-dev`。


    pip install https://github.com/graphite-project/ceres/tarball/master
    pip install whisper
    pip install carbon
    pip install graphite-web


这里我先贴下最终整个系统搭起来后的各个python库版本, 其中logster是一个做日志监控的东西，先`git clone`的本机，然后`pip install -e logster`项目地址即可


    Django==1.4.8
    Twisted==11.1.0
    argparse==1.2.1
    astroid==1.2.1
    cairocffi==0.6
    ceres==0.10.0
    cffi==0.8.6
    configobj==5.0.6
    diamond==3.5.0
    django-tagging==0.3.3
    ipython==2.3.0
    logilab-common==0.62.1
    -e git+https://github.com/etsy/logster.git@4606bfc6b000ec0fd57de639d08cea9629525304#egg=logster-master
    mock==1.0.1
    psutil==2.1.3
    pycparser==2.10
    pylint==1.3.1
    pylint-django==0.5.5
    pylint-plugin-utils==0.2.2
    pyparsing==1.5.7
    python-memcached==1.47
    simplejson==2.1.6
    six==1.8.0
    txAMQP==0.4
    whisper==0.9.12
    wsgiref==0.1.2
    zope.interface==4.1.1

graphite配置与启动
---
根据文档的步骤安装完成后，你会发现`/opt/graphite`下多了一堆东西，将`/opt/graphite/conf`下的*.example,拷贝到去掉example即可

graphite有个服务在2003,2004接口上，你的metrics需要扔到2003上，具体请看文档，现在不用在意这些细节。

metrics就是类似这样的字符串 前缀.前缀.前缀....... blabala, graphite就是根据这种东西画图的,具体请看文档，不用在意这些细节,
因为其他的工具都有封装。

*. 启动carbon, metrics会扔到carbon这个小屋里面


    /opt/graphite/bin/carbon-cache.py start


*. 制造一些metrics, 更改host，或者server, 这里只是做测试，之后会用diamond来采集metrics


    vim /etc/hosts
    添加 127.0.0.1   graphite, 或者其他的东西

    python /opt/graphite/examples/example-client.py
    这些数据存在 /opt/graphite/storage/whisper, 尝试修改example-client.py发点不一样的东西


*. 配置并修改graphite-web的几行代码，启动这个django项目

    cp /opt/graphite/webapp/graphite/local_settings.py{.example,}
    python /opt/graphite/webapp/graphite/manage.py syncdb
    vim /opt/graphite/webapp/graphite/render/glypy.py
    找到import cairo, ....(这就是坑)
    改为import ...
    try:
        import cairo
    except ImportError:
        import cairocffi as cairo

    启动django
    python /opt/graphite/webapp/graphite/manage.py runserver 0.0.0.0:12222(或者其他端口)

4. 浏览器打开http://127.0.0.1:12222, http://127.0.0.1:12222/dashboard这两个页面玩一下,你会看到左侧tree那边有一些数据
这些数据存在`/opt/graphite/storage/whisper`

使用diamond收集metrics
---
给graphite填数据的方式太多了，这里使用diamond,因为豆瓣有一层graphite+diamond的皮, 下面会说

安装
---


    git clone https://github.com/BrightcoveOS/Diamond.git
    cd Diamond
    pip install -e ./


配置并启动
---


    cp /etc/diamond/diamond.conf{.example,}

    vim /etc/diamond/diamond.conf
    找到host, host = graphite(还记得之前配的host么)
    查看下这个文件，你可以cd到collectors_path, handlers_path去看看里面的文件, 因为定制自己的
    diamand collector时需要根据这些东西来写(继承Collector,重写collect方法)，此篇不谈

    service diamond restart


给graphite换层皮, graphite-index
---
graphite的界面实在是不敢恭维，因此很多人为它写UI，这里选择豆瓣的[graphite-index](https://github.com/douban/graph-index)
选择它是因为配置简单

下载
---


    git clone https://github.com/douban/graph-index.git
    cd graph-index


配置
---


    vim config.py
    graphite_url天上你graphite的ip已经端口
    graphite_url = 'http://127.0.0.1:12222'


更新metrics
---


    ./update-metrics.py
    crontab -e
    */5 * * * * python 绝对路径到/update-metrics.py
    ./graph-index.py



使用logster做日志监控
---
日志监控还是需要的，出了nginx的访问日志之外，对于application的异常等等可能也需要监控，这时候使用[logster](https://github.com/duoduo369/logster),就非常方便了，因为他内置了像graphite发metrics的方法，so easy, 这里给了一个我fork的地址，因为我是一个pythoner，logster默认
的parser有apache等等，但是没有python的，我写了一个，提了一个patch.

安装:

    git clone git@github.com:duoduo369/logster.git
    cd logster
    pip install -e ./

用法:
    logster  --output=graphite --graphite-host=graphite的ip已经端口 你的parser 日志绝对路径
    logster  --output=graphite --graphite-host=127.0.0.1:2003 PythonLogster /var/log/adx/adxsterr.log

如果你需要自己定制parser,参照`logster/logster/parsers`下的东西写一个就好。

因为logster自带向graphite发metrics,无须向diamond集成(写Collector),只要起一个定时任务即可。



Finally
---

当然，如果你熟悉django，可以把graphite, graphite-index人给gunicorn和supervisor,这不是重点，需要的可以参考我github上的[demo](https://github.com/duoduo369/django_supervisor_gunicorn_demo).

至于定制你的diamond Collector,监控你想监控的东西，请自己翻阅文档 (继承Collector,重写collect方法),将写好的Collector放在collectors_path下.

为项目添加LICENSE
---

    pip install lice
    lice mit > LICENSE # 这里我选择MIT的LICENSE

安装pycurl
---

    有的时候不能用requests，而需要用curl，pycurl是python的一层封装
    pycurl安装时如果ssl backend不同会报错

    import pycurl

    ImportError: pycurl: libcurl link-time ssl backend (openssl) is differ
    ent from compile-time ssl backend (gnutls)

    pip uninstall pycurl
    export PYCURL_SSL_LIBRARY=openssl
    pip install pycurl

生成ignore文件
---
[joe](https://github.com/karan/joe)

    joe python


buildout
---

[buildout](https://github.com/buildout/buildout)
另一种管理python环境的方式(virtualenv), 有编译的一些操作，可以生成命令
[文章](https://lxneng.com/posts/192)

以[文档](http://www.buildout.org/en/latest/docs/usecase_singlemod.html)为例

执行完bin/buildout后会有下面的目录

```
├── CHANGES.txt
├── LICENSE.txt
├── Makefile
├── PKG-INFO
├── README.txt
├── TODO.txt
├── bin
├── bootstrap.py
├── buildout.cfg
├── develop-eggs
├── eggs
├── ez_setup.py
├── ez_setup.pyc
├── parts
├── setup.cfg
├── setup.py
└── src
```

buildout.cfg, 可以看到定义的`parts=`,可以定义下面的配置段儿
```
[buildout]
develop = .
parts =
  xprompt
  test

[xprompt]
recipe = zc.recipe.egg:scripts
eggs = xanalogica.tumbler
interpreter = xprompt

[test]
recipe = zc.recipe.testrunner
eggs = xanalogica.tumbler
```

全新项目
```
cd newproject
buildout init
wget -O bootstrap.py https://bootstrap.pypa.io/bootstrap-buildout.py
python bootstrap.py

vim buildout.cfg
将下面的东西加到 [buildout] 段, 可以新建一个versions.cfg来做以前pip时requirements.txt的作用

    show-picked-versions=true
    extends = versions.cfg
    update-versions-file = versions.cfg
    versions = versions

vim versions.cfg
[versions]
ipython = 5.1.0
```

pyenv 管理多个版本的python
---

    brew update
    brew install pyenv

安装3.6.10

    pyenv install 3.6.10




cut video
----

    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
    video_file = "/Users/duoduo3369/Movies/0fda7286-77a4-4d7f-a704-07f1c8a87e9b.mp4"
    output_base_path = "/Users/duoduo3369/Movies/audios"

    # time in seconds
    end1 = 60 * 2

    start2 = 60 * 3 + 52
    end2 = start2 + 60

    ffmpeg_extract_subclip(video_file, 0, end1, targetname='{}/chunk1.mp4'.format(output_base_path))
    ffmpeg_extract_subclip(video_file, start2, end2, targetname='{}/chunk2.mp4'.format(output_base_path))
