gitbook
===

使用gitbook写书
    https://github.com/GitbookIO/gitbook

安装
    npm install gitbook -g

例如 github上有项目
    https://github.com/duoduo369/skill_issues
    需要有SUMMARY.md and README.md

    gitbook build -g duoduo369/skill_issues
    gitbook serve -g duoduo369/skill_issues

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
