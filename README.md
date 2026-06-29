# 程序介绍
Telegram 群组、频道消息实时同步转发的 Python 脚本

采用 Python + Telethon 实现自动监控源群组、频道实时内容的发布，将最新内容实时转发到指定频道、群组，无需管理员权限。

# 环境准备
推荐使用 Debian12 系统搭建，其他 Linux 发行商也是可以的，但是需要自己折腾

安装 Python3 和 Pip
```
apt update && apt install python3-pip -y
```

安装 Telethon 库
```
pip3 install telethon
```

# 使用说明
1、修改脚本内的 api_id 和 api_hash，此处需要到 my.telegram.org(https://my.telegram.org) 处申请，需要 telegram 账号满二年以上才可以申请成功

2、修改脚本内的 SOURCE_CHANNEL 和 TARGET_CHANNEL，SOURCE_CHANNEL 为源频道，TARGET_CHANNEL 为指定频道，获取方法可以在 HubCao Robot(https://t.me/HubCao_Bot) 机器人内获取

3、运行 python3 forwarder.py

4、根据提示输入手机号、验证码、如果设置了两步验证密码就不需要验证码了，直接通过输入两步验证密码登录

5、开始转发：看到“正在监听...”后，去源频道发消息，秒转。

# 后台监听
一旦你关闭 SSH 窗口，程序就会停，所以需要设置后台运行监听
```
nohup python3 forwarder.py > output.log 2>&1 &
```
