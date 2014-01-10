python的相关问题
=====

学习脚本 python_koans
---
https://github.com/gregmalcolm/python_koans

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

    用法：pep8 XXX.py，就会告诉你哪些行不符pep8的什么规范
          autopep8 XXX.py, 就会直接在shell中显示符合pep8的脚本的代码

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

用交互模式执行脚本
---
python -i XXX.py
ipython -i XXX.py

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

同行间隔字符串会自动连接
---
    'Hello, world' == "Hello" ", " "world" 

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
