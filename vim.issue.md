vim相关issure
===

请下载 janus 节省不必要的配置时间

https://github.com/carlhuda/janus

自定义的配置放在~/.vimrc.after里面

以下的很多操作默认使用janus安装的插件

例如快速跳转\\w \\b，注释\cc,格式化等等

tab
---
    python可能4个空格缩进，ruby或者别的一些规定2个空格
    下面是关于空格我的~/.vimrc.after,默认tab是4个空格(pythoner),如果写coffee的
    话默认两个
    
    set tabstop=4       " A four-space tab indent width is the prefered coding style
                    " for Python (and everything else!), although of course some
                    " disagree. This page generally assumes you want 4-space
                    " indents.

    set shiftwidth=4    " This allows you to use the < and > keys from VIM's visual
                        " (marking) mode to block indent/unindent regions

    set smarttab        " Use the "shiftwidth" setting for inserting <TAB>s instead
                        " of the "tabstop" setting, when at the beginning of a
                        " line. This may be redundant for most people, but some
                        " poeple like to keep their tabstop=8 for compatability
                        " when loading files, but setting shiftwidth=4 for nicer
                        " coding style.

    set expandtab       " expandtab    et    Insert spaces instead of <TAB>
                        " character when the <TAB> key is pressed. This is also
                        " the prefered method of Python coding, since Python is
                        " especially sensitive to problems with indenting which can
                        " occur when people load files in different editors with
                        " different tab settings, and also cutting and pasting
                        " between applications (ie email/news for example) can
                        " result in problems. It is safer and more portable to
                        " use spaces for indenting.

    set softtabstop=4   " softtabstop=4    sts    People like using real tab
                        " character instead of spaces because it makes it easier
                        " when pressing BACKSPACE or DELETE, since if the indent
                        " is using spaces it will take 4 keystrokes to delete
                        " the indent. Using this setting, however, makes VIM see
                        " multiple space characters as tabstops, and so <BS> does
                        " the right thing and will delete four spaces (assuming
                        " 4 is your setting).

    set autoindent      " autoindent    ai    Very painful to live without this
                        " (especially with Python)! It means that when you press
                        " RETURN and a new line is created, the indent of the new
                        " line will match that of the previous line.

    autocmd FileType coffee setlocal tabstop=2 shiftwidth=2 softtabstop=2


可视化
---

行级别 shift + v
列级别 ctrl + v

可视化是很重要的一个部分，还记得你在记事本里面用鼠标选中某些文字，
然后复制粘贴么？在vim里面只要ctrl + v 然后拉动 h l
等选中文字，y可以复制选中的文字，x可以删除选中的文字,大写I进行插入
按Esc之后会有惊喜(多行注释常用)

打开tab,来回切换
---

:tabedit path

切换ctrl + pageup/pagedown

tab映射,让你的vim变的更加方便
----
有了tab功能，并且可以方便的切换，vim的易用性显得更高了。

http://www.douban.com/group/topic/23129658/

    ctrl + t 打开新tab
    ctrl + h/l 来回切换tab
    ctrl + c 关闭tab


    :map <C-t> :tabedit ./^D

    :map <C-h> :tabp<CR>

    :map <C-l> :tabn<CR>

    :map <C-c> :tabclose<CR>

打开tab list
---
    \t 
    当tab有7 8个的时候，可能感觉移动不方便，可以直接打开tab
    list跳到某个tab去.不过配置了ctrl + h/l之后移动是很简单的事情。

迅速找到并打开当前vim文件夹下的文件
---

    ctrl + p 

例如:
    文件目录如下,你正在编辑 /home/duoduo/proj/A.txt:

    /home/duoduo/proj/A.txt
    /home/duoduo/proj/B.txt
    /home/duoduo/proj/test/A.txt
    /home/duoduo/proj/test2/B.txt
    /home/duoduo/proj/test2/B/A.txt

    当按下ctrl + p
    的时候，vim下面会出现一个条，如果你输入b,会出现下面这几个路径，可以迅速选择打开文件，非常方便。
    /home/duoduo/proj/B.txt
    /home/duoduo/proj/test2/B.txt
    /home/duoduo/proj/test2/B/A.txt

