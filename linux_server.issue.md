linux服务器的相关问题
===

ssh登录服务器
---
http://blog.csdn.net/hugeheadhuge/article/details/6719405

在Ubuntu客户端通过ssh登录服务器。假设服务器的IP地址是192.168.0.103，登录的用户名是hyx。

    $ ssh -l hyx 192.168.0.103

接下来会提示输入密码，然后就能成功登录到服务器上了。

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

###数据库导出

mysqldump --extended-insert=FALSE --complete-insert=TRUE -uroot -p -h
115.28.17.93(远程数据库ip)  health(远程数据库名字) > ~/health.sql

dump出特定的表
mysqldump --extended-insert=FALSE --complete-insert=TRUE -uroot -p -h
115.28.17.93(远程数据库ip)  health tb1 tb2 tb3 > ~/health.sql
