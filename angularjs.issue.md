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


learning demo
---
    使用官网那个关于手机的app tutorial,结合brunch新建的
    项目，节省自己的时间(我用coffee)。

    第一个问题，在controller那一关,brunch demo的controller
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