迅速打开# 路径的文件
---

    gf 

    如果你的文件中有这么一个路径

    # /home/duoduo/proj/B.txt

    将光标移动到/home/duoduo/proj/B.txt上的任意一个字符上，按下gf即可打开这个文件，超快的。

    这个非常常用，无论你是什么格式的文件

滚屏
---
    ctrl + u 上滚半屏
    ctrl + d 下滚半屏
    ctrl + f 上滚一屏
    ctrl + b 下滚一屏

查找移动光标
---
    / 加单词 回车之后 单词会高亮
    例如 /word<CR>
    文章中的word都会高亮，按n可以条到下一个,N可以找到上一个

    \hs 可以关闭或者打开由 / 查找带来的单词高亮问题

    同一行下f字符可以直接跳到字符前的位置，F是向前搜索
    同一行下t字符（to的意思）可以直接跳到字符后的位置，T是向前搜索
    f和t类的都可以使用; ,在重复之前的命令


在行上添加或者减少缩进
---

    向左 shift + < 
    向右 shift + >

    html python  markdown等需要缩进的地方非常常用.

一些之前少用的编辑小命令
---

    替换字符，并且依然在normal模式
        小写r,换一个字
        大写R,从光标位置开始替换后面的字符

        知道这个命令之前都是x i 插入 Esc按这4次的。

    D = d$
    C = c$
    s 修改一个字 = xa
    S = cc

    . 重复上一个命令 当使用 < 缩进行的时候常用


移动当前行
---

    下移ctrl + j
    下移ctrl + k

    可以用可视模式移动一个块

合并两行
--- 

    大写J（shift + j）
    可以用可视模式合并一个块

快速跳转单词
---
\\w 向后跳转
\\b 向前跳转

例如vim 编辑a文章，然后你用ctrl+p跳到了别的地方，跳回a的方法

    ctrl + shift + 6

记录位置，迅速跳转
---

s指任意字母 S是大写,例如ma 用a记录下一个位置,然后光标随意移动,
'a即可跳回。大写的话即使你在别的tab下也可以很方便的跳回这个位置。

记录 m{Ss}
跳回 '{Ss}

另外 当使用G跳转的时候，跳转点会自动mark，''即可跳回


注释
---
添加\cc
取消\cu

经常与shift+v 可视块一起使用


粘贴模式
---

按F4进入粘贴模式，这样要粘贴的文字的格式就会被保留下来。

注意复制粘贴的时候需要先进入insert模式

打开文件时(:tabedit 或者ls等)查看目录下文件
---

ctrl + d

snippets
---
https://github.com/honza/vim-snippets/tree/master/snippets


常用的片段
---

###html常用

https://github.com/honza/vim-snippets/blob/master/snippets/html.snippets

    空格
    snippet nbs
            &nbsp;

    键值对
    snippet attr
            ${1:attribute}="${0:property}"
    snippet attr+
            ${1:attribute}="${2:property}" attr+

    snippet .
            class="${1}"
    snippet #
            id="${1}"
    snippet alt
            alt="${1}"
    snippet charset
            charset="${1:utf-8}"

    snippet height
            height="${1}"
    snippet href
            href="${1:#}"
    snippet rel
            rel="${1}"
    snippet src
            src="${1}"
    snippet title=
            title="${1}"
    snippet width
            width="${1}"

####Elements

都可以直接元素类型加. #


    snippet a
            <a href="${1:#}">${0:$1}</a>
    snippet a.
            <a class="${1}" href="${2:#}">${0:$1}</a>
    snippet a#
            <a id="${1}" href="${2:#}">${0:$1}</a>
    snippet a:ext
            <a href="http://${1:example.com}">${0:$1}</a>

input:hidden 等可以直接指定type

####jquery

https://github.com/honza/vim-snippets/blob/master/snippets/javascript-jquery.snippets

一般直接写方法名


####python

