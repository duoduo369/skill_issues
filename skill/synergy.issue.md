synergy
===


有时候mac和windows无法建立正常的链接时，需要kill mac进程
---

    #!/usr/bin/env bash
    launchctl unload /Library/LaunchAgents/com.symless.synergy.synergy-service.plist
    sudo killall synergy-core
    launchctl load /Library/LaunchAgents/com.symless.synergy.synergy-service.plist
