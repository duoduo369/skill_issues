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


sublime 等打开因此文件
---

打开时在 finder 选择文件时按下 `cmd + shift + .` 即可显示隐藏文件


mac 截图
---

    mkdir ~/Documents/capture
    defaults write com.apple.screencapture location ~/Documents/capture
    killall SystemUIServer


最大化窗口切换
---
    非手势的情况下 ctrl + 键盘左右键


键盘状态回到桌面
---
    ctrl + 键盘上箭


输入法切换
---
    ctrl + space

浏览器tab切换
---
    ctrl + tab

npm 安装错误 No Xcode or CLT version detected!
---

尝试用如下命令进行修复 `xcode-select --install` 系统提示如下信息

    xcode-select: error: command line tools are already installed, use "Software Update" to install updates

而事实上并没有所谓的"Software Update"可以更新

正确姿势

    sudo rm -rf $(xcode-select -print-path)
    xcode-select --install
