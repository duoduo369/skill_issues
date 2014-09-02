nginx相关
====

root与alias
---

location 部分为用户请求

    root选项会将 root地址+location地址拼接成一个Linux路径。
    alias则指定了一个绝对路径，不会拼接location


例子：静态文件的路径为`/public/html/index.html`

root选项：

    location /html {
        root  /public;
    }

    此时nginx看到/public/html/index.html后，发现有html路径,
    找到location /html, 因为是root最终Linux路径为
    root + location ——> /public/html

alias选项：

    location /html {
        alias  /public/html;
    }

    此时nginx看到/public/html/index.html后，发现有html路径,
    找到location /html, 因为是alias,最终Linux路径为alias路径
    alias ——> /public/html

nginx简单的调试
---

如果你没有装echo模块的话可以使用add_header来做一些调试打印,例如
下面的代码就是在请求public的response里面加上了test_nginx则个参数，
并且值为test,即使是404也会有.打开chrome的调试工具可以在network中
轻松的看到这个response带的请求

    location /public {
        add_header test_nginx 'test';
        root /opt/test;
        #index b.html;
    }

url截取(重新)
---
location 可以使用@来命名，官方叫法是named location,这种location只能在
nginx内部使用，一般做跳转.

例如下面的配置就可以将/abc/public/a.html 转换为/public/a.html做到一个url截取的效果

    location /abc {
        add_header test_nginx 'test';
        #index b.html;
        error_page 418 = @inner;return 418;
    }

    location @inner {
        root /opt/test;
        rewrite ^/abc(.+)$ /$1 break;
        add_header inner 'inner';
    }

下面这种配置可以做到url的截取,当需要代理到其他地方做负载均衡的时候需要

    location /dontwantprofix {
        add_header test_nginx 'test';
        rewrite /dontwantprofix/(.*) /$1  break;
        proxy_pass   http://test_server;
        proxy_redirect     off;
        proxy_set_header   Host             $host;
        proxy_set_header   X-Real-IP        $remote_addr;
        proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
    }
