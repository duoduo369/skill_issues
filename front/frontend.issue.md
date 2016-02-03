frontend issue
===

npm淘宝镜像
---

http://npm.taobao.org/

    echo '\n#alias for cnpm\nalias cnpm="npm --registry=https://registry.npm.taobao.org \
      --cache=$HOME/.npm/.cache/cnpm \
      --disturl=https://npm.taobao.org/dist \
      --userconfig=$HOME/.cnpmrc"' >> ~/.zshrc && source ~/.zshrc


一个gulp的脚手架
===

https://github.com/WINTR/gulp-frontend-scaffold

install
---

    cnpm install -g gulp bower
    git clone https://github.com/WINTR/gulp-frontend-scaffold.git && cd gulp-frontend-scaffold
    cnpm install # 然而这个项目并不好用，里面有的东西无法安装了，我fork了一份重新装了一下
    # https://github.com/duoduo369/gulp-frontend-scaffold,
    # 由于有的时候npm bower会很慢，所以直接把bower npm装的东西丢到git了
    cnpm cache clean -f
    cnpm install -g n
    n stable

用法看Readme有介绍, 大体贴两条

* For development: `gulp dev` then navigate to http://localhost:3000 (or IP address).
* For deploy: `gulp build`

跟着文件学习

gulpfile.coffee
---


    gulp           = require 'gulp'
    requireDir     = require 'require-dir'
    runSequence    = require 'run-sequence'

    # Require individual tasks
    requireDir './gulp/tasks', { recurse: true }

    gulp.task "default", ["dev"]

    gulp.task "dev", ->
      runSequence "set-development", [
        "copy-images"
        "bower"
        "stylesheets"
        "webpack"
      ], "server", "watch"

    gulp.task "build", ->
      runSequence [
        "copy-images"
        "bower"
        "stylesheets"
        "webpack"
      ], "minify"

其中用到的东西, 只讲一次，因为各个task可能重复用了某些东西

