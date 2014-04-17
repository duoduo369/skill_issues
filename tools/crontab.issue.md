定时任务
---

查看/etc/crontab
---
    # /etc/crontab: system-wide crontab
    # Unlike any other crontab you don't have to run the `crontab'
    # command to install the new version when you edit this file
    # and files in /etc/cron.d. These files also have username fields,
    # that none of the other crontabs do.

    SHELL=/bin/sh
    PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

    # m h dom mon dow user  command
    17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
    25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
    47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
    52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
    #

5个星星
---

/etc/crontab有注释 # m h dom mon dow user  command
分别是 分，小时，天，月，周
* 代表任何值
17代表17单位(天，小时，分)
/n 代表每n个单位

例如:spider.crontab

    0 */6 * * * /home/duoduo/projects/TechDict/app/spiders/crontabs/scrapy_data.sh -t
    30 1 * * * /home/duoduo/projects/TechDict/app/spiders/crontabs/scrapy_data.sh -y

第一行代表每天每隔6个小时，整点(第一个星星为0)执行某脚本
第二行表示每天1点半执行某脚本

加入cron中
---
    例如上面的spider.crontab文件
    crontab spider.crontab # 以当前用户将定时任务加入linux中
    crontab -l # 查看任务
    crontab -e # 编辑
    实际上，靠谱的做法是查看/var/spool/cron/crontabs下是否有
    此用户的任务
