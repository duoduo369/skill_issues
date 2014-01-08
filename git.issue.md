git相关issue
===

git书籍
---
progit http://git.oschina.net/progit/

zsh增强git
---
    https://github.com/olivierverdier/zsh-git-prompt

    配置方法
    ---
    新建文件夹 ~/.zsh/git-prompt
    将项目里面的 gitstatus.py  zshrc.sh cp到这个文件夹里
    编辑你的 zshrc

    # source  ~/.zsh/git-prompt/zshrc.sh 
    source /home/duoduo/.zsh/git-prompt/zshrc.sh 
    PROMPT='%B%m%~%b$(git_super_status)%# '
    

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
    git config --global alias.br branch  # 注意 后面命令的引号可以不写
    git config --global alias.cm commit

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

fast-forwards
---
fast-forwards指有直接从属关系(log --graph上是一条直线)的分支

演示图
    ——————*——————*——————*——————  # fast-forwards 一条直线

             —————*——
            /        \ 
    ————*——— ——*————————*——    # none fast-forwards
        

git log
---
    git log -p [-数字] #加p显示diff
    git log --stat [-数字] #显示曾改行数

git reflog
---
    git 的引用日志命令

取消对文件的修改
---
    push之前
    在git status中都会有提示
    git reset HEAD <file>  # 将add的文件从暂存区移除
    git checkout -- <file> # 将工作区域文件的修改撤销掉

标签
---
    git tag #显示标签
    git tag -a v0.1 -m "标签描述 -m和描述可以不写"
    git push origin v0.1  # 手动push标签才可以push到服务器 
    git push origin --tags # push所有标签

git自带web
---
    需要安装 lighttpd
    git instaweb  # 启动
    git instaweb --stop # 停止
