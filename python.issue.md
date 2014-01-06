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