[requireDir](https://github.com/aseemk/requireDir)将./gulp/tasks下的所有文件include到
了这个地方，所以下面的gulp.task可以直接用

gulp.task gulp的内置api，定义一个task，[文档](https://github.com/gulpjs/gulp/blob/master/docs/API.md#gulptaskname--deps-fn)

[runSequence](https://github.com/OverZealous/run-sequence)按照特定顺序执行

gulp.tasks.copy-images
---

> 图片处理, 只处理有变化的或者新的图片，压缩，然后复制

    gulp      = require 'gulp'
    plugins   = require('gulp-load-plugins')()
    config    = require "../config.coffee"

    gulp.task "copy-images", ->

      gulp.src "#{config.sourcePath}/#{config.imagesDirectory}/**/*"
        .pipe plugins.plumber()
        .pipe plugins.newer("#{config.outputPath}/#{config.imagesDirectory}")
        .pipe plugins.imagemin
          optimizationLevel: 5
        .pipe gulp.dest "#{config.outputPath}/#{config.imagesDirectory}"

[gulp-load-plugins](https://github.com/jackfranklin/gulp-load-plugins):
便捷的require可以直接调用你package.json里面gulp-xxx的东西,比如下面其实是相等的

    plugins.jshint = require('gulp-jshint');
    plugins.concat = require('gulp-concat');

gulp.src gulp的内置api，是指你的源文件位置，[文档](https://github.com/gulpjs/gulp/blob/master/docs/API.md#gulpsrcglobs-options)

.pipe [文档](https://nodejs.org/api/stream.html#stream_readable_pipe_destination_options),类似linux的管道

[gulp-plumber](https://github.com/floatdrop/gulp-plumber): This monkey-patch plugin is fixing [issue with Node Streams piping](https://github.com/gulpjs/gulp/issues/91). For explanations, read [this small article.](https://gist.github.com/floatdrop/8269868), 大体说node的pipe会出一些什么问题，出异常后会中断命令，这个是防止中断命令的.

[gulp-newer](https://github.com/tschaub/gulp-newer): A Gulp plugin for passing through only those source files that are newer than corresponding destination files. 就是说只处理修改过的文件

[gulp-imagemin](https://github.com/sindresorhus/gulp-imagemin): 跟名字一样，图片压缩

gulp.desc gulp的内置api，是指你的目标文件位置，[文档](https://github.com/gulpjs/gulp/blob/master/docs/API.md#gulpdestpath-options)

所以其实一般是gulp.src的源文件通过.pipe进行各种处理然后cp到gulp.desc的目标位置


gulp.tasks.bower
---

> 讲外部js压缩到一个js: 找到你安装会来的bower的主js，并且统统都丢到vendor.js上

    gulp           = require 'gulp'
    mainBowerFiles = require 'main-bower-files'
    plugins        = require('gulp-load-plugins')()
    config         = require "../config.coffee"

    gulp.task "bower", ->
      gulp.src mainBowerFiles()
        .pipe plugins.concat("vendor.js")
        .pipe gulp.dest "#{config.outputPath}/#{config.jsDirectory}"

[main-bower-files](https://github.com/ck86/main-bower-files): 如果你用bower来装东西，他会把bower上的整个项目拿回来，项目里面会有一个bower.json他会告诉你真的你想用的js在哪里， 所以这个东西就是干这个的，注意，**他貌似只找bower install --save**中的东东--save-dev的不找

[gulp-concat](https://github.com/contra/gulp-concat): Concatenates files, 连接文件


gulp.tasks.stylesheets
---

> css的处理, 这个项目里面用的是styl，所以编译，添加一些浏览器兼容的东西，生成sourcemaps, 复制

    gulp    = require 'gulp'
    plugins = require('gulp-load-plugins')()
    config  = require "../config.coffee"

    gulp.task "stylesheets", ->
      gulp.src ["#{config.sourcePath}/#{config.cssDirectory}/#{config.cssMainFile}.styl"]
        .pipe plugins.plumber()
        .pipe plugins.stylus
          sourcemap:
            inline: config.development
        .pipe plugins.sourcemaps.init
          loadMaps: true
        .pipe plugins.autoprefixer()
        .pipe plugins.sourcemaps.write()
        .pipe gulp.dest "#{config.outputPath}/#{config.cssDirectory}"

      gulp.src ["#{config.sourcePath}/#{config.cssDirectory}/ie.styl"]
        .pipe plugins.plumber()
        .pipe plugins.stylus()
        .pipe plugins.autoprefixer()
        .pipe gulp.dest "#{config.outputPath}/#{config.cssDirectory}"

[gulp-stylus](https://github.com/stevelacy/gulp-stylus):编译[styl](http://stylus-lang.com/)文件用的

[gulp-sourcemaps](https://github.com/floridoo/gulp-sourcemaps)生成[sourcemaps](http://www.ruanyifeng.com/blog/2013/01/javascript_source_map.html)的

[gulp-autoprefixer](https://github.com/sindresorhus/gulp-autoprefixer): 最初没看懂但是看[autoprefixer](https://github.com/postcss/autoprefixer)解释说是加浏览器兼容的一些东西的, 例如下面的代码

    :-webkit-full-screen a {
        display: -webkit-box;
        display: -webkit-flex;
        display: flex
    }
    :-moz-full-screen a {
        display: flex
    }
    :-ms-fullscreen a {
        display: -ms-flexbox;
        display: flex
    }
    :fullscreen a {
        display: -webkit-box;
        display: -webkit-flex;
        display: -ms-flexbox;
        display: flex
    }

    更新node 解决node的版本问题(主要是编译css时的问题)
    sudo npm cache clean -f
    sudo npm install -g n
    sudo n stable

    http://stackoverflow.com/questions/32490328/gulp-autoprefixer-throwing-referenceerror-promise-is-not-defined
    https://github.com/sindresorhus/gulp-autoprefixer/issues/45


gulp.tasks.webpack
---

> 打包源码js的看起来是，因为样式、图片、外部js之前两个task处理了

webpack   = require 'webpack'
gulp      = require 'gulp'
plugins   = require('gulp-load-plugins')()
config    = require "../config.coffee"

gulp.task 'webpack', ->
  production = if config.production then '.production' else ''
  webpack require("../webpack.config#{production}"), (err, stats) ->
    throw new gutil.PluginError 'webpack', err if err
    plugins.util.log "[webpack]", stats.toString()


webpack.config.coffee
    webpack = require('webpack')
    config  = require './config'
    #--------------------------------------------------------
    # Development Config
    #--------------------------------------------------------

    module.exports =
      cache: true
      entry: require './webpack.entries'
      output:
        path: "#{__dirname}/../#{config.outputPath}/#{config.jsDirectory}"
        filename: '[name].js'
      
      externals:
          "jquery": "jQuery"
          "$": "jQuery"

      module: loaders: [ 
        {
          test: /\.coffee$/
          loader: 'coffee-loader'
        }
      ]
      resolve:
        modulesDirectories: [
          'node_modules'
          'bower_components'
        ]
        extensions: [
          ''
          '.js'
          '.coffee'
          '.html'
        ]

[webpack](https://webpack.github.io/)

gulp.tasks.server
---

> 一个node server方便调试


    gulp    = require 'gulp'
    plugins = require('gulp-load-plugins')()
    config  = require "../config.coffee"

    gulp.task "server", ->
       gulp.src config.publicPath
        .pipe plugins.webserver
          host: '0.0.0.0'
          port: 3000
          livereload: 22345

[gulp-webserver](https://github.com/schickling/gulp-webserver): Streaming gulp plugin to run a local webserver with LiveReload, 就是起一个本地服务的

加了host 0.0.0.0 以及livereload不用他的默认配置，因为会出问题

    Port 35729 is already in use by another process

    https://github.com/toddmotto/fireshell/issues/39

gulp.tasks.watch
---

> 开发的时候文件变更马上编译 自动reload什么的

    gulp      = require 'gulp'
    plugins   = require('gulp-load-plugins')()
    config    = require "../config.coffee"

    #--------------------------------------------------------
    # Watch for changes and reload
    #--------------------------------------------------------

    gulp.task "watch", ->
      gulp.watch "#{config.sourcePath}/#{config.cssDirectory}/**/*.{styl,sass,scss,css}", ["stylesheets"]
      gulp.watch "#{config.sourcePath}/#{config.imagesDirectory}/**/*", ["copy-images"]
      gulp.watch "#{config.sourcePath}/#{config.jsDirectory}/**/*.{coffee,js}", ["javascripts"]
      gulp.watch "bower.json", ["bower"]

      plugins.livereload.listen()

      gulp.watch "#{config.publicPath}/**/*", (e) ->
        plugins.livereload.changed(e.path)

      return

[gulp.watch](https://github.com/gulpjs/gulp/blob/master/docs/API.md#gulpwatchglob--opts-tasks-or-gulpwatchglob--opts-cb): 监控文件，并且在文件变化时执行哪些task

[gulp-livereload](https://github.com/vohof/gulp-livereload): 修改后不用刷新浏览器自动加载
