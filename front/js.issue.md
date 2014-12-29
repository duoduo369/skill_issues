node issue
===

学习资源
---
    类似python koans的一种东西,安装后命令行里面有
    题目，按照题目往下走
    http://nodeschool.io/

CoffeeScript issue
===
    
安装
---
    之前需要先安装npm
    sudo npm install -g coffee-script

学习资源
---
    官网直接就有可以运行的东西
    http://coffeescript.org/

    google coffeescript小书(有中文版，而且有在线版)
    http://island205.github.io/tlboc/

    cookbook
    http://coffeescriptcookbook.com/

chaplin issue
===

吐槽一下先，backbone,chaplin,underscore的文档
应该出自一家之手，写的也太烂了吧～你要找的东西
基本都找不到。

网上的例子代码又极少，把用到的代码贴在这里

学习资源
---
    https://github.com/jashkenas/backbone
    http://backbonetutorials.com

    # coffee + backbone
    http://adamjspooner.github.io/coffeescript-meet-backbonejs/ 

    http://chaplinjs.org/

view显示的两种方式
---
    autoRender = true # 立马显示,暂时还没高明白什么时候使用false

    container和region,region优先级高于container,如果都指明则region
    覆盖container。

    1.在view中指定container的选择器,注意指定的这个container在new
    这个View实例之前需要存在。

    View              = require 'views/base/view'
    SiteUser          = require "models/site/site-user"

    module.exports = class SiteUserManagerView extends View

      container: '#add-user-model'
      autoRender: true
      template: require '../templates/add-user'
      className: 'modal-dialog'
      noWrap: false

    2.controller里面指定region,region在使用之前需要在上面
    的view中注册(定义)

    #view 根目录下有这样一个站点view,注册了这几个regions

    View = require 'views/base/view'

    # Site view is a top-level view which is bound to body.
    module.exports = class SiteView extends View
      container: 'body'
      noWrap: true
      regions:
        header: 'header'
        main: 'section'
        footer: 'footer'
      template: require './templates/site'


    controller 使用

    Controller            = require 'controllers/base/controller'

    HeaderView            = require 'views/home/header-view'
    SiteListView          = require 'views/site-manage/list-view'
    SiteDetailView        = require 'views/site-manage/detail-view'

    SiteModel             = require 'models/site/site'
    SiteCollection        = require 'models/site/site-collection'
    SiteUserCollection    = require 'models/site/site-user-collection'
    AdvCollection         = require "models/site/adv-collection"


    module.exports = class SiteController extends Controller

      list: (params)->
        new HeaderView
          region: 'header'
        
        new SiteListView
          collection: new SiteCollection
          advCollection: new AdvCollection
          region: 'main'

      detail: (params) ->
        new HeaderView
          region: 'header'

        new SiteDetailView
          model: new SiteModel
            id: params.id
          siteUserCollection: new SiteUserCollection
            site_id: params.id
          region: 'main'

gulp
---

npm install -g gulp

npm install gulp-util

npm install gulp-coffee

gulpfile.js

    var coffee = require('gulp-coffee');
    var gulp = require('gulp');
    var gutil = require('gulp-util');

    gulp.task('coffee', function() {
      gulp.src('./src/*.coffee')
      .pipe(coffee({bare: true}).on('error', gutil.log))
      .pipe(gulp.dest('./public/'))
    });

    gulp.task('default', function() {
      gulp.run('coffee')
    });

运行gulp

bower
---

bower init 引导生成bower.json
bower install package --save 安装package并且记录到bower.json中
bower install https://github.com/OwlFonk/OwlCarousel.git#1.3.2 --save 安装github的文件
--allow-root允许使用root用户安装

js库
---

[awesome-javascript](https://github.com/sorrycc/awesome-javascript)

在做一些事情的时候总有一些合适的工具

[一个各种js demo web](http://www.dowebok.com/)

js工具 [underscore](https://github.com/jashkenas/underscore)

剪切板[jquery.clipboard](https://github.com/valeriansaliou/jquery.clipboard) [zeroclipboard](https://github.com/zeroclipboard/zeroclipboard)

预先加载一些图片 preload js TODO: add url

图片加载完成 [imagesloaded](https://github.com/desandro/imagesloaded)

浏览器检验  现在在github里面搜了下update browser 暂时没实用过 TODO: add url, [有一个推荐](http://viamarte.github.io/modernweb/)
他还有可视化的东西可以选择然后生成js [连接](http://modernizr.com/)

ie 6-8的一些东西 [Respond](https://github.com/scottjehl/Respond)

鼠标的一些js [mousewheel](https://github.com/jquery/jquery-mousewheel)

做类似手机销售的宣传页 [fullPage.js](https://github.com/alvarotrigo/fullPage.js)

滚轮动画 [scrollReveal.js](https://github.com/julianlloyd/scrollReveal.js) [WOW.js](https://github.com/matthieua/WOW)

根据滚轮模糊图片 [crossfade.js](https://github.com/mikefowler/crossfade.js)

轮播 实在太多了 [owl.carousel](https://github.com/OwlFonk/OwlCarousel) [owl.carousel2](https://github.com/OwlFonk/OwlCarousel2) [unslider](https://github.com/idiot/unslider) [vegas 可以做一个全屏北京效果 有磨砂](https://github.com/jaysalvat/vegas)

弹出层 [layer](https://github.com/sentsin/layer)

刮彩票等等 橡皮擦 [jQuery.eraser](https://github.com/boblemarin/jQuery.eraser)

三方评论系统 [多说](http://duoshuo.com/)

时间轴 [TimelineJS](https://github.com/NUKnightLab/TimelineJS)

进度条 [progress.js](https://github.com/usablica/progress.js/) [pace](https://github.com/HubSpot/pace)

input动画 [fancyInput](https://github.com/yairEO/fancyInput)

select选择 [select2](http://ivaynberg.github.io/select2/)

提示 [tooltipster](https://github.com/iamceege/tooltipster)

延迟加在图片 [echo](https://github.com/toddmotto/echo)

视差滚动(Parallax Scrolling) [stellar](https://github.com/markdalgleish/stellar.js)
[一篇时差滚动插件的文章](http://desiznworld.com/2013/07/free-jquery-parallax-scrolling-plugins.html)
