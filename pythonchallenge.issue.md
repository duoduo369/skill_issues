python changle issue
===
提示，查看前一关解决方案将url中的pc->pcc

0
---
    http://www.pythonchallenge.com/pc/def/0.html
    2 ** 38 = 274877906944

    Hint: try to change the URL address
    -->
    http://www.pythonchallenge.com/pc/def/274877906944.html

1
---
   everybody thinks twice before solving this.
   k -> m
   o -> q
   e -> g
   给出的提示又都是小写
   可以看出规律，
   s = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq
   ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr
   gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc
   spj.'''
   import string
   from = string.ascii_lowercase
   to = from[2:] + from[:2]
   table = string.maketrans(from, to)
   print string.translate(s, table)
   -->
   Out[21]: "i hope you didnt translate it by hand. thats what computers
   are for. doing it in by hand is inefficient and that's why this text
   is so long. using string.maketrans() is recommended. now apply on the
   url."

   In [22]: string.translate('map', table)
   Out[22]: 'ocr'

   http://www.pythonchallenge.com/pc/def/ocr.html

2
---
    recognize the characters. maybe they are in the book, 
    but MAYBE they are in the page source.
    源代码里面有很大一段的注释
    find rare characters in the mess below:
    from collections import Counter

    In [55]: Counter(s)
    Out[55]: Counter({')': 6186, '@': 6157, '(': 6154, ']': 6152, '#':
    6115, '_': 6112, '[': 6108, '}': 6105, '%': 6104, '!': 6079, '+':
    6066, '$': 6046, '{': 6046, '&': 6043, '*': 6034, '^': 6030, '\n':
    1219, 'a': 1, 'e': 1, 'i': 1, 'l': 1, 'q': 1, 'u': 1, 't': 1, 'y':
    1})

    rare --> aeilquty --> equality

3
---
    标题是re，明显是正则,hit又提示一个小写字母在三个大写中间
    继续看源码，里面又有一堆注释
    import re
    p = re.compile('[A-Z]{3}[a-z][A-Z]{3}')
    m = p.search(s)
    m.group() --> WDZjUZM
