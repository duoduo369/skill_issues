npm issue
====

安装
---
    # Node Packaged Modules
    # https://npmjs.org/
    # http://stackoverflow.com/questions/16302436/install-nodejs-on-ubuntu-12-10
    sudo apt-get install python-software-properties python g++ make
    sudo add-apt-repository ppa:chris-lea/node.js
    sudo apt-get update
    sudo apt-get install nodejs

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
