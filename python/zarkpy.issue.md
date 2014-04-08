zarkpy相关问题
====

https://github.com/sdjl/zarkpy
http://sdjl.me/index.php/archives/320

git clone
---
clone 回来放在你的home/yourname目录下面，并且在/opt/建立一个软链接

#vim zark快捷键F1（快速重启） F2(检查bug的错误日志)

F1重启程序
----

例如项目是caadf
注意里面的两个path 是真实的文件地址，例如我的项目都在/home/duoduo/projects/里面，然后第二个注意的是，需要在/opt/里面建立软链接

    duoduo@debian ...caadf/web/cgi % cat /usr/local/bin/launch-curr.py

    #!/usr/bin/env python
    #coding=utf8
    # 你可能会使用zarkpy建立多个项目，此程序用于在vim中添加重新启动当前项目的快捷键

    import sys, os
    assert len(sys.argv) == 2
    file_path = sys.argv[1]
    print file_path
    assert file_path.startswith('/home/duoduo/projects/')
    project_name = file_path.partition('/home/duoduo/projects/')[2].partition('/')[0]
    os.popen('/opt/%s/tool/launch-local.sh restart' % project_name)                                                                  

F2看错误
---
如果提示没有文件的话，建立对应的文件目录。注意事项与上一条相同

    duoduo@debian ...caadf/web/cgi % cat /usr/local/bin/error-curr.py

    #!/usr/bin/env python
    #coding=utf8
    # 你可能会使用zarkpy建立多个项目，此程序用于在vim中查看当前项目的error

    import sys, os
    assert len(sys.argv) == 2
    file_path = sys.argv[1]
    assert file_path.startswith('/home/duoduo/projects/')
    project_name = file_path.partition('/home/duoduo/projects/')[2].partition('/')[0]
    print open('/opt/%s/log/error.log' % project_name, 'r').read()

后台管理创建管理员
---

    python /opt/caadf/web/cgi/model/AdminUser.py add test@sparker5.com test test
