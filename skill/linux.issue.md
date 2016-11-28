重装linux
===

查看linux版本
---
lsb_release -a

更换源
---
    在系统设置里面找到软件源，随便更换一个国内的源
    ctrl + alt + t之后sudo apt-get update
    这时候应该会提醒安装更新,安装

新立得
---
    在软件中心搜索新立得，安装

chrome
---
    在火狐里面打开google,搜索chrome，安装


zsh
---
    sudo chsh -s $(which zsh)

tmux切屏
---
tmux在ssh的时候会显现出功力，因为某些费时操作会阻塞主ssh shell,用tmux解决这个问题
视频
    http://happycasts.net/episodes/41

第一见事情,改配置,更改为如下配置

###常用指令

主要分为两种，一种是在tmux外，一种是tmux内

概念
    session | window | pane
    一个session可以有多个window，一个window有可以被切为多个pane

tmux外

    tmux new-session  # 新建一个session最好加 -s参数保存一个名字,方便之后attach
    tmux list-sessions # 显示所有的session
    tmux a # 可以加-t session名字  attach具体某个session,此操作是
           # tmux deattach之后运行的

进入tmux后

    prefix的意思是按下某个组合键，tmux默认是Ctrl+b,更改为下面的配置为Ctrl+a
    prefix d的意思是先按下prefix组合键，手指都抬起来，然后按下d
    prefix d deattach当前session，这样会回到tmux外的状态(可以tmux a attach回来)
    prefix c 新建一个window
    prefix 数字 跳转到某个window,下方状态栏会有当前window的标号，名字，是否选中
    prefix p 跳转到前一个window
    prefix n 跳转到下一个window
    prefix , 重命名当前的window,这个在你选择window的时候会有帮助
    prefix s 切屏，左右两块pane
    prefix v 切屏，上下两块pane
    prefix x 关闭当前pane(或者Ctrl+d)
    prefix h | j | k | l 类似vim上下左右切换pane
    prefix < 如果有左右屏的话，在又屏按下这个组合键，则右屏面积变大，左屏变小
    prefix + 如果有上下屏的话，在又屏按下这个组合键，屏下屏面积变大，上屏变小
             同理可以对应prefix > prefix -
             >向右变大 | <向左变大 |+向上变大 | -向下变大
    prefix ? 查看快捷键


修改 ~/.tmux.conf如果发现配置没有生效，说明还有tmux进程开着

    ps aux | grep tmux

将tmux有关进程kill后重启tmux就可以了


~/.tmux.conf

    unbind C-b
    set -g prefix C-a
    setw -g mode-keys vi

    # split window like vim
    # vim's defination of a horizontal/vertical split is revised from tumx's
    bind s split-window -h
    bind v split-window -v
    # move arount panes wiht hjkl, as one would in vim after C-w
    bind h select-pane -L
    bind j select-pane -D
    bind k select-pane -U
    bind l select-pane -R

    # resize panes like vim
    # feel free to change the "1" to however many lines you want to resize by,
    # only one at a time can be slow
    bind < resize-pane -L 10
    bind > resize-pane -R 10
    bind - resize-pane -D 10
    bind + resize-pane -U 10

    # bind : to command-prompt like vim
    # this is the default in tmux already
    bind : command-prompt


ssh登录服务器
---
http://blog.csdn.net/hugeheadhuge/article/details/6719405

在Ubuntu客户端通过ssh登录服务器。假设服务器的IP地址是192.168.0.103，登录的用户名是hyx。

    $ ssh -l hyx 192.168.0.103

接下来会提示输入密码，然后就能成功登录到服务器上了。

ssh [-l login_name] [-p port] [user@]hostname

在linux下一般用scp这个命令来通过ssh传输文件。
---

http://www.cnblogs.com/jiangyao/archive/2011/01/26/1945570.html

1、从服务器上下载文件

    scp username@servername:/path/filename /var/www/local_dir（本地目录）
例如scp root@192.168.0.101:/var/www/test.txt  把192.168.0.101上的/var/www/test.txt 的文件下载到/var/www/local_dir（本地目录）

2、上传本地文件到服务器

    scp /path/filename username@servername:/path   
例如scp /var/www/test.php  root@192.168.0.101:/var/www/  把本机/var/www/目录下的test.php文件上传到192.168.0.101这台服务器上的/var/www/目录中

3、从服务器下载整个目录

    scp -r username@servername:/var/www/remote_dir/（远程目录） /var/www/local_dir（本地目录）
例如:scp -r root@192.168.0.101:/var/www/test  /var/www/  

4、上传目录到服务器

    scp  -r local_dir username@servername:remote_dir
例如：scp -r test  root@192.168.0.101:/var/www/   把当前目录下的test目录上传到服务器的/var/www/ 目录


编辑/etc/profile后导致命令找不到的解决方法
---

原因：在设置环境变量时，编辑profile文件没有写正确，导致在命令行下ls等命令不能够识别。

**解决方案：**

    export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
然后vi修改profile文件


vi配置文件
---

随便找了一个

~/.vimrc 

    syntax on
    set nu

    hi Comment ctermfg=DarkCyan

    set backspace=2
    set selection=exclusive
    set selectmode=mouse,key

    filetype on
    filetype plugin on
    filetype indent on

    set fileencodings=utf-8,gbk
    set encoding=euc-cn
    set ambiwidth=double

    set hlsearch
    set incsearch

    set cindent 
    set tabstop=4
    set shiftwidth=4
    set autoindent
    set showmatch
    set matchtime=1

    set wildmenu
    setlocal noswapfile
    set bufhidden=hide


centos 安装文件
---

用yum安装

    yum install zip
    yum install unzip


iptables 防火墙启动80端口
---

以下仅仅是记录，需要参考/etc/sysconfig/iptables修改

编辑vi /etc/sysconfig/iptables文件，如：

    -A RH-Firewall-1-INPUT -m state –state NEW -m tcp -p tcp –dport 22 -j ACCEPT
    -A RH-Firewall-1-INPUT -m state –state NEW -m tcp -p tcp –dport 80 -j ACCEPT
    -A RH-Firewall-1-INPUT -m state –state NEW -m tcp -p tcp –dport 8080 -j ACCEPT

