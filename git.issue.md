git相关issue
===

git书籍
---
progit http://git.oschina.net/progit/

http://sethrobertson.github.io/GitBestPractices/

zsh增强git
---
    zsh bug
        git show HEAD^
        ^显示找不到 使用\^转义或者引号扩起来
        git show HEAD\^    or   git show 'HEAD^'

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
    git config --global alias.stash-unapply '!git stash show -p | git
    apply -R'

ssh不用输入密码直接push
---
    使用http的git比较烦,每次push需要输入用户名密码

    解决方案：使用ssh的地址，并且在osc@git或者github上加上你机器的公钥

    自己有服务器的话
    ssh-keygen -t rsa scp ~/.ssh/id*.pub 远程:~/.ssh/authorized_keys

修改所有commit的作者信息
---
    git filter-branch --commit-filter 'export GIT_AUTHOR_NAME="duoduo369" ;
    export GIT_AUTHOR_EMAIL=duoduo3369@gmail.com; git commit-tree "$@"'

    git filter-branch --commit-filter 'export GIT_AUTHOR_NAME="duoduo3_69" ;
    export GIT_AUTHOR_EMAIL=duoduo3_69@163.com; git commit-tree "$@"'

git ssh_key 用xclip粘贴
---
    xclip -sel clip < ~/.ssh/id_rsa.pub

    或者在zsh里面添加alias
    alias xclip='xclip -selection clipboard'
    cat ~/.ssh/id_rsa.pub | xclip


把master移动到HEAD
---
    有的时候你会不小心在一个空白节点提交，这时候只要将master移动到head即可
    git branch -f master #

git branch
---
    git branch --merged# 查看分支的直接上游

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

git remote
---
    git remote add 分支名 地址 # 添加分支
    git remote -v # 查看分支
    git remote show 分支名 # 查看分支状态

git 抓回远程分支
---
    git checkout master
    git pull
    # 上面两不是重点
    git checkout -b 分支名 远程分支名

git 删除远程分支
---
    git push origin --delete <branchName>
    git push origin :<branchName>

fast-forwards
---
fast-forwards指有直接从属关系(log --graph上是一条直线)的分支

演示图
    ——————*——————*——————*——————  # fast-forwards 一条直线

             —————*——
            /        \
    ————*——— ——*————————*——    # none fast-forwards


git rebase
---
    在开发中有下面的分支结构 master,develop,feature/f1,feature/f2
    因改保持master,develop是一条直线的，

    ———*—————*—— (master)
                \
                 ——*—————*————(develop)
                    \
                     —*—————*————(feature/f1)
    假设你在开发特性f1,commit后到如图的节点状态(注意不提交),
    可以看到develop是领先与你的分支的，这时候需要checkout 到
    develop 分支，pull一把，保证develop是最新状态，然后checkout
    回自己的feature/f1,这个时候git rebase develop

    ———*—————*—— (master)
                \
                 ——*—————*————(develop)————*(feature/f1)

    git的节点图变成这个样子了，发现feature/f1会到develop后面，
    变成一条直线，没有以前merge的各种合并状态，这个时候
    git push origin feature/f1, 然后你可以发起一个merge-request
    让你的管理员合并你的feature/f1分支和develop分支了，这时候
    develop是fast-forward

git log
---
    git log -[数字] 显示几条log
    git log -p [-数字] #加p显示diff,展开commit
    git log --stat [-数字] #显示曾改行数
    gitk 图形界面查看git log的节点情况 需要安装

git stash
---
    储藏修改
    git stash
    git stash list 查看stash列表
    git stash apply 应用储藏
    git stash show -p | git apply -R 取消应用
    git stash clear 清除储藏

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

git 和python
---
    pep8 检查代码风格

    在git项目下的.git/hooks添加pre-commit,chmod 755 pre-commit
    https://gist.github.com/lentil/810399

    pyflakes检查代码语法

