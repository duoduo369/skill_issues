npm issue
====

安装
---

用apt-get 安装nodejs的时候会有问题，就是命令行里面没有node这个指令，
而npm安装又会用到，因此先正确安装node

安装node到官网下载对应系统的包

    比如下载node-v0.10.26-linux-x64.tar.gz到 /home/duoduo/download

    sudo cd /usr/local && tar --strip-components 1 -xzf \
        /home/duoduo/download/node-v0.10.26-linux-x64.tar.gz

安装cnpm加速,国内的人使用npm有的时候是一种煎熬

    可以直接
    sudo npm install -g cnpm

    或者使用阿里云
    sudo npm install -g cnpm --registry=http://registry.npm.taobao.org


brunch issue
===

安装
---
    需要安装npm
    npm install -g brunch

使用
---
    brunch new
    # 运行之后会报错，然后他会给你提示让选择一个模板,我选择chaplin这个
    brunch new gh:paulmillr/brunch-with-chaplin 目标文件路径
    # 如果不加后面的文件路径的话，默认以当前文件夹，需要为空

    构建
    brunch build
    brunch build --production  # 生产环境

    本地服务器浏览
    brunch watch --server # 会按照开发环境来编译，js,css不会压缩
    brunch watch --server --production  # 会按照生产环境来编译，
                                        # js,css会压缩

bower issue
===

https://github.com/bower/bower

安装
---
    之前需要先安装npm

安装package后自动保存到bower.json
---
    例如安装jquery
    bower install jquery --save