重启iptalbes服务：

    /etc/init.d/iptables restart 


java安装
---

###下载

首先下载最新的jdk 6 目前是45版本，下载地址不太好找，在oracle官网的download-->java se -->Previous Releases找到下载地址，现在oracle下载必须注册了。
http://www.oracle.com/technetwork/java/javase/downloads/index.html?ssSourceSiteId=ocomen

###移动到服务器
下载完成后首先将本地的文件上传到服务器上 scp命令，有关scp命令的问题见上一个issure。

###解压
上传到服务器之后例如在/opt/files文件夹，首先给jdk-6u45-linux-x64.bin加上执行权限 chmod +x jdk-6u45-linux-x64.bin,然后./jdk-6u45-linux-x64.bin他就会解压到当前目录，如果想移动到别的目录，使用mv命令即可。

###
修改环境变量
vi 编辑/etc/profile文件，在最下面写上这几行代码，注意你真实的路径，然后重新登录服务器，java javac命令都能找到，安装成功，如果出现什么命令找不到的话，请见上一个issure的解决方案。

    JAVA_HOME=/opt/jdk1.6.0_45
    PATH=$JAVA_HOME/bin:$PATH
    CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
    export JAVA_HOME
    export PATH
    export CLASSPATH

###安装结束


tomcat安装
---

下载 apache-tomcat-6.0.37.zip
将文件scp到服务器/opt/files

unzip 命令解压即可,如果没有unzip命令，yum 安装
http://www.cnblogs.com/lucyjiayou/archive/2011/12/25/2301046.html

