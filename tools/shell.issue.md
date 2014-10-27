bash shell
===

code style
---
    缩进为两个空格
    if [condition]; then # ;then写在一行
    while condition; do # ;then写在一行

以一下脚本为例
---

* 模块化
    . ./utils.sh # 或者 source./utils.sh
                 # 为了模块化
                 # 是导入当前目录下的utils.sh脚本
* function
    传参数
        参数使用$num代表传入的参数

    return
        听说智能返回数字(c语言里面的状态码)
        因此想返回字符串使用echo

* 函数调用
    单行调用直接使用func_name;
    如果在echo或者赋值的时候，使用$()
    例如: echo $(date +%Y-%m-%d)
          A=echo $(date +%Y-%m-%d)

* if
    不等时加!
    例如:
        if [ ! "$1" ]; then
          abc
        fi

* 脚本提示

例子
---
    #!/bin/bash
    . ./utils.sh

    path=${PWD}"/../"

    today(){
        echo $(date +%Y-%m-%d)
    }

    yesterday(){
        echo $(date -d yesterday +%Y-%m-%d)
    }

    scrapy_data(){
      start_date=$1
      end_date=$2
      cd $path
      echo "log: scrapy ${start_date} ~ ${end_date} data"
      scrapy crawl paper_edu_spider -a start_date=$start_date -a end_date=$end_date
    }

    scrapy_today(){
      scrapy_data $(today) $(today);
    }

    scrapy_yesterday(){
      scrapy_data $(yesterday) $(yesterday);
    }

    if [ ! "$1" ]; then
      echo "-h for help"
      exit 1
    fi

    while getopts "hty" arg; do
      case $arg in
        t)
          scrapy_today;
          ;;
        y)
          scrapy_yesterday;
          ;;
        h)
          echo "usage:"
          echo "    use -t to scrapy today"
          echo "    use -y to scrapy yesterday"
          ;;
        ?)
          echo "-h for help"
          exit 1
          ;;
      esac
    done

将某个目录下的某类型的文件都搞到一个文件中
---

例如将所有的py文件copy到一个文件中(例如我想在kindle里面看python-pattern这个项目的所有源代码)

下面的命令将项目里面所有的文件按照文件名+内容的方式copy到了pattern.txt中

for f in `ls *py`;do echo $f >> pattern.txt; cat $f >> pattern.txt;done;


bash的{}扩展
---
{}中使用','分隔会自动扩展

    cp xxx/{a,b} --> cp xxx/a xxx/b
