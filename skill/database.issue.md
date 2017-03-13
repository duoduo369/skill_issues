mongo
===

[doc](http://docs.mongodb.org/manual/)

基本用法
---

service mongodb restart

shell中启动 `mongo`

show dbs

use 数据库

help

db

查看表
show collections

查找
db.表.find(条件).limit(n)
find里面第一个dict是查询条件，第二个dict是显示哪些列
db.users.find( { age: { $gt: 18 } }, { name: 1, address: 1 } ).limit(5)

[查询条件](http://docs.mongodb.org/manual/reference/operator/query/#query-selectors)

显示列那边，_id默认为1，其他为0

默认返回20条，有个提示输入it查看更多

mysql
===

基本用法
---

service mysql restart

shell中启动 `mysql -u用户 -p` `mysql`

show databases;

use 数据库;

查看表
show tables;

查找
select * from XXX where xx=xx limit x;

查看mysql使用的是哪个配置文件
---

whichi mysqld
/usr/sbin/mysqld --verbose --help | grep -A 1 'Default options'


mongo可视化工具
---

https://robomongo.org


用explain语法分析mysql语句执行，看是否能命中缓存等
---
就是在正常的sql前面加上explain即可

https://www.sitepoint.com/using-explain-to-write-better-mysql-queries/


海量数据时offset limit的问题
----
即使字段加索引，如果select多个字段时offset依然会很慢，需要分两步走
先把id查出来，然后根据id用in查属性，这是因为id会命中一些filesort
例如

```
select a.id, a.attr1, a.attr2 from my_table as a
where a.attr1 = 'xx'
limit 25000000, 10
```

```
select a.id from my_table as a
where a.attr1 = 'xx'
limit 25000000, 10

select a.id, a.attr1, a.attr2 from my_table as a
where a.id in (刚刚查出来的)
```


