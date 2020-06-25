hadoop.md
---

下载
---

    下载tar.gz
    https://archive.apache.org/dist/hadoop/core/
    国内源
    http://mirror.bit.edu.cn/apache/hadoop/common/

本地安装
---

解压后倒入环境变量

    export HADOOP_HOME="/opt/projects/libs/hadoop-2.8.5"
    export PATH="$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin"

观察是否安装正常

    hadoop version

首次使用HDFS, 需要格式化

    hdfs namenode -format
