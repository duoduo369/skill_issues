mac中使用rz sz
---
http://openexz.sinaapp.com/2012/08/29/%E5%9C%A8iterm2%E4%B8%AD%E4%BD%BF%E7%94%A8zmodem%E7%9A%84%E6%96%B9%E6%B3%95/


mysql
---
brew services start mysql

ssh-key copy
---
cat ~/.ssh/id_rsa.pub | pbcopy


mac 开放某个端口例如1234
---

		sudo vim /etc/pf.conf

		# Open port 1234 for TCP on all interfaces
		pass in proto tcp from any to any port 1234
		# You can limit the ip addresses .. replace any with allowed addresses ..


		sudo pfctl -f /etc/pf.conf
		重启电脑


允许局域网中的xshell ssh mac
---

    Mac的系统偏好设置 > 共享 > 打开远程登录和远程管理


使用BetterTouchTool 增强touch bar
---
    https://www.folivora.ai/
