python的相关问题
=====

###
结构
    * python安装相关
    * python编码规范
    * python语法技巧
    * python部分脚本
    * python部分资源|文章

##python安装相关

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

##python编码规范

import this
----
    The Zen of Python

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

    ----

    python之禅 

    优美胜于丑陋（Python 以编写优美的代码为目标）
    明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
    简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）
    复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
    扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
    间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
    可读性很重要（优美的代码是可读的）
    即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）
    不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）
    当存在多种可能，不要尝试去猜测
    而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
    虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）
    做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）
    如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准） 
    命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召)

python 编码规范
---
    安装pep8 easy_install pep8
    安装autopep8 easy_install autopep8

    安装pyflakes 检查语法
    pip install pyflakes

    用法：pep8 XXX.py，就会告诉你哪些行不符pep8的什么规范
          autopep8 XXX.py, 就会直接在shell中显示符合pep8的脚本的代码


    可以将pep8和pyflakes放到.git的hacks里面提交前自动检查, 参见git issue

    或者编写如下脚本pycheck,然后将这个脚本在bin下建立一个软链接，
    sudo ln -s ~/path/pycheck /usr/local/bin/

        #!/usr/bin/env python
        # -*- coding: utf-8 -*-


        import os
        import sys

        if len(sys.argv) <= 1:
            print 'Usage: pycheck file'
            sys.exit(-1)

        file_ = sys.argv[1]

        if not file_.endswith('.py'):
            print 'only accept *.py file'
            sys.exit(-1)

        os.system("pyflakes %s" % file_)
        os.system("pep8 %s" % file_)


    PEP8
    ---

    4个空格而不是制表符
    ---

    每行最多79个字符,文档注释每行最多72个
    合适使用\(长with,assert),在运算符后面换行，而不是前面
    ---

    一级函数和类定义用两行隔开
    类内函数定义用一行隔开
    ---

    import需要分开写，from XX import的时候可以写在一行,
    import总是写在文件的顶行(文档注释和模块注释下面),
    import按照下面的顺序,并且用空行隔开这三组
    1.标准库
    2.三方库
    3.自定义的模块
    import os
    import sys
    from subprocess import Popen, PIPE

    import 后面写 __all__

    Absolute imports are recommended
    import mypkg.sibling
    from mypkg import sibling
    from mypkg.sibling import example

    尽量避免 from <module> import * 
    ---

    多行对齐的时候，如果第一行有字，则下移行与第一行左
    对齐,如果使用'悬挂'式对齐，则第一行不要有字，注意左
    侧要在一条竖线上。

    # Aligned with opening delimiter
    foo = long_function_name(var_one, var_two,
                             var_three, var_four)

    # More indentation included to distinguish this from the rest.
    def long_function_name(
            var_one, var_two, var_three,
            var_four):
        print(var_one)

    my_list = [
        1, 2, 3,
        4, 5, 6,
        ]
    result = some_function_that_takes_arguments(
        'a', 'b', 'c',
        'd', 'e', 'f',
        )
    ---

    空格

    Yes: spam(ham[1], {eggs: 2}) # 各种括号内部紧接着的地方不加空格

    i = i + 1 # 双目运算符两边都要有空格
    submitted += 1
    x = x*2 - 1
    hypot2 = x*x + y*y # 如果有优先级不同的运算时，低优先级的双目不加空格
    c = (a+b) * (a-b)

    def complex(real, imag=0.0):   # 方法中参数的=前后没有空格
        return magic(r=real, i=imag)

    Yes: if x == 4: print x, y; x, y = y, x # 标点符号(,:;)后加空格，

    Yes: spam(1) # 函数调用的时候()紧接着函数，不加空格

    Yes: dict['key'] = list[index] #字典和数组也是一样
    ---

    注释

    段落注释每行以# 开头
    行注释最少两个空格隔开语句

    文档注释 共有的类，方法需要写，私有的可以不写.
    单行注释，做什么返回什么
    """Do X and return a list."""

    第一行紧接着写简短 描述，空开一行写详细描述，空开一行结尾
    """Return a foobang

    Optional plotz says to frobnicate the bizbaz first.

    """

    命名
    ---
    _single_leading_underscore  # 私有的，from M import * 不会导入
    single_trailing_underscore_  # 最后的下滑线防止与关键字等重名
    __double_leading_underscore  # 类内部使用双下滑线的时候会重命名，
                                 # 类FooBar内部, __boo ->  _FooBar__boo
    __double_leading_and_trailing_underscore__  # 双下划线是magic方法

    不要使用单个l O 做变量名字 可能会看成 1 0

    模块名和包名需要简短而且都是小写字母命名,如果能提高可读性，模块名
    可以加下划线，模块名必须简短，因为模块名是文件夹的名字，有些操作系统会
    截短文件夹名

    类名使用驼峰式 CapWords
    异常类后面加Error后缀
    因为有from M import * ,使用 __all__ 的机制

    方法名用小写下滑线分隔
    如果是private方法和变量的话使用单下划线，双下滑线是为了防止在子类中的命名
    冲突（python会自动重命名，子类只用双下滑线掉不到的）,这样就防止子类继承这个
    属性了。

    为继承设计
    如果开始搞不清楚使用private还是public的时候，设置为private(python没有真正的
    private)


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

    disable=E1101,R0904,W0142,W0622,R0201

    pylint task.py # 此时启用了插件

