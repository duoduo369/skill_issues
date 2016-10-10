redis相关issue
===

连接远程机器
---
redis-cli -h host -p port

本机各个redis命令可以执行多少次
---
redis-benchmark -c 1 -q # 1为1个client -q是简化输出结果
单客户端一般性能为这个命令的50%~60%

redis集合命名
---

redis不是关系型的数据库，但是可以通过某些命名规则在当做数据库用

例如:

    类名:id --> 来创建对应的集合

scan遍历元素
---
[scan](http://redis.io/commands/scan)
类似命令: SSCAN, HSCAN, ZSCAN

sscan每次执行会返回两个值, 一个时下次scan的cursor位置，一个时这次scan到接结果

```
Since these commands allow for incremental iteration, returning only a
small number of elements per call, they can be used in production
without the downside of commands like KEYS or SMEMBERS that may block
the server for a long time (even several seconds) when called against
big collections of keys or elements.

However while blocking commands like SMEMBERS are able to provide all the elements that are part of a Set in a given moment, The SCAN family of commands only offer limited guarantees about the returned elements since the collection that we incrementally iterate can change during the iteration process.
```

避免使用keys, smembers官方解释是这些命令会block redis, 而且sscan注意加上count这玩意儿并不太靠谱
当然keys, smembers这些可以保证你取值的时候数据一定是当前快照，sscan取值时如果数据有了
变动可能会跟想象的不一样，看业务场景。

可以看到,count这个东西有的时候redis并不遵循
```
The default COUNT value is 10.
When iterating the key space, or a Set, Hash or Sorted Set that is big
enough to be represented by a hash table, assuming no MATCH option is
used, the server will usually return count or a bit more than count
elements per call.
When iterating Sets encoded as intsets (small sets composed of just
integers), or Hashes and Sorted Sets encoded as ziplists (small hashes
and sets composed of small individual values), usually all the elements
are returned in the first SCAN call regardless of the COUNT value.
```

```
key = 'table_key'
cur = 0
while True:
    cur, ret = redis.SOME_TABLE.sscan(key, cursor=cur, count=100)
    # some code deal with ret
    if cur == 0:
        return
```

```
从Redis v2.8开始，SCAN命令已经可用，它允许使用游标从keyspace中检索键。对比KEYS命令，虽然SCAN无法一次性返回所有匹配结果，但是却规避了阻塞系统这个高风险，从而也让一些操作可以放在主节点上执行。

需要注意的是，SCAN 命令是一个基于游标的迭代器。SCAN 命令每次被调用之后，
都会向用户返回一个新的游标，用户在下次迭代时需要使用这个新游标作为 SCAN
命令的游标参数，
以此来延续之前的迭代过程。同时，使用SCAN，用户还可以使用keyname模式和count选项对命令进行调整。

SCAN相关命令还包括SSCAN 命令、HSCAN 命令和 ZSCAN
命令，分别用于集合、哈希键及有续集等。
```
