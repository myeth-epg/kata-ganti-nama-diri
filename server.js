#!/usr/bin/env node
// -*- coding: utf-8 -*-
// Universal Node.js Web Server for SJKC Kata Ganti Nama Diri Game & Editor
// Runs on Ugreen NAS (Linux) or Windows PC with zero npm dependencies

const http = require('http');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const PORT = parseInt(process.env.PORT || process.argv[2] || '8084', 10);
const BASE_DIR = __dirname;
const DATA_FILE = path.join(BASE_DIR, 'kata_ganti_nama_data.json');
const BACKUP_FILE = path.join(BASE_DIR, 'kata_ganti_nama_data.bak.json');
const BUILD_SCRIPT = path.join(BASE_DIR, 'build_html.py');

const MIME_TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.mp3':  'audio/mpeg',
    '.js':   'application/javascript; charset=utf-8',
    '.css':  'text/css; charset=utf-8',
    '.png':  'image/png',
    '.ico':  'image/x-icon'
};

const server = http.createServer((req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

    if (req.method === 'OPTIONS') {
        res.writeHead(200);
        res.end();
        return;
    }

    const parsedUrl = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
    let pathname = decodeURIComponent(parsedUrl.pathname);

    // 1. API: GET /api/data
    if (pathname.endsWith('/api/data')) {
        res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
        res.setHeader('Content-Type', 'application/json; charset=utf-8');
        if (fs.existsSync(DATA_FILE)) {
            res.writeHead(200);
            fs.createReadStream(DATA_FILE).pipe(res);
        } else {
            res.writeHead(404);
            res.end(JSON.stringify({ error: 'kata_ganti_nama_data.json not found' }));
        }
        return;
    }

    // 2. API: POST /api/save
    if (pathname.endsWith('/api/save') || pathname.endsWith('/api/save-json')) {
        if (req.method !== 'POST') {
            res.writeHead(405);
            res.end('Method Not Allowed');
            return;
        }

        let body = '';
        req.on('data', chunk => { body += chunk; });
        req.on('end', () => {
            try {
                const newData = JSON.parse(body);
                if (!Array.isArray(newData)) {
                    throw new Error('Data must be an array of question objects.');
                }

                if (fs.existsSync(DATA_FILE)) {
                    fs.copyFileSync(DATA_FILE, BACKUP_FILE);
                }

                fs.writeFileSync(DATA_FILE, JSON.stringify(newData, null, 2), 'utf8');

                let rebuildMsg = "index.html 与 editjson.html 已同步更新";
                exec(`python "${BUILD_SCRIPT}"`, (err, stdout, stderr) => {
                    if (err) console.log('[WARN] Rebuild html err:', stderr || err.message);
                });
                const BUILD_EDIT_SCRIPT = path.join(BASE_DIR, 'build_editjson.py');
                exec(`python "${BUILD_EDIT_SCRIPT}"`, (err, stdout, stderr) => {
                    if (err) console.log('[WARN] Rebuild editjson err:', stderr || err.message);
                });

                res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
                res.end(JSON.stringify({
                    success: true,
                    count: newData.length,
                    message: `成功保存 ${newData.length} 道题目！${rebuildMsg}`,
                    backup: 'kata_ganti_nama_data.bak.json'
                }));
                console.log(`[API] Saved ${newData.length} items to kata_ganti_nama_data.json`);
            } catch (err) {
                res.writeHead(400, { 'Content-Type': 'application/json; charset=utf-8' });
                res.end(JSON.stringify({ success: false, error: err.message }));
                console.error('[API ERR]', err.message);
            }
        });
        return;
    }

    // 3. Static Files
    let relativeFile = pathname;
    const folderPrefix = '/scripts_custom/iflow-edugames-kata-ganti-nama-diri';
    if (relativeFile.startsWith(folderPrefix)) {
        relativeFile = relativeFile.substring(folderPrefix.length);
    }
    if (relativeFile === '/' || relativeFile === '') {
        relativeFile = '/index.html';
    }

    const filePath = path.join(BASE_DIR, relativeFile);

    if (!filePath.startsWith(BASE_DIR) || !fs.existsSync(filePath) || fs.statSync(filePath).isDirectory()) {
        res.writeHead(404);
        res.end('404 Not Found');
        return;
    }

    const ext = path.extname(filePath).toLowerCase();
    if (ext === '.json' || ext === '.html') {
        res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
    }
    res.setHeader('Content-Type', MIME_TYPES[ext] || 'application/octet-stream');
    res.writeHead(200);
    fs.createReadStream(filePath).pipe(res);
});

server.listen(PORT, '0.0.0.0', () => {
    console.log('=======================================================');
    console.log(` SJKC Kata Ganti Nama Diri Server Running on Port ${PORT}`);
    console.log(` Game:   http://localhost:${PORT}/index.html`);
    console.log(` Editor: http://localhost:${PORT}/editjson.html`);
    console.log(` Admin:  http://localhost:${PORT}/admin.html`);
    console.log('=======================================================');
});