##python语法技巧

按字符处理字符串
---
    for c in string:
        dosomething

    map(fun,string)

常用字符串
---
    import string

isinstance可以判断多个类型
---
    isinstance(obj,(type1,type2))

    isinstance('duoduo',basestring)

对齐
---
    ljust,rjust,center(20,'补位符')
    '  duoduo'.ljust(20,'*)

join
---
    join前面的东西插入到间隔中
    ',*'.join(map(str,xrange(5))) --> '0,*1,*2,*3,*4'

将字符串按照自己定义的间隔分割
---
    cuts = [2,3,5,8]
    zip([0]+cuts,cuts+[None]) --> [(0, 2), (2, 3), (3, 5), (5, 8), (8,
    None)]

    s = 'duoduo     duoduo'
    pieces = [s[i:j] for i,j in zip([0]+cuts,cuts+[None])]

split分割字符串
---
    当split的规则有多个时，使用re的split

    tring = "the,rain;in,spain"
    pattern = re.compile(',|;')
    words = pattern.split(string)

对象比较
---
    tuple, list比较时候可以这样
    (1, 2, 3) < (1, 2, 4) # True
    # http://stackoverflow.com/questions/5292303/python-tuple-comparison

同行间隔字符串会自动连接
---
    'Hello, world' == "Hello" ", " "world"
    不同行的字符串也会链接
    a = 'aabc'
        'def'

    a == 'aabcdef' # True,
                   # 有一次因为这个原因出的bug找了好久才发现
                   # 类似这样,元组每行需要','分隔，第二行漏了
                   # some_tuple = (
                        'abc',
                        'bed'
                        'edf',
                   )

三个引号注意最后的引号
---
    """last need \""""
    '''last need \''''

万物皆对象
---
    isinstance(None,object) == True # None 也是对象
    None is None # 只有1个None

切片
---
    前闭后开  a[0:3] --> 下表0～2
    前 < 后才有值，否则为[]

创建有默认值的dict
---
    d = {}.fromkeys(('key1','key2'),'value')

格式化字符串
---
    value1 = 'doh'
    value2 = 'DOH'
    1. string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
    2. string = "The values are %s, %s, %s and %s!". % (value2,value1,value1, value2)

    小数点
    string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5), 4)

r字符的一些问题
---
    len('\n') == 1
    len(r'\n') == 2

    '\n' != r'\n'

    raw string 常用于 正则，文件路径，url

python新旧class
---

    class OldStyleClass:
        "An old style class"

    class NewStyleClass(object):
        "A new style class"
        pass

    type(OldStyleClass).__name__ ==  'classobj' #old class 没有__class__
    type(NewStyleClass) == NewStyleClass.__class__ == type

    old_style = OldStyleClass()
    new_style = NewStyleClass()

    old_style.__class__.__name__ == 'OldStyleClass'
    new_style.__class__.__name__ == 'NewStyleClass'

    type(old_style).__name__ == 'instance'
    type(new_style).__name__ == 'NewStyleClass'

函数式
----
    import functools
    functools.partial(func,部分参数) ==> 新的方法
    对于 fun(a,b,c=None)这种方法，暂时没找到如何只设置b的方法

from XXX import *
---
    控制*时，需要在脚本中添加
    __all__ = (XXX,XXX) # 此时improt * 时只会导入 XXX,XXX

类方法，静态方法，普通方法
---
    1.普通方法 第一个参数是self(对象)
    2.类方法 第一个参数是cls(类)
    3.静态方法 没有第一个参数

    从第一个参数的默认命名规范上就可以基本
    猜出这几个方法的不同之处

    1.普通方法需要新建一个实例，用obj.fun调用
    2.@classmethod @staticmethod 类方法和静态
    方法即可以通过类直接调用， 也可以通过实例
    调用,需要注意一点，当他们与普通方法重名的
    时候会覆盖普通方法。
    3.类方法类似java和c++类里面的静态方法


python私有方法
---

    class Dog
        def __method(self):
            pass

    Dog()._Dog__method() # 依然可以调用

异常
---
    抓到的异常的[0] 为异常信息message
    except RuntimeError as ex:
        print ex[0]

