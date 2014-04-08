heroku
===

查看日志
---
    heroku logs -n 20(最大1500) --app 你的app 
    python 里面print 的东西会显示
    https://devcenter.heroku.com/articles/logging

本地测试
---
    oauth 需要填写线上地址，怎么本地测试呢？
    例如:
    test.herokuapp.com

    foreman start 默认在0.0.0.0:5000

    sudo vim /etc/hosts
    添加
    127.0.0.1 test.herokuapp.com

    server {
      server_name  test.herokuapp.com;
      if ($http_host ~ "test\.herokuapp\.com$") {
           rewrite ^/(.*)$ http://0.0.0.0:5000 permanent;
      }
    }

