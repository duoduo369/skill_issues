不知道怎么分类的内容
===

最热帖子排名算法
---

    (p – 1) / (t + 2)^1.5

    其中，
    1）p 表示文章得到的投票数，之所以要使用 (p – 1)，应该是想去掉文章提交者的那一票。
    2）(t + 2)^1.5， 这个是时间因子。t 表示当前时间与文章提交时间间隔的小时数。但为什么要加 2 之后再取 1.5 的幂，似乎就没什么道理可言了，也许是个 trial-and-error 的结果吧。

http://www.cnblogs.com/zhengyun_ustc/archive/2010/12/15/amir.html

基于赞成票，反对票的投票算法
---
基于用户投票的排名算法（五）：威尔逊区间

http://www.oschina.net/question/12_45051?sort=time&p=1

unix命令行介绍
---

[the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line)


google搜索某站点内容
---
Google输入 site:站点域名 xxx 值得你拥有


macos 升级导致git不可用
---

    xcode-select --install
    xcode-select: note: install requested for command line developer tools


macos 升级后导致 vagrant不可用
----

    1. 去vagrant官网下载最新vagrant重新安装
    2. 去virtualbox官网下载最新virtualbox重新安装
    3. 启动vagrant他会让跟新插件
    4. vagrant up

    如果不行可能要执行下面的
    * vagrant plugin install vagrant-vbguest
    找到之前的box文件重新添加 vagrant box add def devstack.box

