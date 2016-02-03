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

跟着文件学习
---

gulpfile.coffee

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
