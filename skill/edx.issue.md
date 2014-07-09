edx issure
===

[edx](https://github.com/edx/edx-platform)、[configuration](https://github.com/edx/configuration) 这是edx的开源平台

其中会有各种配置问题，安装问题，vagrant问题

vagrant
===

vagrant up 时会下载某个box,box 会下载到本地 ~/.vagrant.d/boxes,
这个过程巨慢,建议下载前看一下 Vagrantfile config.vm.box_url的东西有多大，
你可以先从网上用下载器down下来，并且存入移动硬盘之类的，再解压到~/.vagrant.d/boxes
下,以后其他小机器需要的时候直接拿硬盘拷过去即可。


configuration
===

configuration 启动官网base devstack
---

1.安装依赖, 注意到官网下载vagrant、vitualbox的deb安装包

  sudo apt-get install nfs-kernel-server

  pip install -r requirements.txt

2.启动vagrant

  cd vagrant/base/devstack
  vagrant up
