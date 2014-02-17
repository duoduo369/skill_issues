angularjs
===

使用brunch来新建项目
---
    brunch里面可以方便的管理需要用到的各种库
    brunch n gh:scotch/angular-brunch-seed
    包含coffeescript,angularjs,bootstrap

    新建完成后可以阅读readme里面有详细的说明

    注意：默认brunch新建的项目使用jade模板，如果想用html
    在scripts中可以发现有compile-html.sh(请阅读README,非常详细的说明)
    ./scripts/compile-html.sh

    ps:现在我用的这个版本angular 是1.2.5 有点老了，把bower.js angular
    相关的部分都改成*就会下载最新版本



learning demo
---
    使用官网那个关于手机的app tutorial,结合brunch新建的
    项目，节省自己的时间(我用coffee)。

    problems

    1. 在controller那一关,brunch demo的controller
    代码如下,开始我已为可以直接在后面接 
    `.controller('xxxCtrl',[...])`,结果页面报错，原来应该这样

    angular.module('app.controllers', [])

    .controller('AppCtrl', [
      '$scope'
      '$location'
      '$resource'
      '$rootScope'

    ($scope, $location, $resource, $rootScope) ->

      # Uses the url to determine if the selected
      # menu item should have the class active.
      $scope.$location = $location
      $scope.$watch('$location.path()', (path) ->
        $scope.activeNavId = path || '/'
      )

      # getClass compares the current url with the id.
      # If the current url starts with the id it returns 'active'
      # otherwise it will return '' an empty string. E.g.
      #
      #   # current url = '/products/1'
      #   getClass('/products') # returns 'active'
      #   getClass('/orders') # returns ''
      #
      $scope.getClass = (id) ->
        if $scope.activeNavId.substring(0, id.length) == id
          return 'active'
        else
          return ''
    ])

    .controller('MyCtrl1', [
      '$scope'

    ($scope) ->
      $scope.onePlusOne = 2
    ])

    .controller('MyCtrl2', [
      '$scope'

    ($scope) ->
      $scope
    ])
    
    正确的做法,由于官网demo中新建了一个命名空间，而brunch
    的命名空间是另一个，所以应该如下,之后的controller在接着写,
    注意在html页面里的ng-app选中这个命名空间`<html
    ng-app="phonecatApp">`
    

    angular.module('phonecatApp', [])

    .controller('PhoneListCtrl', [
      '$scope'

    ($scope) ->
      $scope.phones = [
        'name': 'Nexus S'
        'snippet': 'Fast just got faster with Nexus S.'
      ,
        'name': 'Motorola XOOM™ with Wi-Fi'
        'snippet': 'The Next, Next Generation tablet.'
      ,
        'name': 'MOTOROLA XOOM™'
        'snippet': 'The Next, Next Generation tablet.'
      ]
    ])

    2. 在step-12需要用动画,jquery需要用1.10.X,angular > 1.2.10
    在bower.js更改相应配置

angular初步感觉
---

    1. app.js是程序的入口,读代码的时候从这个文件下手
    app.js 做了这些事情:
        * 声明了命名空间，以及需要加载的各个其他模块
        * 定义了路由表，而路由表又是链接controller和view的桥梁

    2. services 和 controller
        * controller 和以前其他mvc里面controller相同，处理业务逻辑,
          而angularjs由于为了让controller处理的事情更少，而且不同的
          页面对应的业务也不同，controller主要处理数据，view里面也会
          有一些和数据显示有关的业务处理(directive),这样controller就
          更容易测试
        * services 则是真正想服务器请求资源的组建，还暴露对象的名字
          # phonecatServices.factory('Phone', ['$resource', ....])
          例如factory暴露出的名字就可以供controller来引用

    3. filter
        * filter类似linux的管道符，对后台传来的原生数据做一步处理，
          使得view里面显示的时候可以更加的人性化(而不是显示true,null
          或者其他不符和自己心意的数据)

    4. animate
        * angularjs提供的动画

angularjs 新浪微博跨域解决办法
---
    问题：oauth跨域
    angularjs jsonp只能是get方式，而http.post和resouce oauth时都会引发跨域问题

    解决办法，让跨域变成非跨域
    跨域是前端问题，javascript访问非本域的东西的时候会有这个问题，因此后端实现
    oauth然后让前端访问本域内的地址就可以解决这个问题。

    方法有下面：
       1.后端服务器做个代理(公司牛人给的解决方案，具体怎么样实现没有深入研究) 
       2.使用新浪的sdk，后端解决oauth, <a href="/oauth2/sina/authorize">
         http://open.weibo.com/wiki/SDK(新浪) 
         http://michaelliao.github.io/sinaweibopy/(python sdk)
         https://github.com/tianyu0915/django-sina-login(python sdk 例子)

最佳实践
---
    from ng-book

1. $scope绑定的时候将数据绑定到model的属性上
    $scope.clock  --> $scope.clock.now

2. controller命名使用XXController而不是XXCtrl
