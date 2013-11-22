python写的脚本
===

##tomcat相关脚本(4个)

字符串替换脚本
----
需要系统中有python sed

用法:python 需要替换的文件路径 原字符串 目标字符串


    #!/usr/bin/env python
    #coding=utf-8
    # 字符串重命名脚本 
    # 用法:file old_str new_str 
    import os
    import sys

    if __name__=='__main__':
        if len(sys.argv) == 4:
            file_path = sys.argv[1]
            old_name = sys.argv[2]
            new_name = sys.argv[3]
            if os.path.exists(file_path): 
                print '把文件"%s"中的"%s"字符串替换为"%s"' % (file_path,old_name, new_name)
                os.system('''sed -i "" -e "s/%s/%s/g" "%s" 2>/dev/null''' % (old_name, new_name, file_path))
            else:
                print '%s 不存在，请检查你的输入' % file_path
        else:
            print 'Usage: python replace_str.py file_path old_str new_str'
            print 'rename之前,建议先备份原代码'


tomcat 里面的server.xml文件端口替换脚本
----

多个tomcat的时候需要替换这几个端口号t("8080","8009","8443","8005")，需要用到之前的字符串低换脚本

用法： python replace_tomcat_server_port.py replace_str.py文件路径 替换server.xml端口加的阀值，例如如果server_num=4,("8080","8009","8443","8005")-->("8084","8013","8447","8009")

    #!/usr/bin/env python
    #coding=utf-8
    # tomcat server.xml端口重命名脚本,以第一个tomcat为基准
    import sys
    import os 

    PORTS=("8080","8009","8443","8005")

    if __name__=='__main__':
        if len(sys.argv) == 4:
            replace_strpy_path = sys.argv[1]
            tomcat_path = sys.argv[2]
            server_num = sys.argv[3]
            serverxml_path = "%s/conf/server.xml" % tomcat_path
            if not os.path.exists(replace_strpy_path):
                print "替换脚本%s不存在" % (replace_strpy_path)
                exit(1)
            if not replace_strpy_path.endswith("py"):
                print "替换脚本路径%s 输入有误" % (replace_strpy_path)
                exit(1)
            if not os.path.exists(serverxml_path): 
                print '%s 不存在，请检查你的输入' % serverxml_path
                exit(1)        
            try:
                server_num = int(server_num)
                if server_num <= 0:
                    raise Exception("参数 server_num 输入错误,应该大于0")
                    exit(1)
            except:
                print '参数 server_num 输入类型错误，应该为int' % server_num
                exit(1)
            else:
                for port in PORTS:
                   # print "%s %s %s %s " %  (replace_strpy_path,serverxml_path, port, str(int(port)+server_num))
                    os.system('''"%s" %s %s %s 2>/dev/null''' % (replace_strpy_path,serverxml_path, port, str(int(port)+server_num)))
        else:
            print 'Usage: python replace_tomcat_server_port.py /filepath/replace_str.py server_num(int)'
            print 'rename之前,建议先备份原代码'

tomcat复制脚本
----
tomcat复制脚本，复制之后会进行server.xml的端口重命名，用到了之前的server.xml文件端口替换脚本，和字符串替换脚本，需要将他们放在一个文件夹中。

用法：Usage: python cp_tomcat.py 要拷贝的tomcat的路径 拷贝的份数

 
   #!/usr/bin/env python
    #coding=utf-8
    #tomcat复制脚本，复制之后会进行server.xml的端口重命名

    import os
    import sys

    if __name__ == '__main__':
        if len(sys.argv) == 3:
            tomcat_path = sys.argv[1]
            cp_nums = sys.argv[2]
            
            this_file_path = os.path.split(os.path.realpath(__file__))[0]
            replace_tomcat_server_port_py_path = '%s/replace_tomcat_server_port.py' %(this_file_path)
            place_strpy_path = '%s/replace_str.py' % (this_file_path)
            try:
                cp_nums = int(cp_nums)
                if cp_nums <= 0:
                    raise Exception("参数 server_num 输入错误,应该大于0")
                    exit(1)
            except:
                print '参数拷贝份数 cp_nums 输入类型错误，应该为int' % cp_nums
                exit(1)    
            if not os.path.exists(tomcat_path):
                print 'tomcat路径输入有误：%s' % (tomcat_path)
                exit(1)    
            if not os.path.exists(replace_tomcat_server_port_py_path):
                print '替换server.xml脚本%s不存在 请将%s放在同一文件夹下' % (place_strpy_path,'replace_tomcat_server_port.py')
                exit(1)
            if not os.path.exists(place_strpy_path):
                print '替换脚本%s不存在 请将%s放在同一文件夹下' % (place_strpy_path,'replace_str.py')
                exit(1)
            try:    
                print 'bin/*.sh 添加x权限' 
                os.system('chmod +x %s/bin/*.sh' % (tomcat_path))
            except:
                print '为%s/bin/*.sh文件添加权限时发生错误，请检查你tomcat的路径是否输入正确' % (tomcat_path)
                exit(1)
            
            for i in xrange(1,cp_nums+1):
                cp_tomcat_path = '%s_%s' % (tomcat_path,i)
                print '复制tomcat文件 %s  to %s' % (tomcat_path,cp_tomcat_path)
                os.system('cp -r %s %s' % (tomcat_path,cp_tomcat_path))
                print 'server.xml端口号重命名'
                os.system('''"%s" %s %s %s 2>/dev/null''' % (replace_tomcat_server_port_py_path,place_strpy_path, cp_tomcat_path, i))
        else:
            print 'Usage: python cp_tomcat.py tomcat_path cp_nums'
            print 'rename之前,建议先备份原代码'

tomcat集群启动关闭脚本
-----
 用法：Usage: python tomcats.py (start|shutdown) 第一个tomcat位置 启动或者关闭的份数



   #!/usr/bin/env python
    #coding=utf-8
    # 启动或关闭tomcat集群，以第一个tomcat的端口为基准

    import os
    import sys

    FIRST_TOMCAT_PORT = 8080

    if __name__=="__main__":
        if len(sys.argv) == 4:
            cmd_type = sys.argv[1]
            first_tomcat_path = sys.argv[2]    
            nums = sys.argv[3]
            try:
                cmd_type = cmd_type.strip()
                if cmd_type != "start" and cmd_type != "shutdown":
                    print "cmd_type应为(%s|%s)" % ("start","shutdown")
                    exit(1)
            except:
                 print "cmd_type应为(%s|%s)" % ("start","shutdown")
                 exit(1)
            if not os.path.exists(first_tomcat_path):
                print "队首tomcat路径输入有误：%s" % (first_tomcat_path)
                exit(1)
            try:
                nums = int(nums)
                if nums <= 0:
                    raise Exception("参数 nums 输入错误,应该大于0")
                    exit(1)
            except:
                print "参数 nums 输入类型错误，应该为int" % nums
                exit(1)
            if cmd_type == "start":
                cmd = "startup.sh"
            else:
                cmd = "shutdown.sh"
            # 第一个tomcat
            os.system("%s/bin/%s" % (first_tomcat_path,cmd))
            # 其余的tomcat
            if nums > 1:
                for i in xrange(1,nums):
                    os.system("%s_%s/bin/%s"% (first_tomcat_path,i,cmd)) 
        else:
            print "Usage: python tomcats.py (start|shutdown) first_tomcat_path nums(int) "
