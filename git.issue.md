git相关issue
===

ssh不用输入密码直接push
---
    使用http的git比较烦,每次push需要输入用户名密码

    解决方案：使用ssh的地址，并且在osc@git或者github上加上你机器的公钥 

    自己有服务器的话
    ssh-keygen -t rsa scp ~/.ssh/id*.pub 远程:~/.ssh/authorized_keys 

配置友好的log
---

    git config --global alias.alog "log --all --decorate --graph --color" 

使用 git alog 命令
