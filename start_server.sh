#!/bin/bash
# -----------------------------------------------------------------
# Auto-runner for Kata Ganti Nama Diri Server on Ugreen NAS (Port 8084)
# -----------------------------------------------------------------
DIR="/volume3/NASepg/scripts_custom/iflow-edugames-kata-ganti-nama-diri"
cd "$DIR" || exit 1

if [ -x "/volume3/NASepg/node-v20/bin/node" ]; then
    NODE_BIN="/volume3/NASepg/node-v20/bin/node"
elif command -v node >/dev/null 2>&1; then
    NODE_BIN="node"
else
    echo "[ERROR] Node.js not found!"
    exit 1
fi

pkill -f "server.js 8084" 2>/dev/null || true
sleep 1

mkdir -p /volume3/NASepg/logs
nohup "$NODE_BIN" "$DIR/server.js" 8084 >> /volume3/NASepg/logs/kgnd_server.log 2>&1 &

echo "✅ Server started in background on port 8084!"
echo "Log file: /volume3/NASepg/logs/kgnd_server.log"
echo "URL: http://192.168.0.238:8084/scripts_custom/iflow-edugames-kata-ganti-nama-diri/editjson.html"
