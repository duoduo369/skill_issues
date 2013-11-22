nginx相关
====

nginx安装
---

请参考  linux-server.issue.md 服务器安装文件,源码或者解压方式中的nginx部分

nginx配置
---

nginx配置离不开服务器，当然localhost也可以算服务器。

##举例：
**下面配置一个名叫me.aft.com的server，开发时在本机开发(127.0.0.1)。**

####DNS
首先需要在/etc/hosts下添加一行,因为DNS里面没有me.aft.com只能自己机器来搞了。

    127.0.0.1 me.aft.com

####配置nginx
在nginx的配置地址(与编译参数有关，可以nginx -V察看里面的--conf-path )，如/etc/nginx，先瞅一瞅，vim /etc/nginx/nginx.cnf：

默认安装的参数有一堆注释，先不管，有一个server_name 为localhost的，类似下面，
这个就是安装玩nginx之后输入localhost会出现欢迎界面的配置。

    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

####结合nginx的网站
下面配置一个简单的网站，nginx优化的东西暂时不关心，就是做一个动静分离的网站而已，nginx不关心后台服务器的实现方式，他做一个转发的角色。这里后台使用4个 tomcat。

首先/etc/nginx下新建个文件夹，mkdir /etc/nginx/aft，这么做是不想把nginx.cnf这个主配置文件搞脏，nginx.cnf中使用include /etc/nginx/aft/*包含aft下面所有的nginx server的配置，现在nginx.cnf可能看起来这个样子：


    worker_processes  4;


    events {
        worker_connections  10240;
    }


    http {
        include       mime.types;
        default_type  application/octet-stream;
        
        sendfile        on;
        keepalive_timeout  65;

        gzip  on;

        include /etc/nginx/aft/* ; # /etc/nginx/aft/aft 
       

    }

在aft文件夹下建个一**软链接**，

    ln -s aft -> /home/duoduo/git/SpringMVCPractice/justforfun/WebContent/doc/nginx/aft,

例如我有一个项目justforfun,里面有个aft的nginx配置文件，做软链接的话直接可以在项目里面改这个文件，不用每次跑到/etc/nginx/aft这里更改.

####aft配置文件讲解

    # /etc/hosts/ 
    # 127.0.0.1 me.aft.com
    # tomcat server.xml path=""
    upstream tomcat {
    ip_hash;
    server 127.0.0.1:8080 weight=2;
        server 127.0.0.1:8081 weight=2;
        server 127.0.0.1:8080 weight=2;
        server 127.0.0.1:8081 weight=2;
        check interval=3000 rise=2 fall=5 timeout=1000;
    }
    server {
        listen 80;
        server_name  me.aft.com;
        set $tomcat_location /home/duoduo/tomcats/tomcat;
        location = / {
            proxy_pass http://tomcat;
        }
        location  ~ ^/ueditor/ {
            root $tomcat_location/webapps/justforfun/;
        }
        location  ~ ^/changable1.0.0/ {
            root $tomcat_location/webapps/justforfun/resources;
        }
        location ~ \.(js|css)$ {
            root $tomcat_location/webapps/justforfun/resources;
        }
        location /nstatus {
            check_status;
            access_log off;
            #allow SOME.IP.ADD.RESS;
            ##deny all;
        }
        location / {
            proxy_pass http://tomcat;
        }
    }

#####upstream
使用tomcat集群，所以搞一个upstream ，名字随便起，这里叫做tomcat，里面的server注意不要加http://。

使用ip_hash算法，这样同一个用户就会映射到同一个tomcat,注意nginx中ip_hash使用的是**c类网络**(例如192.168.1.102他只会取192.168.1),源码中hash3次，得到最终的结果，这样子如果是**内网测试**的话，所有的机器都会到**相同**的tomcat上，**不是ip_hash不准，人家就是这么设计的**。

weight是RR（轮询，nginx的一种调度方式）时用到的参数，权重越大，这个server的责任越重。

check 这不是nginx默认模块里的，需要安装**nginx_upstream_check_module**给nginx做健康度检查，可以看其个server的状态，很有用的。
    
    upstream tomcat {
    ip_hash;
    server 127.0.0.1:8080 weight=2;
        server 127.0.0.1:8081 weight=2;
        server 127.0.0.1:8080 weight=2;
        server 127.0.0.1:8081 weight=2;
        check interval=3000 rise=2 fall=5 timeout=1000;
    }

#####server

server最重要，关系到你文件能不能访问到。

listen监听80端口，server_name监听的名字,例如server_name： me.aft.com 192.168.1.200，这样配置的话如果你访问http://me.aft.com 或者http://192.168.1.200,nginx就会在这个server里面找location里对应的文件。

set，可以用set设置变量。例如：`set $tomcat_location /home/duoduo/tomcats/tomcat;`

location的配置规则，最长匹配，如果location里面有多个符合的地方，他会找匹配串里最长的那一串,location里面的地址最后不要轻易加/；

    * = 号直接匹配，例如下面的“= /”（首页）,proxy_pass http://tomcat; proxy_pass是nginx会条转到什么地方去，这里写tomcat，对应上面upstream里面的四个server，在这里写http://

    * ~ ^/ueditor/,以/ueditor/开头文件找这里(root $tomcat_location/webapps/justforfun)，因为里面都是静态文件，所以直接访问磁盘的静态文件，对应规则是这样的http://me.aft.com/ueditor/XXX  --》/home/duoduo/tomcats/tomcat/webapps/justforfun/XXX。
 
    * /nstatus 直接匹配http://me.aft.com/nstatus，nginx的健康度检查，能看到你的server那几个还活着。

    * /  ，这个匹配所有之前没匹配到的东西，也就是动态文件jsp|freemarker之类的，直接把权利交还给原服务器处理。

    server {
        listen 80;
        server_name  me.aft.com;
        set $tomcat_location /home/duoduo/tomcats/tomcat;
        location = / {
            proxy_pass http://tomcat;
        }
        location  ~ ^/ueditor/ {
            root $tomcat_location/webapps/justforfun;
        }
        location  ~ ^/changable1.0.0/ {
            root $tomcat_location/webapps/justforfun/resources;
        }
        location ~ \.(js|css)$ {
            root $tomcat_location/webapps/justforfun/resources;
        }
        location /nstatus {
            check_status;
            access_log off;
            #allow SOME.IP.ADD.RESS;
            ##deny all;
        }
        location / {
            proxy_pass http://tomcat;
        }
    }

ps：如果需要别的机器访问来测试的话，别忘了修改iptables，把80端口给开出来。

