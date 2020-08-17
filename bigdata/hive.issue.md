hive
===

下载
---

    https://archive.apache.org/dist/hive/

    国内源
    https://mirror.bit.edu.cn/apache/hive/


本地安装
---

解压后导入环境变量

    export HIVE_HOME="/opt/projects/libs/apache-hive-2.3.7-bin"
    export PATH="$PATH:$HIVE_HOME/bin"

https://cwiki.apache.org/confluence/display/Hive/GettingStarted

		export HADOOP_HOME=<hadoop-install-dir>

		$HADOOP_HOME/bin/hadoop fs -mkdir       /tmp
		$HADOOP_HOME/bin/hadoop fs -mkdir       /user/hive/warehouse
		$HADOOP_HOME/bin/hadoop fs -chmod g+w   /tmp
		$HADOOP_HOME/bin/hadoop fs -chmod g+w   /user/hive/warehouse

配置 metadata

		cp $HIVE_HOME/conf/hive-default.xml.template   $HIVE_HOME/conf/hive-site.xml

添加这几段

		<property>
			<name>system:java.io.tmpdir</name>
			<value>/tmp/hive/java</value>
		</property>
		<property>
			<name>system:user.name</name>
			<value>${user.name}</value>
		</property>

修改 metadata 数据库到 mysql

		<property>
			<name>javax.jdo.option.ConnectionURL</name>
			<value>jdbc:mysql://localhost:3306/hive_metastore</value>
			<description>
				JDBC connect string for a JDBC metastore.
				To use SSL to encrypt/authenticate the connection, provide database-specific SSL flag in the connection URL.
				For example, jdbc:postgresql://myhost/db?ssl=true for postgres database.
			</description>
		<property>
			<name>javax.jdo.option.ConnectionPassword</name>
			<value>hivepassword</value>
			<description>password to use against metastore database</description>
		</property>
		<property>
			<name>javax.jdo.option.ConnectionUserName</name>
			<value>hive</value>
			<description>Username to use against metastore database</description>
		</property>
		<property>
			<name>javax.jdo.option.ConnectionDriverName</name>
			<value>com.mysql.jdbc.Driver</value>
			<description>Driver class name for a JDBC metastore</description>
		</property>


mysql 创建表

		CREATE USER 'hive'@'%' IDENTIFIED BY 'hivepassword';
		create database hive_metastore;
		GRANT ALL ON hive_metastore.* TO 'hive'@'%';
		flush privileges;

将正确版本的mysql-mysql-connector-java.jar 放到 $HIVE_HOME/lib中

初始化metadata表

		schematool -dbType mysql -initSchema

观察是否安装正常

    hive


使用外部表
---

当一个目录下有一堆相同类型的csv时, 似乎需要制定文件夹而不是某个csv，LOCATION默认是hdfs，与hdfs:///testhive 类似

	CREATE EXTERNAL TABLE IF NOT EXISTS hive_test(
		  Id1 STRING, Id2 STRING, Id3 STRING, Name STRING)
		  ROW FORMAT DELIMITED
		  FIELDS TERMINATED BY ','
		  STORED AS TEXTFILE
		  LOCATION '/testhive';

这样可以直接select *


拷贝一个表的内容
---
例如需要拷贝的表为 hive_test

1. 观察表结构

    show create table hive_test;

2. 将第一步的result表名字改成要拷贝的表名创建hive表, 例如 export_hive_test

3. 插入数据

    insert into export_hive_test select * from hive_test;


bash执行hive短句
----

    hive -S -e 'show create table hive_test'

bash通过文件执行sql
---

    hive -f /tmp/hive_test.sql