unzip apache-tomcat-6.0.37.zip -d ../tomcats/

      368  yum install zip
      369  zip
      370  unzip
      371  yum install unzip
      372  unzip
      373  ll
      374  ll ../
      375  ll ../tomcats/
      376  rm ../tomcats/tomcat 
      377  unzip apache-tomcat-6.0.37.zip -d ../tomcats/
      378  cd ..
      379  ll
      380  cd tomcats/
      381  ll
      382  cd apache-tomcat-6.0.37/
      383  ll
      384  cd bin/
      385  ll
      386  chmod +x ./*.sh
      387  ll
      388  ./startup.sh 
      389  ./shutdown.sh 
      390  cd ..
      391  ll
      392  history


weblogic 安装
----
参考文章
https://blogs.oracle.com/brunoborges/entry/how_to_install_weblogic_12c

    1.在oracle上下载wls1211_dev.zip文件
    2.export MW_HOME=/opt/weblogic
    mkdir -p $MW_HOME/mydomain
    3.确保你之前已经安装了jdk和export了JAVA_HOME(参照java安装),但是无论你之前有没有export过JAVA_HOME,在这个bash里面必须export
    一次 export JAVA_HOME=/opt/jdk1.6.0_45
    4.unzip wls1211_dev.zip -d $MW_HOME
    5.cd $MW_HOME
    ./configure.sh
    6. $MW_HOME/wlserver/server/bin/setWLSEnv.sh
    7.cd $MW_HOME/mydomain
    $JAVA_HOME/bin/java $JAVA_OPTIONS -Xms1024m -Xmx1024m
    -XX:MaxPermSize=256m -Dweblogic.management.allowPasswordEcho=true
    weblogic.Server


nginx 安装
---

包含nginx_upstream_check_module 健康度检查模块

参考文章
http://my.oschina.net/wuzhaohui/blog/121822

首先下载nginx_upstream_check_module 和nginx1.4.3 将文件scp到服务器的/opt/files下

unzip到当前目录

    [root@aft files]# ll
    总用量 79416
    -rw-------. 1 root root  7277530 11月  8 10:20 apache-tomcat-6.0.37.zip
    -rwxr-xr-x. 1 root root 72087592 11月  8 09:24 jdk-6u45-linux-x64.bin
    drwxr-xr-x. 8 1001 1001     4096 10月  8 20:07 nginx-1.4.3
    -rw-------. 1 root root   767971 11月  8 11:35 nginx-1.4.3.tar.gz
    drwxr-xr-x. 5 root root     4096  6月 11 21:11 nginx_upstream_check_module-master
    -rw-r--r--. 1 root root   150847 11月  8 11:39 nginx_upstream_check_module-master.zip
    -rw-r--r--. 1 root root        0 11月  8 09:24 test
    -rw-r--r--. 1 root root  1021703 11月  8 11:40 wrk-master.zip


安装依赖

    yum install patch
    yum -y install gcc openssl-devel pcre-devel zlib-devel 
    yum install make


打补丁

    [root@aft nginx-1.4.3]# patch -p1 < /opt/files/nginx_upstream_check_module-master/check_1.2.6+.patch

添加用户和组，注意和后面./configure里面的--user和--group一致

    #/usr/sbin/groupadd -f nginx
    #/usr/sbin/useradd -g nginx nginx

./configure配置文件

    ./configure --prefix=/opt/nginx --sbin-path=/opt/nginx/sbin/nginx --conf-path=/opt/nginx/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx/nginx.pid --lock-path=/var/lock/nginx.lock --user=nginx --group=nginx --with-http_ssl_module --with-http_flv_module --with-http_stub_status_module --with-http_gzip_static_module --http-client-body-temp-path=/var/tmp/nginx/client/ --http-proxy-temp-path=/var/tmp/nginx/proxy/ --http-fastcgi-temp-path=/var/tmp/nginx/fcgi/ --http-uwsgi-temp-path=/var/tmp/nginx/uwsgi --http-scgi-temp-path=/var/tmp/nginx/scgi --with-pcre --add-module=/opt/files/nginx_upstream_check_module-master

vi /etc/init.d/nginx

    #!/bin/bash  
    #  
    #chkconfig: - 85 15   
    #description: Nginx is a World Wide Web server.  
    #processname: nginx   
     
    nginx=/opt/nginx/sbin/nginx # /opt/nginx/sbin/nginx 
    conf=/opt/nginx/etc/nginx/nginx.conf  # /opt/nginx/etc/nginx/nginx.conf  

    # fix pid parent dir bug
    file_path="/var/run/nginx"
    if [ ! -d "$file_path" ] ;then
    mkdir "$file_path"
    fi

    case $1 in 
           start) 
                  echo -n "Starting Nginx"
                  $nginx -c $conf 
                  echo " done" 
           ;; 

           stop) 
                  echo -n "Stopping Nginx"
                  killall -9 nginx 
                  echo " done"
           ;;

           test)
                  $nginx -t -c $conf
           ;;

            reload)
                  echo -n "Reloading Nginx"
                  ps auxww | grep nginx | grep master | awk '{print $2}' | xargs kill -HUP
                  echo " done"
           ;;

            restart) 
                    $0 stop 
                    $0 start 
           ;; 

           show) 
                  ps -aux|grep nginx 
           ;; 

           *) 
                  echo -n "Usage: $0 {start|restart|reload|stop|test|show}"
           ;; 

    esac

加上x权限

    chmod +x /etc/init.d/nginx

 将nginx增加到启动列表中

    chkconfig --add nginx

让nginx随机启动

    chkconfig --level 35 nginx on 

将nginx加入环境变量

    NGINX_HOME=/opt/nginx
    PATH=$NGINX_HOME/sbin:$PATH
    export PATH

nginx常用命令
    
    nginx -t #测试nginx配置文件
    nginx -s reload #重新载入nginx配置文件（不关闭nginx）
    nginx -v #查看nginx版本
    nginx -V #查看nginx 编译参数
    nginx -h # 帮助
    service nginx
    

python安装
---

参考
http://www.cnblogs.com/yuechaotian/archive/2013/06/03/3115482.html

官网下载Python-2.7.5.tgz scp到服务器/opt/files/

解压文件 tar xvf Python-2.7.5.tar.bz2
设定安装目录 ./configure --prefix=/opt/python
安装  make && make install

      575  ll
      576  cd /opt/files/
      577  ll
      578  tar -zxvf Python-2.7.5.tgz 
      579  ll
      580  cd Python-2.7.5
      581  ll
      582  ./install-sh 
      583  mkdir /opt/python
      584  ll /opt/
      585  ./config --prefix=/opt/python
      586  ./configure --prefix=/opt/python
      587  make && make install
      588  python
      589  ll

mysql安装
---

    yum -y install perl
    rpm -ivh MySQL-server-5.5.32-1.e16.x86_64.rpm
    rpm -ivh MySQL-client-5.5.32-1.e16.x86_64.rpm

>查看mysql 服务是否启动

    /etc/rc.d/init.d/mysql status

启动mysql

    service mysql start 
    netstat -nat    显示3306

停止mysql服务

    mv /var/lib/mysql /mydb
    修改/etc/rc.d/init.d/mysql

    basedir=
    datadir=/mydb/mysql

/etc/my.cnf 配置

    cp /usr/share/mysql/my-huge.cnf /etc/my.cnf
    vi /etc/my.cnf 

在client修改socket

    socket= /mydb/mysql/mysql.sock

在mysqld下面分别加上datadir和修改socket

    datadir=/mydb/mysql
    socket= /mydb/mysql/mysql.sock

service start 

The server quit without updating PID file (/mydb/mysql/aft.develop.pid)的问题

删除掉/mydb/mysql/mysql-bin.index

http://blog.rekfan.com/articles/186.html

###允许远程访问
    注释掉#bind-address           = 127.0.0.1

###解决utf-8的问题

show variables like 'character%';

http://stackoverflow.com/questions/3513773/change-mysql-default-character-set-to-utf8-in-my-cnf

在mysql5.5之后 不能在mysqld中使用 `default-character-set=utf8`，否则会启动异常的

vi /etc/my.cnf

    [client]
    default-character-set=utf8

    [mysql]
    default-character-set=utf8


    [mysqld]
    collation-server = utf8_unicode_ci
    init-connect='SET NAMES utf8'
    character-set-server = utf8

密码重置

    use mysql;
    UPDATE user SET Password=PASSWORD('...') WHERE User='root';
    FLUSH PRIVILEGES; 

###/etc/my.cnf

    # Example MySQL config file for very large systems.
    #
    # This is for a large system with memory of 1G-2G where the system runs mainly
    # MySQL.
    #
    # MySQL programs look for option files in a set of
    # locations which depend on the deployment platform.
    # You can copy this option file to one of those
    # locations. For information about these locations, see:
    # http://dev.mysql.com/doc/mysql/en/option-files.html
    #
    # In this file, you can use all long options that a program supports.
    # If you want to know which options a program supports, run the program
    # with the "--help" option.

    # The following options will be passed to all MySQL clients
    [client]
    #password   = your_password
    port        = 3306
    socket      = /mydb/mysql/mysql.sock
    default-character-set=utf8
    #socket     = /var/lib/mysql/mysql.sock

    # Here follows entries for some specific programs

    # The MySQL server
    [mysqld]
    port        = 3306
    datadir=/mydb/mysql
    socket      = /mydb/mysql/mysql.sock
    collation-server = utf8_unicode_ci
    init-connect='SET NAMES utf8'
    character-set-server=utf8
    #socket     = /var/lib/mysql/mysql.sock
    skip-external-locking
    key_buffer_size = 384M
    max_allowed_packet = 1M
    table_open_cache = 512
    sort_buffer_size = 2M
    read_buffer_size = 2M
    read_rnd_buffer_size = 8M
    myisam_sort_buffer_size = 64M
    thread_cache_size = 8
    query_cache_size = 32M
    # Try number of CPU's*2 for thread_concurrency
    thread_concurrency = 8

    # Don't listen on a TCP/IP port at all. This can be a security enhancement,
    # if all processes that need to connect to mysqld run on the same host.
    # All interaction with mysqld must be made via Unix sockets or named pipes.
    # Note that using this option without enabling named pipes on Windows
    # (via the "enable-named-pipe" option) will render mysqld useless!
    # 
    #skip-networking

    # Replication Master Server (default)
    # binary logging is required for replication
    log-bin=mysql-bin

    # required unique id between 1 and 2^32 - 1
    # defaults to 1 if master-host is not set
    # but will not function as a master if omitted
    server-id   = 1

    # Replication Slave (comment out master section to use this)
    #
    # To configure this host as a replication slave, you can choose between
    # two methods :
    #
    # 1) Use the CHANGE MASTER TO command (fully described in our manual) -
    #    the syntax is:
    #
    #    CHANGE MASTER TO MASTER_HOST=<host>, MASTER_PORT=<port>,
    #    MASTER_USER=<user>, MASTER_PASSWORD=<password> ;
    #
    #    where you replace <host>, <user>, <password> by quoted strings and
    #    <port> by the master's port number (3306 by default).
    #
    #    Example:
    #
    #    CHANGE MASTER TO MASTER_HOST='125.564.12.1', MASTER_PORT=3306,
    #    MASTER_USER='joe', MASTER_PASSWORD='secret';
    #
    # OR
    #
    # 2) Set the variables below. However, in case you choose this method, then
    #    start replication for the first time (even unsuccessfully, for example
    #    if you mistyped the password in master-password and the slave fails to
    #    connect), the slave will create a master.info file, and any later
    #    change in this file to the variables' values below will be ignored and
    #    overridden by the content of the master.info file, unless you shutdown
    #    the slave server, delete master.info and restart the slaver server.
    #    For that reason, you may want to leave the lines below untouched
    #    (commented) and instead use CHANGE MASTER TO (see above)
    #
    # required unique id between 2 and 2^32 - 1
    # (and different from the master)
    # defaults to 2 if master-host is set
    # but will not function as a slave if omitted
    #server-id       = 2
    #
    # The replication master for this slave - required
    #master-host     =   <hostname>
    #
    # The username the slave will use for authentication when connecting
    # to the master - required
    #master-user     =   <username>
    #
    # The password the slave will authenticate with when connecting to
    # the master - required
    #master-password =   <password>
    #
    # The port the master is listening on.
    # optional - defaults to 3306
    #master-port     =  <port>
    #
    # binary logging - not required for slaves, but recommended
    #log-bin=mysql-bin
    #
    # binary logging format - mixed recommended 
    #binlog_format=mixed

    # Uncomment the following if you are using InnoDB tables
    #innodb_data_home_dir = /var/lib/mysql
    #innodb_data_file_path = ibdata1:2000M;ibdata2:10M:autoextend
    #innodb_log_group_home_dir = /var/lib/mysql
    # You can set .._buffer_pool_size up to 50 - 80 %
    # of RAM but beware of setting memory usage too high
    #innodb_buffer_pool_size = 384M
    #innodb_additional_mem_pool_size = 20M
    # Set .._log_file_size to 25 % of buffer pool size
    #innodb_log_file_size = 100M
    #innodb_log_buffer_size = 8M
    #innodb_flush_log_at_trx_commit = 1
    #innodb_lock_wait_timeout = 50

    [mysqldump]
    quick
    max_allowed_packet = 16M

    [mysql]
    no-auto-rehash
    default-character-set=utf8
    # Remove the next comment character if you are not familiar with SQL
    #safe-updates

    [myisamchk]
    key_buffer_size = 256M
    sort_buffer_size = 256M
    read_buffer = 2M
    write_buffer = 2M

    [mysqlhotcopy]
    interactive-timeout

###数据库导出导入

    mysqldump --extended-insert=FALSE --complete-insert=TRUE -uroot -p -h
    115.28.17.93(远程数据库ip)  health(远程数据库名字) > ~/health.sql

    dump出特定的表
    mysqldump --extended-insert=FALSE --complete-insert=TRUE -uroot -p -h
    115.28.17.93(远程数据库ip)  health tb1 tb2 tb3 > ~/health.sql

    导出部分数据(where)
    mysqldump -uroot -p  -h 115.28.17.93 social_crm topic_topic_26 --where="type='tweet' order by created_at desc limit 0,10000" > ~/opic_topic_3.sql

    导入
    登录进mysql后用source
    mysql -uroot -p social_crm
    source ~/文件路径


工具增强
====


编辑器vim
----

vim 直接安装janus,节省安装插件时间

https://github.com/carlhuda/janus

常用 ctrl + p
/ + n
gf (例如有个井号注释地址 # /home/duoduo/file.js,在# 后的路径按gf，会打开这个文件)

grep
---

    grep '需要查的词' -ril ./
    r表示递归，i表示忽略大小写，l表示只列出文件名

    grep '需要查的词' -ril $(find '*py') 查找所有py文件

    grep -e 'aws$' -r ./
    -e 表示使用正则

    grep -n显示行号 这个比较有用

grep增强ack
---

安装ack

http://brooky.cc/2012/09/28/ack-for-%E5%B7%A5%E7%A8%8B%E5%B8%AB%E7%94%A8%E7%9A%84-grep/

http://beyondgrep.com/

ps:janus里面已经安装,使用方法:Ack 


搜索近期命令
----

    ctrl + r

    history | grep 想要的命令

shell 复制和粘贴
-----

    在网页或者其他地方用鼠标左键选择要复制的元素，即可复制；
    在shell上点鼠标中键即可粘贴；
    shell上 ctrl + Shift + c 复制
    shell上 ctrl + Shift + v 粘贴

shell增强
---

安装zsh,并且配置zshrc
---
    #color{{{
    autoload colors
    colors
     
    for color in RED GREEN YELLOW BLUE MAGENTA CYAN WHITE; do
    eval _$color='%{$terminfo[bold]$fg[${(L)color}]%}'
    eval $color='%{$fg[${(L)color}]%}'
    (( count = $count + 1 ))
    done
    FINISH="%{$terminfo[sgr0]%}"
    #}}}
     
    #命令提示符
    RPROMPT=$(echo "$RED%D %T$FINISH")
    PROMPT=$(echo "$CYAN%n@$YELLOW%M:$GREEN%/$_YELLOW>$FINISH ")
     
    #PROMPT=$(echo "$BLUE%M$GREEN%/
    #$CYAN%n@$BLUE%M:$GREEN%/$_YELLOW>>>$FINISH ")
    #标题栏、任务栏样式{{{
    case $TERM in (*xterm*|*rxvt*|(dt|k|E)term)
    precmd () { print -Pn "\e]0;%n@%M//%/\a" }
    preexec () { print -Pn "\e]0;%n@%M//%/\ $1\a" }
    ;;
    esac
    #}}}
     
    #编辑器
    export EDITOR=vim
    #输入法
    export XMODIFIERS="@im=ibus"
    export QT_MODULE=ibus
    export GTK_MODULE=ibus
    #关于历史纪录的配置 {{{
    #历史纪录条目数量
    export HISTSIZE=10000
    #注销后保存的历史纪录条目数量
    export SAVEHIST=10000
    #历史纪录文件
    export HISTFILE=~/.zhistory
    #以附加的方式写入历史纪录
    setopt INC_APPEND_HISTORY
    #如果连续输入的命令相同，历史纪录中只保留一个
    setopt HIST_IGNORE_DUPS
    #为历史纪录中的命令添加时间戳
    setopt EXTENDED_HISTORY      
     
    #启用 cd 命令的历史纪录，cd -[TAB]进入历史路径
    setopt AUTO_PUSHD
    #相同的历史路径只保留一个
    setopt PUSHD_IGNORE_DUPS
     
    #在命令前添加空格，不将此命令添加到纪录文件中
    #setopt HIST_IGNORE_SPACE
    #}}}
     
    #每个目录使用独立的历史纪录{{{
    cd() {
    builtin cd "$@"                             # do actual cd
    fc -W                                       # write current history  file
    local HISTDIR="$HOME/.zsh_history$PWD"      # use nested folders for history
    if  [ ! -d "$HISTDIR" ] ; then          # create folder if needed
    mkdir -p "$HISTDIR"
    fi
    export HISTFILE="$HISTDIR/zhistory"     # set new history file
    touch $HISTFILE
    local ohistsize=$HISTSIZE
    HISTSIZE=0                              # Discard previous dir's history
    HISTSIZE=$ohistsize                     # Prepare for new dir's history
    fc -R                                       #read from current histfile
    }
    mkdir -p $HOME/.zsh_history$PWD
    export HISTFILE="$HOME/.zsh_history$PWD/zhistory"
     
    function allhistory { cat $(find $HOME/.zsh_history -name zhistory) }
    function convhistory {
    sort $1 | uniq |
    sed 's/^:\([ 0-9]*\):[0-9]*;\(.*\)/\1::::::\2/' |
    awk -F"::::::" '{ $1=strftime("%Y-%m-%d %T",$1) "|"; print }'
    }
    #使用 histall 命令查看全部历史纪录
    function histall { convhistory =(allhistory) |
    sed '/^.\{20\} *cd/i\\' }
    #使用 hist 查看当前目录历史纪录
    function hist { convhistory $HISTFILE }
     
    #全部历史纪录 top50
    function top50 { allhistory | awk -F':[ 0-9]*:[0-9]*;' '{ $1="" ; print }' | sed 's/ /\n/g' | sed '/^$/d' | sort | uniq -c | sort -nr | head -n 50 }
     
    #}}}
     
    #杂项 {{{
    #允许在交互模式中使用注释  例如：
    #cmd #这是注释
    setopt INTERACTIVE_COMMENTS      
     
    #启用自动 cd，输入目录名回车进入目录
    #稍微有点混乱，不如 cd 补全实用
    setopt AUTO_CD
     
    #扩展路径
    #/v/c/p/p => /var/cache/pacman/pkg
    setopt complete_in_word
     
    #禁用 core dumps
    limit coredumpsize 0
     
    #Emacs风格 键绑定
    bindkey -e
    #bindkey -v
    #设置 [DEL]键 为向后删除
    #bindkey "\e[3~" delete-char
     
    #以下字符视为单词的一部分
    WORDCHARS='*?_-[]~=&;!#$%^(){}<>'
    #}}}
     
    #自动补全功能 {{{
    setopt AUTO_LIST
    setopt AUTO_MENU
    #开启此选项，补全时会直接选中菜单项
    #setopt MENU_COMPLETE
     
    autoload -U compinit
    compinit
     
    #自动补全缓存
    #zstyle ':completion::complete:*' use-cache on
    #zstyle ':completion::complete:*' cache-path .zcache
    #zstyle ':completion:*:cd:*' ignore-parents parent pwd
     
    #自动补全选项
    zstyle ':completion:*' verbose yes
    zstyle ':completion:*' menu select
    zstyle ':completion:*:*:default' force-list always
    zstyle ':completion:*' select-prompt '%SSelect:  lines: %L  matches: %M  [%p]'
     
    zstyle ':completion:*:match:*' original only
    zstyle ':completion::prefix-1:*' completer _complete
    zstyle ':completion:predict:*' completer _complete
    zstyle ':completion:incremental:*' completer _complete _correct
    zstyle ':completion:*' completer _complete _prefix _correct _prefix _match _approximate
     
    #路径补全
    zstyle ':completion:*' expand 'yes'
    zstyle ':completion:*' squeeze-shlashes 'yes'
    zstyle ':completion::complete:*' '\\'
     
    #彩色补全菜单
    eval $(dircolors -b)
    export ZLSCOLORS="${LS_COLORS}"
    zmodload zsh/complist
    zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}
    zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
     
    #修正大小写
    zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}'
    #错误校正
    zstyle ':completion:*' completer _complete _match _approximate
    zstyle ':completion:*:match:*' original only
    zstyle ':completion:*:approximate:*' max-errors 1 numeric
     
    #kill 命令补全
    compdef pkill=kill
    compdef pkill=killall
    zstyle ':completion:*:*:kill:*' menu yes select
    zstyle ':completion:*:*:*:*:processes' force-list always
    zstyle ':completion:*:processes' command 'ps -au$USER'
     
    #补全类型提示分组
    zstyle ':completion:*:matches' group 'yes'
    zstyle ':completion:*' group-name ''
    zstyle ':completion:*:options' description 'yes'
    zstyle ':completion:*:options' auto-description '%d'
    zstyle ':completion:*:descriptions' format $'\e[01;33m -- %d --\e[0m'
    zstyle ':completion:*:messages' format $'\e[01;35m -- %d --\e[0m'
    zstyle ':completion:*:warnings' format $'\e[01;31m -- No Matches Found --\e[0m'
    zstyle ':completion:*:corrections' format $'\e[01;32m -- %d (errors: %e) --\e[0m'
     
    # cd ~ 补全顺序
    zstyle ':completion:*:-tilde-:*' group-order 'named-directories' 'path-directories' 'users' 'expand'
    #}}}
     
    ##行编辑高亮模式 {{{
    # Ctrl+@ 设置标记，标记和光标点之间为 region
    zle_highlight=(region:bg=magenta #选中区域
    special:bold      #特殊字符
    isearch:underline)#搜索时使用的关键字
    #}}}
     
    ##空行(光标在行首)补全 "cd " {{{
    user-complete(){
    case $BUFFER in
    "" )                       # 空行填入 "cd "
    BUFFER="cd "
    zle end-of-line
    zle expand-or-complete
    ;;
    "cd --" )                  # "cd --" 替换为 "cd +"
    BUFFER="cd +"
    zle end-of-line
    zle expand-or-complete
    ;;
    "cd +-" )                  # "cd +-" 替换为 "cd -"
    BUFFER="cd -"
    zle end-of-line
    zle expand-or-complete
    ;;
    * )
    zle expand-or-complete
    ;;
    esac
    }
    zle -N user-complete
    bindkey "\t" user-complete
    #}}}
     
    ##在命令前插入 sudo {{{
    #定义功能
    sudo-command-line() {
    [[ -z $BUFFER ]] && zle up-history
    [[ $BUFFER != sudo\ * ]] && BUFFER="sudo $BUFFER"
    zle end-of-line                 #光标移动到行末
    }
    zle -N sudo-command-line
    #定义快捷键为： [Esc] [Esc]
    bindkey "\e\e" sudo-command-line
    #}}}
     
    #命令别名 {{{
    alias cp='cp -i'
    alias mv='mv -i'
    alias rm='rm -i'
    alias ls='ls -F --color=auto'
    alias ll='ls -al'
    alias grep='grep --color=auto'
    alias la='ls -a'
    alias pacman='sudo pacman-color'
    alias p='sudo pacman-color'
    alias y='yaourt'
    alias h='htop'
     
    #[Esc][h] man 当前命令时，显示简短说明
    alias run-help >&/dev/null && unalias run-help
    autoload run-help
     
    #历史命令 top10
    alias top10='print -l  ${(o)history%% *} | uniq -c | sort -nr | head -n 10'
    #}}}
     
    #路径别名 {{{
    #进入相应的路径时只要 cd ~xxx
    hash -d A="/media/ayu/dearest"
    hash -d H="/media/data/backup/ayu"
    hash -d E="/etc/"
    hash -d D="/home/ayumi/Documents"
    #}}}
     
    ##for Emacs {{{
    #在 Emacs终端 中使用 Zsh 的一些设置 不推荐在 Emacs 中使用它
    #if [[ "$TERM" == "dumb" ]]; then
    #setopt No_zle
    #PROMPT='%n@%M %/
    #>>'
    #alias ls='ls -F'
    #fi
    #}}}
     
    #{{{自定义补全
    #补全 ping
    zstyle ':completion:*:ping:*' hosts 192.168.1.{1,50,51,100,101} www.google.com
     
    #补全 ssh scp sftp 等
    #zstyle -e ':completion::*:*:*:hosts' hosts 'reply=(${=${${(f)"$(cat {/etc/ssh_,~/.ssh/known_}hosts(|2)(N) /dev/null)"}%%[# ]*}//,/ })'
    #}}}
     
    #{{{ F1 计算器
    arith-eval-echo() {
    LBUFFER="${LBUFFER}echo \$(( "
    RBUFFER=" ))$RBUFFER"
    }
    zle -N arith-eval-echo
    bindkey "^[[11~" arith-eval-echo
    #}}}
     
    ####{{{
    function timeconv { date -d @$1 +"%Y-%m-%d %T" }
     
    # }}}
     
    zmodload zsh/mathfunc
    autoload -U zsh-mime-setup
    zsh-mime-setup
    setopt EXTENDED_GLOB
    #autoload -U promptinit
    #promptinit
    #prompt redhat
     
    setopt correctall
    autoload compinstall
     
    #漂亮又实用的命令高亮界面
    setopt extended_glob
     TOKENS_FOLLOWED_BY_COMMANDS=('|' '||' ';' '&' '&&' 'sudo' 'do' 'time' 'strace')
     
     recolor-cmd() {
         region_highlight=()
         colorize=true
         start_pos=0
         for arg in ${(z)BUFFER}; do
             ((start_pos+=${#BUFFER[$start_pos+1,-1]}-${#${BUFFER[$start_pos+1,-1]## #}}))
             ((end_pos=$start_pos+${#arg}))
             if $colorize; then
                 colorize=false
                 res=$(LC_ALL=C builtin type $arg 2>/dev/null)
                 case $res in
                     *'reserved word'*)   style="fg=magenta,bold";;
                     *'alias for'*)       style="fg=cyan,bold";;
                     *'shell builtin'*)   style="fg=yellow,bold";;
                     *'shell function'*)  style='fg=green,bold';;
                     *"$arg is"*)
                         [[ $arg = 'sudo' ]] && style="fg=red,bold" || style="fg=blue,bold";;
                     *)                   style='none,bold';;
                 esac
                 region_highlight+=("$start_pos $end_pos $style")
             fi
             [[ ${${TOKENS_FOLLOWED_BY_COMMANDS[(r)${arg//|/\|}]}:+yes} = 'yes' ]] && colorize=true
             start_pos=$end_pos
         done
     }
    check-cmd-self-insert() { zle .self-insert && recolor-cmd }
     check-cmd-backward-delete-char() { zle .backward-delete-char && recolor-cmd }
     
     zle -N self-insert check-cmd-self-insert
     zle -N backward-delete-char check-cmd-backward-delete-char

    PATH=$PATH:$HOME/.rvm/bin # Add RVM to PATH for scripting

    # source ~/.zsh/git-prompt/zshrc.sh  # 如果安装git-prompt就开启，包括下行
    # PROMPT='%B%m%~%b$(git_super_status)%# '

    # source ~/.nvm/nvm.sh  # 如果安装nvm则取消注释, nvm是node的一个包管理
    # source /opt/python_env/django1.6.1/bin/activate # 如果有这个python evn

#source /opt/python_env/heroku/bin/activate 

shell 操作命令 生成gif
---
    https://github.com/icholy/ttygif
    http://www.oschina.net/p/ttyrec
    http://my.oschina.net/hanjiafu/blog/155189

    默认的源应该装不上 我换了soho的源就ok了

    按照ttygif里面的方式make完后，将ttygif,和concat.sh cp 到/usr/bin下
    sudo cp make的路径/{ttygif,concat.sh} /usr/bin

    ttyrec tmp # 开始录像
    # 进行录像命令...
    # 点击Ctrl+D 或者输入exit结束录像
    ttygif tmp # 生成gif贞
    concat.sh terminal.gif # 生成gif图片

chrome安装SwitchySharp
---

问题，在新机器上没翻墙前是登陆不了chrome的，也就拿不到书签和扩展，没有扩展就没法翻墙，
鸡生蛋蛋生鸡的问题。好在goagent自带电池，在goagent local 下有SwitchySharp.crx

第一步是装SwitchySharp

1. 如果最近google没被墙，自然可以商店里面直接安装；
2. windows用户直接在chrome中打开extensions(扩展程序), 把SwitchySharp.crx拖进去即可安装;
3. linux用户比较蛋疼，总之ubuntu是很蛋疼的，不能托到chrome里面去，需要将SwitchySharp.crx
   重命名为SwitchySharp.zip,解压，然后在chrome extensions里面点开开发这模式，Load unpacked
   extension 将解压的文件夹加过来即可安装。

解决goagent翻墙后上twitter等无效
----
    Ubuntu 系统：
    打开 Chrome 浏览器 首选项 > 高级选项 > 管理证书…
    在授权中心导入 GoAgent/local 目录下的 CA.crt
    证书（注意不要导入到服务器，否则不起作用） 在 
    授权中心 找到 GoAgent CA 并点击 修改… 
    修改信任设置为全部选中 重启浏览器

    Windows 系统： 打开 Chrome 浏览器 选项 > 高级选项 > 管理证书… 
    导入证书 > 下一步 >选择GoAgent/local 目录下的 CA.crt证书 
    > 下一步 > 选择 证书存储： 浏览… > 
    受信任的根证书颁发机构 > 下一步 … > 完成 重启浏览器
    （在系统托盘右键chrome图标退出，如果直接点击窗口关闭按键无效）

    http://lyericwang.blog.163.com/blog/static/716901742012626156844/

浏览器快捷键
---
    Ctrl+T            # 打开新标签页
    Ctrl+Shift+T      # 重新打开上次关闭的标签页。 
    Ctrl+1 ~ Ctrl+8   # 切换到指定位置编号的标签页。
    Ctrl+9            # 切换到最后一个标签页
    Ctrl+Tab          # 切换到下一个标签页
    Ctrl+Shift+Tab    # 切换到上一个标签页
    Ctrl+W or Ctrl+F4 # 关闭当前标签页或窗口


tree
---
    显示文件加结构
    sudo apt-get install tree
    tree

    .
    ├── angularjs.issue.md
    ├── build.issue.md
    ├── css.issue.md
    ├── django.issue.md
    ├── git.issue.md
    ├── heroku.issue.md
    ├── js.issue.md
    ├── linux.issue.md
    ├── nginx.issue.md
    ├── oauth.issue.md
    ├── python.issue.md
    ├── README.md
    ├── scrapy.issue.md
    ├── springmvc.issue.md
    ├── vim.issue.md
    └── zarkpy.issue.md

桌面通知
---
    notify-send 跑步
    可以与crontab配合做提醒

查找
---

1. find

    find 地址 -name 文件名
    find ./ -name settings.py
    时间 -atime n n天前访问的文件
    大小 -size n
    正则 -regex

2. grep

    # 递归查找当前目录所有内容包含"内容"的文件
    grep 内容 -ril ./

    # 超找当前文件夹下前缀为lms文件中包含"内容"的文件
    grep 查找 -ril lms*

    # 递归查找当前目录所有内容包含"内容"的py文件
    grep 内容 -ril $(find -name '*.py')


3. vim command P

    打开vim 点击ctrl + p

压缩解压
---

.tar.gz 和 .tgz
解压：tar zxvf FileName.tar.gz
压缩：tar zcvf FileName.tar.gz DirName // 压缩参数加上 p可以保持权限，解压后cp -p可以保持权限不变

mysql暂时关闭外键
---
SET foreign_key_checks = 0;

mysql修改密码
---

    mysql -u root -p

　　mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('newpass');

用户相关
---

添加用户

    useradd duoduo

添加用户组

    groupadd  duoduo

显示各个组

    groups

添加root权限

    sudo vim /etc/sudoers
    在root  ALL=(ALL:ALL) ALL下添加
    duoduo  ALL=(ALL:ALL) ALL

修改密码

    passwd duoduo

查看用户信息

    id

文件下载
---

wget 支持断点下载的工具

    wget -c -t 0 -O new_name.tar.gz http://www.cnscn.org/old_name.tar.gz 
    -c 断点 -t 0 反复尝试  -O 重命名

查找之前命令
---
在shell里面会输入很多命令，有的时候你想找几百次之前的某条名利，按下`ctrl + r`搜索


安装ttf字体
---
[fontpalace](http://www.fontpalace.com/)下载喜欢的字体，程序员一般选consolas

    cd 到下载目录后

    sudo cp *.ttf /usr/local/share/fonts
    cd /usr/local/share/fonts
    sudo chown root:root *.ttf
    sudo fc-cache

查看端口
---

    netstat -ntlp

linux 更新locale
---

    sudo apt-get install language-pack-en-base
    sudo dpkg-reconfigure locales

    add to ~/.zshrc

    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8

    source ~/.zshrc

    中文
    sudo apt-get install language-pack-zh-hans-base


sed
---

-n 不打印
-n p打印
d删除
w重定向
s替换
e执行命令
&表示匹配的正则
i添加行,行前
a添加行,行后

    sed -n 'p' 文件 = cat 文件
    sed -n '1,4p' 文件 = 打印文件的1~4行
    sed -n '1~4p' 文件 = 从第一行开始，每隔4行打一行
    sed -n '/正则/p' 文件 = 打印文件符合正则的行
    sed -n -e '/正则1/p' -e '/正则2/p' 文件 = 打印文件符合正则1或正则2的行
    sed -n '{/正则1/p
    /正则2/p}' 文件 = 打印文件符合正则1或正则2的行

    r.txt --> 里面有两行
    /正则1/p
    /正则2/p
    sed -n -f r.txt 文件 = 打印文件符合正则1或正则2的行

    sed -n '/正则1/,/正则2/p' 文件 = 打印从符合正则1开始的行到符合正则2的所有行

    sed -n '/正则1/,8p' 文件 = 打印从符合正则1开始打印到第8行
    sed -n '/正则1/,+3p' 文件 = 打印从符合正则1开始，再多3行

    sed '2d' 文件 = 打印去掉第二行后的文件

    sed '2 w 输出文件' 输入文件 = 将输入文件的第二行写到输出文件
    sed -n '/正则/,$ w 输出文件' 输入文件 = 将输入文件中符合正则开始的行到最后的行写到输出文件中

    sed 's/正则1/正则2/' 文件 = 将正则由1替换成2
    sed -n 's/正则1/正则2/p' 文件 = 打印替换结果
    sed '/查找正则/s/正则1/正则2/' = 替换查找正则行里面的正则1到正则2
    sed 's/正则1/正则2/g' 文件 = 默认一行只换第一个，g表示全换
    sed 's/正则1/正则2/i' 文件 = i表示忽略大小写

    sed 's/^/文字/g' 文件 = 为文件每行开头添加文字
    sed 's/&/文字/g' 文件 = 为文件每行开头添加文字
    sed '{s/^/文字1/g
    s/$/文字2/g}' 文件 = 为文件每行开头添加文字1,结尾添加文字2

    sed 's/^/ls -l /e' files.txt(文件名列表)

    sed 's/^.*/<&>/' 文件，将文件每行添加<>

    sed -ibak -i 会修改源文件 bak会备份

    sed '2 a 字符串' 文件= 在文件第2行后添加字符串
    sed '2 i 字符串' 文件= 在文件第2行前添加字符串
    sed '2 c 字符串' 文件= 在文件修改第2行为字符串

