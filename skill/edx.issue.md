edx issure
===

[edx](https://github.com/edx/edx-platform)、[configuration](https://github.com/edx/configuration) 这是edx的开源平台

其中会有各种配置问题，安装问题，vagrant问题

vagrant
===

保存box
---
box下载方式有两种：

1. vagrant up

    vagrant up 时会下载某个box, box 会下载到本地 ~/.vagrant.d/boxes,
    这个过程巨慢,建议下载前看一下 Vagrantfile config.vm.box_url的东西有多大，
    你可以先从网上用下载器down下来，并且存入移动硬盘之类的，再解压到~/.vagrant.d/boxes
    下,以后其他小机器需要的时候直接拿硬盘拷过去即可。

2. 直接通过url下载

    下载下的东西为XXX.box
    添加命令为 vagrant box add my-box downloaded.box
    这时候在~/.vagrant.d/boxes下就会有my-box 与方法一就一样


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

problem:

    The guest machine entered an invalid state while waiting for it
    to boot. Valid states are 'starting, running'. The machine is in the
    'poweroff' state. Please verify everything is configured
    properly and try again.

    If the provider you're using has a GUI that comes with it,
    it is often helpful to open that and watch the machine, since the
    GUI often has more helpful error messages than Vagrant can retrieve.
    For example, if you're using VirtualBox, run `vagrant up` while the
    VirtualBox GUI is open.

这个问题可能和以下几点有关：
1. 用了虚拟机，就是说是在虚拟机中搞的，例如本机windows 7,vmware ubuntu 配置edx
2. BOIS里面的 Intel Virtual Enable
3. 可以启动下VirtualBox 发现西面有两个警告，包括内存超过物理机的50%,还有一个什么视频内存小于9M
   这个先在VirtualBox GUI调节一下内存(system)去掉这些警告尝试启动一下。成功的话在配置文件Vagrantfile
   里面调整下Memeory和cpu参数，将Memeory调整小，cpu调节为1试试
