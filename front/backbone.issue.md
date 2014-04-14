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