awk
---

awk处理列,只记录简单的分割操作，复杂的话还是用python脚本

    awk -F, '{print $1}' 使用,分割，打印第一列
    awk -F: '{print $NF}' 使用:分割，打印最后一些
    awk -F: '/AA/ {print $1}' 找到AA的所有行，按照:分割，打印第一列


磁盘命令
---
因为虚拟机给配的磁盘很小，经常因为磁盘的原因起不了服务(超大的log文件，测试时可以删)

    df 查看磁盘占中
    du -sh * 递归查看各个文件磁盘大小
    du -h 显示为M kb这种

    ncdu 需要安装先,比du -sh *快


yes输入y
---
    很多时候(大部分是删除)时会问你y/n
    yes XXX 会一直打印XXX,默认是y
    yes | rm -i *.txt
    yes | cp -rf xxx yyy


tail实时打印
---
    查log时需要实时查看
    tail -f XXX.log

cd - 回到刚才的目录
---
    在linux下，有的时候cd会不小心cd到家目录，cd -可以直接返回你刚才的目录

查看进程树
---
    pstree -p

bash输入命令时删除最后一个词
---
    ctrl + w

查看文件行数
---
    wc -l 文件名

获取外网IP
---
    curl ip.cn
    curl cip.cc
    curl ifconfig.me
    windows: telnet cip.cc
    telnet win7 win8需要开启 自行百度

