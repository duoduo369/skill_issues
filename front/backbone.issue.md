backbone issue
===

文件结构
---
    app
    ├── assets  # 根目录的assert
    │   ├── images
    │   └── index.html
    ├── common  # backbone的配置、application、基类等等
    │   ├── application.coffee
    │   ├── config.coffee
    │   ├── mediator.coffee
    │   ├── mock.coffee
    │   └── views
    │       └── base
    │           └── view.coffee
    ├── lib
    │   ├── utils.coffee
    │   └── view-helper.coffee
    └── tutorial # 具体的模块
        ├── assets
        │   └── README.md
        ├── controllers
        │   └── README.md
        ├── initialize.coffee
        ├── routes.coffee
        └── views # view和template
            ├── home
            │   ├── list-view.coffee
            │   └── templates
            │       └── README.md
            └── README.md

修改页面的dom使用render
---

注意，取属性值的时候需要用双引号,因为解释器不识别单引号

    $('ul').append "<li>item  #{@counter}</li>"

view el
---
    el必须是**pre exist**，也就是在调用前必须存在此元素

    View = require 'common/views/base/view'

    module.exports = class ListView extends View

      el: '#test'

      initialize: ->
        _.bindAll @
        @render()

      render: ->
        $(@el).append('<ul><li>hello backbone</li></ul>')
        @

注意`<script>require('/tutorial/initialize');</script>`这一行需要写在 id='test'
的元素后面，否则会找不到这个dom

    <!doctype html>
    <!--[if IE 8]>    <html class="no-js lt-ie9" lang="en"> <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
    <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
      <title>Brunch example application</title>
      <meta name="viewport" content="width=device-width">
      <link rel="stylesheet" href="/stylesheets/app.css">
      <script src="/javascripts/vendor.js"></script>
      <script src="/javascripts/app.js"></script>
    </head>
    <body>
        <header>
            <h1>title</h1>
            <p>p p p p</p>
        </header>
        <div id="test"></div>
        <script>require('/tutorial/initialize');</script>
    </body>
    </html>

MVC
---

###1.定义model|collection

    # app/tutorial/models/item.coffee

    Model = require 'common/models/base/model'

    module.exports = class Item extends Model

      defaults:
        part1: 'hello'
        part2: 'Backbone'


    # app/tutorial/models/list.coffee

    Collection = require 'common/models/base/collection'
    Item = require './item'

    module.exports = class List extends Collection

      model: Item

###2.定义view

new collection; 绑定事件、events中和init中绑定; render添加dom初始元素

    View = require 'common/views/base/view'
    List = require 'tutorial/models/list'
    Item = require 'tutorial/models/item'

    module.exports = class ListView extends View

      el: '#test'
      events:
        'click button': 'addItem'

      initialize: ->
        _.bindAll @

        @collection = new List
        @collection.bind('add', @appendItem)

        @counter = 0
        @render()

      render: ->
        @$el.append '<button class="pure-button pure-button-primary">Add List Item</button>'
        @$el.append '<ul></ul>'

      addItem: ->
        @counter++
        item = new Item
        item.set
          part2: "#{item.get 'part2'} #{@counter}"
        @collection.add item

      appendItem: (item) ->
        $('ul').append "<li>#{item.get 'part1'}  #{item.get 'part2'}</li>"


chaplin
===
使用chaplin后有一些变化,以及用法

view
---
根据源码
https://github.com/chaplinjs/chaplin/blob/master/src/chaplin/views/view.coffee

backbone view中的el现在为container

    constructor: @el = @container if @container

autoRender是否在constructor里面调用一次render

    constructor: @render() if @autoRender


不要在使用_bindAll会出现问题

item-view
---
item-view继承自Chaplin.View,以前使用render添加dom，现在可以直接使用
hbs模板,不过根据源码getTemplateFunction必须重写

    getTemplateFunction ->
      throw new Error 'View#getTemplateFunction must be overridden'

重写成,可以放在你自定义的View基类里面

    getTemplateFunction: ->
      @template

hbs模板使用双括号引用model中的属性 {{attr}}

list-view
---

与item-view相同，也是需要重写getTemplateFunction
list view中的itemView指明具体的ItemView,当list view的collection中
有变化时会自动渲染dom,此例中的addItem在collection里面调用add会处发
这个事件，注意container和listSelector的不同

源码中listSelector的注释:

    # as the container of the item views. If you specify `listSelector`, the
    # item views will be appended to this element. If empty, $el is used.
    listSelector: null

例如本例子中的模板里面有一个ul，注意listSelector是在**本模板的dom中选择**,
即:

    最初
    <div id="test">listview会加在这里</div>
    加载listview后
    <div id="test"><button ...><ul></ul></button></div>
    如果listSelector为 'div ul'会选不中这个ul的
    使用ul才可以选中

    View = require 'common/views/base/view'
    CollectionView = require 'common/views/base/collection-view'
    List = require 'tutorial/models/list'
    Item = require 'tutorial/models/item'
    ItemView = require './item-view'

    module.exports = class ListView extends CollectionView

      autoRender: true
      container: '#test'
      itemView: ItemView
      listSelector: 'ul'
      template: require './templates/list'

      events:
        'click button': 'addItem'

      initialize: ->
        @collection = new List
        @counter = 0
        super

      addItem: ->
        @counter++
        item = new Item
        item.set
          part2: "#{item.get 'part2'} #{@counter}"
        @collection.add item

    模板list.hbs

    <button class="pure-button pure-button-primary">Add List Item</button>
    <ul></ul>
