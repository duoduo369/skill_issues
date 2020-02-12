基本安装
---

去官网下载一个桌面，注册账号登录


docker image
---
如果 docker 镜像下载过于缓慢，可以让同伴导出镜像，自己导入

    导出
    docker save -o my_ubuntu_v3.tar runoob/ubuntu:v3
    docker save ubuntu:load>/root/ubuntu.tar

    导入
    docker load<ubuntu.tar
