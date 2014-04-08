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
