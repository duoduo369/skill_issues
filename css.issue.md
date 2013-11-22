css相关
===

背景background
---------

background: url("backtop.png") no-repeat scroll -145px -65px;(left top)

background-position 来更改图片位置

IE6 不支持的
---

    * box-shadow
    * border-radius
    * rgba(0,0,0,0.4)

overflow
----

容器元素的时候用overflow=auto，用在父元素上，IE6 需要加上zoom:1，并且需要一个width或者height来是IE hasLayout

例如，在header级的ul li a 上面li添加float之后在IE中飞走了，可以在ul上加上overflow

    .header {
        width:500px;
        margin-left:180px;
    }
    .header  ul {
        overflow:auto;
    }
    .header  ul li{
        float:left;
    }
    .header  ul li a{
        color:#FFF;
        display:block;
        line-heigth:20px;
        padding:20px;   
        text-decoration:none;
    }

display:block
--------

可以让a里面的所有元素变为一个块区，这样在鼠标移动到元素包含列的时候就能触发a。
abbr为简写 

    <a href="http://learn.shayhowe.com/advanced-html-css/">
        <span>An Advanced Guide to</span>
        <abbr title="Hyper Text Markup Language">HTML</abbr>
        <abbr title="and">&amp;</abbr>
        <abbr title="Cascading Style Sheets">CSS</abbr>
    </a>


背景
-----

将最后面一个父块设置背景色

例如下面的代码块，css作为左右分栏(div-container,detailed-css-positioning)，如果将body设置为黑色，detailed-css-positioning设为白色，就不用担心右边白的比左边黑的长了，因为黑色会一直跟随父背景增长的。

    <body >
        <div id="container">
            <div id="div-container">
            </div>
            <div id="detailed-css-positioning">
            </div>
        </div>
    </body>

font
-----

font中的line-height是指这行字的高度。如果想要垂直居中，把line-height设置到和容器一样高即可。

例如下面设置一个圆形的div(IE 6 8无效 border-radius)，font:26px/20px-->font-size:26px,line-height:20px
那么div的高度 = 20px + 15px * 2(padding: 15px 0) = 50px，宽度设置为50，这样div就是一个方形的了，
然后设置border并且让text-align居中即可。

    .contents h5 span{
        border-radius: 30px;
        font: 26px/20px "Droid Serif",Constantia,Palatino,"Palatino Linotype","Book Antiqua",Georgia,serif;
        padding: 15px 0;
        text-align: center;
        text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.1);
        
        width: 50px;
    }


使用绝对定位
---

父容器一定是relative，
然后孩子使用absolute即可绝对定位。


兼容ie的透明度写法
----

    opacity: 0.98;
    -ms-filter: progid:DXImageTransform.Microsoft.Alpha(Opacity = 98);
    filter: alpha(opacity = 98); 


字体代码片段
----

    body {
        font: 12px/1.6 "Hiragino Sans GB","Microsoft YaHei","Segoe UI",Tahoma,Arial,Helvetica,sans-serif;
    }
    pre {
        font: 12px/1.6 "Hiragino Sans GB","Microsoft YaHei","Segoe UI",Tahoma,Arial,Helvetica,sans-serif;
    }
    code {
        font-family: courier new,courier,monospace
    }

火狐里面超过时显示省略号...
---

只适用于像新闻标题这种1行显示的

设定容器宽度,然后不让文字换行，超出部分隐藏

    
    text-overflow:ellipsis;
    white-space:nowrap;
    overflow:hidden; 

分页或者导航ul li a
----

1.li上加float:left

2.a上一定加display:block;color，并且在a上设置字体。

    .zarkfx_pagination_default .zarkfx_pagination_current_page {color:#000;}
    .zarkfx_pagination_default ul li {float:left;}
    .zarkfx_pagination_default ul li a {display:block;color:#6F6F6F; font-size:12px; }

添加其余样式美化

1.a上可以用padding来美化

    .zarkfx_pagination_default{
        width:500px ;
        margin:0 auto;
        padding-bottom: 40px;
        padding-top: 10px;
        text-align: center;
    }

    .zarkfx_pagination_default ul li{
        margin: 0 5px;
    }
    .zarkfx_pagination_default ul li a{
        color:#CCCCAA;
        font-weight:bold;
        border:1px solid #CCCCCC;
        padding:10px;
        text-decoration:none;
    }
    .zarkfx_pagination_default ul li a:hover{
        color:#F7739F;
        box-shadow: 0 4px 2px -2px rgba(0,0,0,0.4);
    }
