python的相关问题
=====

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
