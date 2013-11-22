vim相关issure
===

请下载 janus 节省不必要的配置时间

跳回之前编辑的文章
---

ctrl + shift + 6

记录位置，迅速跳转
---

记录 m{Ss}
跳回 '{Ss}

打开tab,来回切换
---

:tabedit path

切换ctrl + pageup/pagedown

tab映射
----

http://www.douban.com/group/topic/23129658/

    :map <C-t> :tabedit ./^D

    :map <C-h> :tabp<CR>

    :map <C-l> :tabn<CR>

    :map <C-c> :tabclose<CR>

粘贴模式
---

按F4进入粘贴模式，这样要粘贴的文字的格式就会被保留下来。

打开文件时(:tabedit 或者ls等)查看目录下文件
---

ctrl + d
