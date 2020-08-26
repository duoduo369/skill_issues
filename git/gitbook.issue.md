gitbook
===

使用gitbook写书
    https://github.com/GitbookIO/gitbook

安装
    npm install gitbook-cli -g

例如 github上有项目

    https://github.com/duoduo369/skill_issues
    需要有SUMMARY.md and README.md

gitbook build 如果有如下异常说明node版本不对，他用的node 10

	Installing GitBook 3.2.3
	/usr/local/lib/node_modules/gitbook-cli/node_modules/npm/node_modules/graceful-fs/polyfills.js:287
		  if (cb) cb.apply(this, arguments)
	TypeError: cb.apply is not a function
		at /usr/local/lib/node_modules/gitbook-cli/node_modules/npm/node_modules/graceful-fs/polyfills.js:287:18

如果node版本不对，安装nvm

gitbook serve


SUMMARY格式
    章节之间不能有空格

    # skill_issues

    平时开发时的经验积累，有高级用法，也有简单用法，都是干货。为的是增加开发效率！

    * [前端](front/README.md)
        * [angularjs](front/angularjs.issue.md)
        * [js](front/js.issue.md)
        * [css](front/css.issue.md)
    * [python](python/README.md)
        * [python](python/python.issue.md)
