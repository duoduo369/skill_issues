入门推荐书籍
---

[Docker 从入门到实践](https://yeasy.gitbook.io/docker_practice/)


基本安装
---

去官网下载一个桌面，注册账号登录


国内 docker 镜像加速
----

编辑文件/etc/docker/daemon.json，若没有该文件则手动创建, mac 在 `~/.docker/daemon.json`

		{

			"registry-mirrors": [
				"https://registry.docker-cn.com",
				"http://hub-mirror.c.163.com",
				"https://docker.mirrors.ustc.edu.cn"
			]
		}


service docker restart

mac直接点击docker上面的restart按钮


docker image
---
如果 docker 镜像下载过于缓慢，可以让同伴导出镜像，自己导入

    导出
    docker save -o my_ubuntu_v3.tar runoob/ubuntu:v3
    docker save ubuntu:load>/root/ubuntu.tar

    导入
    docker load<ubuntu.tar


通过 Dockerfile 构建
---
    docker build -t="duoduo3369/etl" .


启动 shell
---

    docker run -i -t duoduo3369/etl /bin/bash


cp docker 文件
---

对应image需要启动起来

    docker run -i -t 01e651890836 /bin/bash

    docker ps # 找到对应的 CONTAINER ID
    docker cp CONTAINER ID:/opt/xx.zip .


查看docker存储占用
---

    docker system df


删除悬虚镜像
---
    docker image ls -f dangling=true 后显示出来的 none none的镜像为玄虚镜像，可以执行下面的命令批量删除

    docker image prune


docker run
---

nginx:

    docker run -d -p 80:80 --name nginx nginx


docker-compose up异常
---

https://github.com/docker/for-mac/issues/3785

2.3.0.4 删除 ~/.docker/config.json 里面的的

    "credsStore" : "desktop",
