工具增强
====


编辑器vim
----

vim 直接安装janus,节省安装插件时间

https://github.com/carlhuda/janus

常用 ctrl + p
/ + n
gf (例如有个井号注释地址 # /home/duoduo/file.js,在# 后的路径按gf，会打开这个文件)

grep增强ack
---

安装ack

http://brooky.cc/2012/09/28/ack-for-%E5%B7%A5%E7%A8%8B%E5%B8%AB%E7%94%A8%E7%9A%84-grep/

http://beyondgrep.com/

ps:janus里面已经安装,使用方法:Ack 


shell增强
---

安装zsh,并且配置zshrc

shell 操作命令 生成gif
---
    https://github.com/icholy/ttygif
    http://www.oschina.net/p/ttyrec
    http://my.oschina.net/hanjiafu/blog/155189

    默认的源应该装不上 我换了soho的源就ok了

    按照ttygif里面的方式make完后，将ttygif,和concat.sh cp 到/usr/bin下
    sudo cp make的路径/{ttygif,concat.sh} /usr/bin

    ttyrec tmp # 开始录像 
    # 进行录像命令...
    # 点击Ctrl+D 或者输入exit结束录像
    ttygif tmp # 生成gif贞
    concat.sh terminal.gif # 生成gif图片 