https://github.com/honza/vim-snippets/blob/master/snippets/python.snippets

添加自己的issue

在janus里面这个插件在~/.vim/janus/vim/tools/vim-snippets/snippets下

例如：当写zarkpy继承model的时候就可以新建以下的模板,在.py文件中输入clm按下tab就会补全

    snippet clm
        class ${1:ClassName}(Model):
            table_name = '$1'
            column_names = [${2}]

            template = \ 
                ''' CREATE TABLE {$table_name} (
                    {$table_name}id int unsigned  not null auto_increment,
                    ${3}
                    primary key ({$table_name}id)
                )ENGINE=InnoDB; ''' 
            ${0}

单词大小写转化
---
    1.选中单词 ctrl + v  w 
    转换大小写 gu(小写)    gU(大写)
    2. guw gUw

vim 编译coffeescript
---
    vim的一个插件
    https://github.com/kchmck/vim-coffee-script

    安装
    Install pathogen.vim into ~/.vim/autoload/ 
    http://www.vim.org/scripts/script.php?script_id=2332

    Enable pathogen in your vimrc. Here's a bare-minimum vimrc that enables all the features of vim-coffee-script:

        call pathogen#infect()
        syntax enable
        filetype plugin indent on
        
        :map <F3> :CoffeeCompile vert<CR>  # 安F3编译 并且右边显示

    Create the directory ~/.vim/bundle/:

    mkdir ~/.vim/bundle
    Clone the vim-coffee-script repo into ~/.vim/bundle/:

    git clone https://github.com/kchmck/vim-coffee-script.git ~/.vim/bundle/vim-coffee-script/

~/.vimrc.after
---

    set tabstop=4       " A four-space tab indent width is the prefered coding style
                        " for Python (and everything else!), although of course some
                        " disagree. This page generally assumes you want 4-space
                        " indents.

    set shiftwidth=4    " This allows you to use the < and > keys from VIM's visual
                        " (marking) mode to block indent/unindent regions

    set smarttab        " Use the "shiftwidth" setting for inserting <TAB>s instead
                        " of the "tabstop" setting, when at the beginning of a
                        " line. This may be redundant for most people, but some
                        " poeple like to keep their tabstop=8 for compatability
                        " when loading files, but setting shiftwidth=4 for nicer
                        " coding style.

    set expandtab       " expandtab    et    Insert spaces instead of <TAB>
                        " character when the <TAB> key is pressed. This is also
                        " the prefered method of Python coding, since Python is
                        " especially sensitive to problems with indenting which can
                        " occur when people load files in different editors with
                        " different tab settings, and also cutting and pasting
                        " between applications (ie email/news for example) can
                        " result in problems. It is safer and more portable to
                        " use spaces for indenting.

    set softtabstop=4   " softtabstop=4    sts    People like using real tab
                        " character instead of spaces because it makes it easier
                        " when pressing BACKSPACE or DELETE, since if the indent
                        " is using spaces it will take 4 keystrokes to delete
                        " the indent. Using this setting, however, makes VIM see
                        " multiple space characters as tabstops, and so <BS> does
                        " the right thing and will delete four spaces (assuming
                        " 4 is your setting).

    set autoindent      " autoindent    ai    Very painful to live without this
                        " (especially with Python)! It means that when you press
                        " RETURN and a new line is created, the indent of the new
                        " line will match that of the previous line. 
    set textwidth=79

    autocmd FileType coffee setlocal tabstop=2 shiftwidth=2 softtabstop=2

    set noswapfile

    :map <F1> :wa
    :! /usr/local/bin/launch-curr.py %:p 


    :map <F2> :! /usr/local/bin/error-curr.py %:p 

    :map <F3> :CoffeeCompile vert<CR>

    :map <C-t> :tabedit ./
    :map <C-n> :tabnew ./
    :map <C-h> :tabp<CR>
    :map <C-i> :tabn<CR>
    :map <C-c> :tabclose<CR>

    :imap <C-l> <C-x><C-o>

    call pathogen#infect()
    syntax enable
    filetype plugin indent on
