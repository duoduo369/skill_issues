git相关issue
===

git书籍
---
progit http://git.oschina.net/progit/

git 配置
---
    查看配置列表
    git config --list


    用户名邮箱
    ---
    git config --global user.name yangyang
    git config --global user.email yangyang@admaster.com.cn

    颜色
    ---
    git config --global color.branch 'auto'
    git config --global color.ui 'auto'
    git config --global color.status 'auto'

    配置友好的log
    ---

    git config --global alias.alog "log --all --decorate --graph --color" 

    其他的别名
    ---
    git config --global alias.st 'status'
    git config --global alias.co 'checkout'

ssh不用输入密码直接push
---
    使用http的git比较烦,每次push需要输入用户名密码

    解决方案：使用ssh的地址，并且在osc@git或者github上加上你机器的公钥 

    自己有服务器的话
    ssh-keygen -t rsa scp ~/.ssh/id*.pub 远程:~/.ssh/authorized_keys 




把master移动到HEAD
---
    有的时候你会不小心在一个空白节点提交，这时候只要将master移动到head即可
    git branch -f master # 

git diff
---
    git diff 
    查看尚未暂存的文件更新了哪些部分 (add后又修改了的文件,也就是说如果
    修改之后add *，则没有东西可以显示，如果想看到这些add的diff,
    加--cached 参数)

    git diff --cached
    已经暂存起来的文件和上次提交时的快照之间的差异
    ---

    diff --git a/b.py b/b.py   # b.py前面有a和b两个字母，是a,b状态的标记
    index 40a96af..3c4d5b7 100644  # index 是diff两个指纹的前几位用..隔开
    --- a/b.py   #  - 是 a状态
    +++ b/b.py   #  + 是 b状态
    @@ -1,4 +1,5 @@  # -1,4 a状态从第一行开始向下4行，  +1,5
    b状态从第一行开始向下5行

git commit
---
    git commit -m "简短注释"
    git commit     #长注释，第一行写简单介绍，空一行，下面写详细说明

    #当提交之后发现漏了文件之后
    #先git add 忘记的文件,然后用amend参数
    git commit --amend

git log
---
    git log -p [-数字] #加p显示diff
    git log --stat [-数字] #显示曾改行数