python解析
---
    以前只知道有里表解析，好吧涨见识了

    列表解析 []
    ---
    c = [(i,j) for i,j in enumerate(range(5))]
    ==> [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

    字典解析 {key:value XXXX}
    ---
    c = {i:j for i,j in enumerate(range(5))}
    ==> {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

    集合解析 {value XXXX}
    ---
    c = {i for i,j in enumerate(range(5))}
    ==> set([0, 1, 2, 3, 4])


property
---
    property(fget=None, fset=None, fdel=None, doc=None)

    类里面用property装饰器的时候，如果不加参数
    就是get,加的话一般是设置getter/setter,
    注意先get,后set

__getattr__ __getattribute__ getattr
---
    __getattribute__  # 只用户新式类(继承自object),只要有任何属性访问，
    就会调用
    __getattr__  # 只有在不包含某个属性的时候才会被调用，也就是说
    是在__getattribute__发生AttributeError之后才会调用

    getattr  # 有这么一个解释 
             # You use __getattr__ to define how to handle attributes that are not found 
             # and 
             # getattr to get the attributes 
             # 可见 getattr与__getattribute__类似

__setattr__的递归问题
---
    __setattr__会在每次进行赋值操作的时候被调用，
    即 self.foo = bar 这样会导致递归
    解决的办法是使用self.__dict__['foo'] = bar
    新式类使用 object.__setattr__(self, item, value)

向文件添加一行 print
---
    http://www.python.org/dev/peps/pep-0214/
    print >> fileobj, "line str"
    PEP 214 http://www.python.org/dev/peps/pep-0214/

python cook
---
    collection.deque rotate 列表旋转
        q = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        q.rotate(2)  # -> deque([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])


    sorted sort key
        里面有个key=XXX参数，使用这个参数时会在第一次比较的时候
        应用这个方法，比在cmp里面使用一些方法处理要快，因为cmp每次
        比较的时候都会调用一次

        In [32]: sorted("bqwDAdasf",key=str.lower)
        Out[32]: ['A', 'a', 'b', 'D', 'd', 'f', 'q', 's', 'w']

    operator
        attrgetter,itemgetter是取出指定某元素的好方法

        attrgetter 这个方法是取某个属性，类似object.getattr(obj,attr)
        不同的是attrgetter先将attr取出来做回调，obj后来再传

        class attrgetter(__builtin__.object)
         |  attrgetter(attr, ...) --> attrgetter object
         |  
         |  Return a callable object that fetches the given attribute(s) from its operand.
         |  After, f=attrgetter('name'), the call f(r) returns r.name.
         |  After, g=attrgetter('name', 'date'), the call g(r) returns (r.name, r.date).
         |  After, h=attrgetter('name.first', 'name.last'), the call h(r) returns
         |  (r.name.first, r.name.last).

        itemgetter 则是取数组指定下表

        class itemgetter(__builtin__.object)
         |  itemgetter(item, ...) --> itemgetter object
         |  
         |  Return a callable object that fetches the given item(s) from its operand.
         |  After, f=itemgetter(2), the call f(r) returns r[2].
         |  After, g=itemgetter(2,5,3), the call g(r) returns (r[2], r[5], r[3])

groupby的用法
---
    groupby与sql的groupby不太一样，返回的k,v中的v比较特别，
    groupby(iter,func),当func的值改变的时候，groupby认为是另一个
    分组:
        groupby: [1,2,2,3,1] --> [(1,iter),(2,iter),(3,iter),(1,iter)]
        有两点和sql以及想想的可能不同
            上例中最后诡异的1,
            上例中除了最后一个每个iter是空的
        groupby: [1,1,2,2,3] --> [(1,iter),(2,iter),(3,iter)]

    因此使用groupby之前必须先排序，而且排序的规则(sorted的key)
    就是groupby中的func,参考代码如下

    # -*- coding: utf-8 -*-
    from itertools import groupby
    from operator import attrgetter
    from collections import defaultdict


    class Model(object):
        def __init__(self, id):
            super(Model, self).__init__()
            self.id = id
        def __unicode__(self):
            return unicode(self.id)

    test = []

    for i in xrange(5):
        test.append(Model(i))

    for i in xrange(10):
        test.append(Model(i))

    # 可以修改此处，直接groupby不排序

    keyfunc = attrgetter('id')
    test = sorted(test, key=keyfunc)
    gb = groupby(test, keyfunc)

    result = defaultdict(list)

    for k, g in gb:
        result[k].extend(list(g))

##python部分脚本

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

##python部分资源|文章

文章
---
    # Python 开发者应该知道的 7个开发库
    http://www.oschina.net/question/12_78983

    # Python Best Practice
    http://stevenloria.com/python-best-practice-patterns-by-vladimir-keleshev-notes/?utm_content=buffer98fb1&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer

    # python协程，超棒的帖子各种例子
    http://www.dabeaz.com/coroutines/

学习脚本 python_koans
---
https://github.com/gregmalcolm/python_koans
