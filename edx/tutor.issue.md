tutor
===

[Document](https://docs.tutor.overhang.io/)


开发环境命令
---

启 django
    tutor dev runserver lms
    tutor dev runserver cms

进 bash

    tutor dev run lms bash
    tutor dev run cms bash

ipython

    tutor dev run lms ./manage.py lms shell
    tutor dev run cms ./manage.py cms shell

宿主机挂载 edx 各个项目目录
---

[doc](https://docs.tutor.overhang.io/dev.html#run-a-local-development-webserver)

	vim "$(tutor config printroot)/env/dev/docker-compose.override.yml"

添加 如下配置后 tutor config save, 之后使用 tutor dev xxx 就会用挂载的目录了

	version: "3.7"
	services:
	  lms:
		volumes:
		  - /path/to/edx-platform/:/openedx/edx-platform
	  cms:
		volumes:
		  - /path/to/edx-platform/:/openedx/edx-platform
	  lms-worker:
		volumes:
		  - /path/to/edx-platform/:/openedx/edx-platform
	  cms-worker:
		volumes:
		  - /path/to/edx-platform/:/openedx/edx-platform


开发环境有时候 paver update_assets 会报错
---

    tutor dev start lms 
    tutor dev exec lms /bin/bash
    paver update_assets --settings=tutor.development
    然后 关掉 start lms的shell, tutor dev runserver lms

