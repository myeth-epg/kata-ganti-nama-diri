# -*- coding: utf-8 -*-
import http.server
import socketserver
import os
import sys
import json
import shutil
import subprocess

PORT = 8084
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "kata_ganti_nama_data.json")
BACKUP_FILE = os.path.join(BASE_DIR, "kata_ganti_nama_data.bak.json")
BUILD_SCRIPT = os.path.join(BASE_DIR, "build_html.py")
BUILD_EDIT_SCRIPT = os.path.join(BASE_DIR, "build_editjson.py")

FOLDER_PREFIX = '/scripts_custom/iflow-edugames-kata-ganti-nama-diri'

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def translate_path(self, path):
        clean_path = path.split('?', 1)[0].split('#', 1)[0]
        if clean_path.startswith(FOLDER_PREFIX):
            clean_path = clean_path[len(FOLDER_PREFIX):]
            if not clean_path.startswith('/'):
                clean_path = '/' + clean_path
        return super().translate_path(clean_path)

    def normalize_path(self):
        p = self.path
        if '?' in p:
            p = p.split('?')[0]
        if p.startswith(FOLDER_PREFIX):
            sub = p[len(FOLDER_PREFIX):]
            if not sub.startswith('/'):
                sub = '/' + sub
            return sub
        return p

    def end_headers(self):
        norm = self.normalize_path()
        if norm.endswith('.json') or '/api/' in norm:
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        norm = self.normalize_path()
        if norm == '/api/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(b'[]')
            return
        super().do_GET()

    def do_POST(self):
        norm = self.normalize_path()
        if norm in ('/api/save', '/api/save-json'):
            length = int(self.headers.get('Content-Length', 0))
            raw = self.rfile.read(length)
            try:
                new_data = json.loads(raw.decode('utf-8'))
                if not isinstance(new_data, list):
                    raise ValueError("Data must be a JSON array.")

                if os.path.exists(DATA_FILE):
                    shutil.copy2(DATA_FILE, BACKUP_FILE)

                with open(DATA_FILE, 'w', encoding='utf-8') as f:
                    json.dump(new_data, f, ensure_ascii=False, indent=2)

                for script in (BUILD_SCRIPT, BUILD_EDIT_SCRIPT):
                    if os.path.exists(script):
                        subprocess.Popen([sys.executable, script], cwd=BASE_DIR)

                resp = json.dumps({
                    "success": True,
                    "count": len(new_data),
                    "message": f"成功保存 {len(new_data)} 道题目！index.html 与 editjson.html 已同步更新",
                    "backup": "kata_ganti_nama_data.bak.json"
                }, ensure_ascii=False).encode('utf-8')

                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(resp)
            except Exception as e:
                resp = json.dumps({"success": False, "error": str(e)}, ensure_ascii=False).encode('utf-8')
                self.send_response(400)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(resp)
            return

        self.send_response(404)
        self.end_headers()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), CustomHandler) as httpd:
        print("=======================================================")
        print(f" SJKC Kata Ganti Nama Diri Server Running on Port {PORT}")
        print(f" Game:   http://localhost:{PORT}/index.html")
        print(f" Editor: http://localhost:{PORT}/editjson.html")
        print(f" Admin:  http://localhost:{PORT}/admin.html")
        print("=======================================================")
        httpd.serve_forever()