使用sz rz传输文件
---

    sudo apt-get install lrzsz
    rz -be 从本地传到服务器
    sz 从服务器下载到本地

curl获得网页header信息
---

    curl -I www.baidu.com


查看服务器连接
---

> to get a list of the number of connections you have per ip run,

`netstat -nat | awk {'print $5'} | cut -d ':' -f1 | sort | uniq -c | sort -n`

查看TIME_WAIT
---

`netstat -an | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'`

    TIME_WAIT 814
    CLOSE_WAIT 1
    FIN_WAIT1 1
    ESTABLISHED 634
    SYN_RECV 2
    LAST_ACK 1

常用的三个状态是：ESTABLISHED 表示正在通信，TIME_WAIT 表示主动关闭，CLOSE_WAIT 表示被动关闭。

[文章](http://blog.csdn.net/shootyou/article/details/6622226)

linux机器之间不输入密码直接ssh
---
例如 机器A想ssh到B，并且不输入密码

对于B机器需要:

vim /etc/ssh/sshd_config, 将下面几行的注释去掉

    PubkeyAuthentication yes
    PubkeyAuthentication no
    AuthorizedKeysFile     %h/.ssh/authorized_keys

将A机器的公钥 `~/.ssh/id_rsa.pub`里面的东西粘贴到B的 `~/.ssh/authorized_keys`里

B机器重启ssh服务 `service ssh restart`

mac方法: http://www.zhihu.com/question/30640159

xshell中文乱码
---

在Xshell中[file]-> [open] -> 在打开的session中选择连接的那个，点击properties ->[Terminal]，在右边translation中选择UTF-8，再重新连接服务器即可。
[原文](http://blog.csdn.net/choice_jj/article/details/8020278)

录制shell
---
http://showterm.io/

处理json
---
[jq](https://stedolan.github.io/jq/)
