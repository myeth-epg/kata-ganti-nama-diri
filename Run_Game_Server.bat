@echo off
chcp 65001 >nul
echo =======================================================
echo 启动 华小国语人称代词 (Kata Ganti Nama Diri) 本地服务器
echo SJK(C) Kata Ganti Nama Diri Game ^& Editor Server
echo =======================================================
echo.
echo 本机游戏地址:    http://localhost:8084/index.html
echo 本机编辑器地址:  http://localhost:8084/editjson.html
echo 管理员后台地址:  http://localhost:8084/admin.html
echo 局域网访问地址:  http://192.168.0.238:8084/editjson.html
echo.
echo 游戏及编辑进行时，请保持此窗口开启。
echo 正在打开编辑器...
start http://localhost:8084/editjson.html

python server.py 8084
pause
