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
