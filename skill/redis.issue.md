redis相关issue
===

本机各个redis命令可以执行多少次
---
redis-benchmark -c 1 -q # 1为1个client -q是简化输出结果
单客户端一般性能为这个命令的50%~60%

redis集合命名
---

redis不是关系型的数据库，但是可以通过某些命名规则在当做数据库用

例如:

    类名:id --> 来创建对应的集合
