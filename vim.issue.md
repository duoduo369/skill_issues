vim相关issure
===

请下载 janus 节省不必要的配置时间

自定义的配置放在~/.vimrc.after里面

合并两行
--- 

    大写J（shift + j）

加注释
---
\cc

ctrl+v 可视块,大写I插入

跳回之前编辑的文章
---


例如vim 编辑a文章，然后你用ctrl+p跳到了别的地方，跳回a的方法

    ctrl + shift + 6

记录位置，迅速跳转
---

s指任意字母 S是大写

记录 m{Ss}
跳回 '{Ss}

打开tab,来回切换
---

:tabedit path

切换ctrl + pageup/pagedown

tab映射
----

http://www.douban.com/group/topic/23129658/

    ctrl + t 打开新tab
    ctrl + h/l 来回切换tab
    ctrl + c 关闭tab


    :map <C-t> :tabedit ./^D

    :map <C-h> :tabp<CR>

    :map <C-l> :tabn<CR>

    :map <C-c> :tabclose<CR>

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
