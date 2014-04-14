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
1.定义model|collection

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

2.定义view

* new collection
* 绑定事件、events中和init中绑定
* render添加dom初始元素

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
