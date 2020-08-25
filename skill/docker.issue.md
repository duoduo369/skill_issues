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

    docker run -it 01e651890836 /bin/bash
    docker exec -it 69d1 /bin/bash

    docker ps # 找到对应的 CONTAINER ID
    docker cp CONTAINER ID:/opt/xx.zip .


查看docker存储占用
---

    docker system df


删除悬虚镜像
---
    docker image ls -f dangling=true 后显示出来的 none none的镜像为玄虚镜像，可以执行下面的命令批量删除

    docker image prune


清除所有不在run的container
---

    docker container prune


docker run
---

nginx:

    docker run -d -p 80:80 --name nginx nginx


docker-compose up异常
---

https://github.com/docker/for-mac/issues/3785

2.3.0.4 删除 ~/.docker/config.json 里面的的

    "credsStore" : "desktop",


创建column
---

    docker volume create archer-mysql
    docker volumn ls
    docker volume inspect archer-mysql


创建 network
---

    docker network create -d bridge

docker run挂载git项目
---
cd 到宿主机的git项目中, 例如下面的命令会将当前目录挂载到 /opt/etl, 并且workdir为 /opt/etl

	docker run -it --rm --name etl -v "$PWD":/opt/etl -w /opt/etl duoduo3369/etl /bin/bash

注意，/opt/默认不在mac的分享目录中, 需要按照下面的提示在docker图形界面里面设置一下

docker: Error response from daemon: Mounts denied:
The path /opt/projects/exome/etl
is not shared from OS X and is not known to Docker.
You can configure shared paths from Docker -> Preferences... -> File Sharing.
See https://docs.docker.com/docker-for-mac/osxfs/#namespaces for more info.


k8s
---

mac 安装

根据这个项目来 https://github.com/AliyunContainerService/k8s-for-docker-desktop

!注意，一定要看看自己docker的k8s是哪个版本，在下载这个项目的对应分支去安装
