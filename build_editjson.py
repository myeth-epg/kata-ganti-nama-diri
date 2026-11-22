import json

with open(r'X:\scripts_custom\iflow-edugames-kata-ganti-nama-diri\kata_ganti_nama_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

json_str = json.dumps(data, ensure_ascii=False)

html_content = '''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>华小国语人称代词题库编辑器 | Kata Ganti Nama Diri Editor</title>
    <style>
        :root {
            --bg-main: #1e1e22;
            --bg-header: #25252b;
            --bg-card: #2a2a30;
            --bg-input: #18181b;
            --border-color: #3f3f46;
            --text-primary: #f1f5f9;
            --text-muted: #94a3b8;
            --accent-blue: #60a5fa;
            --accent-orange: #fb923c;
            --accent-green: #22c55e;
            --accent-red: #ef4444;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei", sans-serif;
            background: var(--bg-main);
            color: var(--text-primary);
            padding-bottom: 60px;
        }
        header {
            position: sticky;
            top: 0;
            z-index: 100;
            background: var(--bg-header);
            border-bottom: 2px solid var(--border-color);
            padding: 14px 22px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.4);
        }
        .header-inner {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
        }
        .header-title h1 {
            font-size: 1.25em;
            color: var(--accent-blue);
            font-weight: 800;
        }
        .header-sub {
            font-size: 0.82em;
            color: var(--text-muted);
            margin-top: 2px;
        }
        .controls {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            align-items: center;
        }
        .ctrl-input, .ctrl-select {
            background: var(--bg-input);
            color: var(--text-primary);
            border: 1.5px solid var(--border-color);
            border-radius: 8px;
            padding: 7px 11px;
            font-size: 0.9em;
            outline: none;
        }
        .ctrl-input:focus, .ctrl-select:focus { border-color: var(--accent-blue); }
        .btn {
            border: none;
            border-radius: 8px;
            padding: 8px 14px;
            font-weight: 700;
            font-size: 0.88em;
            cursor: pointer;
            transition: all 0.15s;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }
        .btn:hover { opacity: 0.9; transform: translateY(-1px); }
        .btn-save { background: #16a34a; color: #fff; }
        .btn-add { background: #2563eb; color: #fff; }
        .btn-del { background: #dc2626; color: #fff; padding: 6px 10px; font-size: 0.8em; }
        .btn-card-save { background: #0284c7; color: #fff; padding: 6px 12px; font-size: 0.82em; }
        .btn-card-save.saved { background: #16a34a; }

        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 16px;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }
        .status-bar {
            background: #27272e;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 10px 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 8px;
            font-size: 0.88em;
            color: var(--text-muted);
        }
        .q-card {
            background: var(--bg-card);
            border: 1.5px solid var(--border-color);
            border-radius: 14px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            transition: border-color 0.2s;
        }
        .q-card:hover { border-color: #52525b; }
        .q-card-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }
        .q-index-badge {
            background: #1e3a5f;
            color: #93c5fd;
            padding: 3px 10px;
            border-radius: 8px;
            font-weight: 800;
            font-size: 0.85em;
        }
        .row-grid-4 {
            display: grid;
            grid-template-columns: 110px 90px 1fr 180px;
            gap: 10px;
        }
        .row-grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }
        .field-group {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
        .field-label {
            font-size: 0.76em;
            font-weight: 700;
            color: var(--text-muted);
        }
        .field-input {
            background: var(--bg-input);
            color: var(--text-primary);
            border: 1.5px solid var(--border-color);
            border-radius: 8px;
            padding: 8px 10px;
            font-size: 0.92em;
            width: 100%;
            outline: none;
        }
        .field-input:focus { border-color: var(--accent-blue); }
        .field-answer { color: #4ade80; font-weight: 800; }
        .field-sentence { color: #f8fafc; font-weight: 600; }
        .field-zh { color: var(--accent-orange); }

        @media (max-width: 780px) {
            .row-grid-4, .row-grid-2 { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <header>
        <div class="header-inner">
            <div class="header-title">
                <h1>✏️ 华小国语人称代词题库编辑器 (Kata Ganti Nama Diri)</h1>
                <div class="header-sub">点击卡片右上角「💾 保存此项」或顶部「💾 全部保存」，自动更新游戏网页 index.html</div>
            </div>
            <div class="controls">
                <input type="text" class="ctrl-input" id="search-input" placeholder="🔍 搜索句子 / 答案 / ID..." oninput="renderCards()" style="width:200px;">
                <select class="ctrl-select" id="cat-filter" onchange="renderCards()">
                    <option value="ALL">全部单元</option>
                </select>
                <button class="btn btn-add" onclick="addNewQuestion()">➕ 新增题目</button>
                <button class="btn btn-save" onclick="saveAllData()">💾 全部保存</button>
            </div>
        </div>
    </header>

    <div class="container">
        <div class="status-bar">
            <span id="count-info">⏳ 正在加载题库...</span>
            <span id="save-status">就绪 (注意：避免将 awak/anda/kamu 或 saya/aku 放进同一题选项)</span>
        </div>
        <div id="cards-wrap" style="display:flex; flex-direction:column; gap:14px;"></div>
    </div>

    <script id="embedded-data" type="application/json">
''' + json_str + '''
    </script>

    <script>
        let items = [];

        async function loadData() {
            try {
                const res = await fetch('/api/data', { cache: 'no-store' });
                if (res.ok) {
                    items = await res.json();
                } else {
                    throw new Error('API unavailable');
                }
            } catch (e) {
                try {
                    const res2 = await fetch('kata_ganti_nama_data.json', { cache: 'no-store' });
                    if (res2.ok) items = await res2.json();
                    else throw new Error('JSON fetch failed');
                } catch (e2) {
                    items = JSON.parse(document.getElementById('embedded-data').textContent);
                }
            }
            populateCategories();
            renderCards();
        }

        function populateCategories() {
            const sel = document.getElementById('cat-filter');
            const prev = sel.value;
            const cats = Array.from(new Set(items.map(i => i.category).filter(Boolean)));
            sel.innerHTML = '<option value="ALL">全部单元 (' + items.length + '题)</option>' +
                cats.map(c => `<option value="${esc(c)}">${esc(c)}</option>`).join('');
            if (cats.includes(prev)) sel.value = prev;
        }

        function esc(s) {
            return String(s || '').replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
        }

        function renderCards() {
            const q = (document.getElementById('search-input').value || '').toLowerCase().trim();
            const cat = document.getElementById('cat-filter').value;
            const wrap = document.getElementById('cards-wrap');

            const filtered = items.map((item, idx) => ({ item, idx })).filter(({ item }) => {
                if (cat !== 'ALL' && item.category !== cat) return false;
                if (!q) return true;
                return (item.id || '').toLowerCase().includes(q) ||
                       (item.sentence || '').toLowerCase().includes(q) ||
                       (item.answer || '').toLowerCase().includes(q) ||
                       (item.translation_zh || '').toLowerCase().includes(q);
            });

            document.getElementById('count-info').textContent = `共 ${items.length} 题 | 当前显示 ${filtered.length} 题`;

            wrap.innerHTML = filtered.map(({ item, idx }) => {
                const distStr = Array.isArray(item.distractors) ? item.distractors.join(', ') : '';
                return `
                <div class="q-card" id="card-${idx}">
                    <div class="q-card-top">
                        <span class="q-index-badge">#${idx + 1} · ${esc(item.id)}</span>
                        <div style="display:flex; gap:8px;">
                            <button class="btn btn-card-save" id="btn-save-${idx}" onclick="saveSingleCard(${idx})">💾 保存此项</button>
                            <button class="btn btn-del" onclick="deleteItem(${idx})">🗑️ 删除</button>
                        </div>
                    </div>
                    <div class="row-grid-4">
                        <div class="field-group">
                            <label class="field-label">题号 ID</label>
                            <input class="field-input" value="${esc(item.id)}" onchange="items[${idx}].id=this.value">
                        </div>
                        <div class="field-group">
                            <label class="field-label">组别 Group</label>
                            <input class="field-input" value="${esc(item.group)}" onchange="items[${idx}].group=this.value">
                        </div>
                        <div class="field-group">
                            <label class="field-label">单元分类 Category</label>
                            <input class="field-input" value="${esc(item.category)}" onchange="items[${idx}].category=this.value">
                        </div>
                        <div class="field-group">
                            <label class="field-label">正确答案 Answer</label>
                            <input class="field-input field-answer" value="${esc(item.answer)}" onchange="items[${idx}].answer=this.value">
                        </div>
                    </div>
                    <div class="field-group">
                        <label class="field-label">国语填充句子 Sentence（使用 ( ________ ) 表示空格）</label>
                        <input class="field-input field-sentence" value="${esc(item.sentence)}" onchange="items[${idx}].sentence=this.value">
                    </div>
                    <div class="field-group">
                        <label class="field-label">3 个干扰选项 Distractors（逗号分隔，例如: Kamu, Mereka, Beliau）</label>
                        <input class="field-input" value="${esc(distStr)}" onchange="items[${idx}].distractors=this.value.split(',').map(s=>s.trim()).filter(Boolean)">
                    </div>
                    <div class="row-grid-2">
                        <div class="field-group">
                            <label class="field-label">华语翻译 Translation ZH</label>
                            <input class="field-input field-zh" value="${esc(item.translation_zh)}" onchange="items[${idx}].translation_zh=this.value">
                        </div>
                        <div class="field-group">
                            <label class="field-label">语法解析 Explanation ZH</label>
                            <input class="field-input" value="${esc(item.explanation_zh)}" onchange="items[${idx}].explanation_zh=this.value">
                        </div>
                    </div>
                </div>`;
            }).join('');
        }

        function addNewQuestion() {
            const nextNum = items.length + 1;
            const idStr = 'A' + String(nextNum).padStart(3, '0');
            items.unshift({
                id: idStr,
                group: "A",
                category: "Group A: Kata Ganti Nama Diri",
                sentence: "( ________ ) suka membaca buku di perpustakaan.",
                answer: "Saya",
                distractors: ["Kamu", "Beliau", "Mereka"],
                explanation_zh: "",
                translation_zh: ""
            });
            populateCategories();
            renderCards();
        }

        function deleteItem(idx) {
            if (!confirm(`确定删除第 #${idx + 1} 题 (${items[idx].id}) 吗？`)) return;
            items.splice(idx, 1);
            populateCategories();
            renderCards();
            saveAllData();
        }

        async function saveSingleCard(idx) {
            const btn = document.getElementById(`btn-save-${idx}`);
            const ok = await saveAllData();
            if (ok && btn) {
                btn.textContent = "✅ 已保存";
                btn.classList.add('saved');
                setTimeout(() => {
                    btn.textContent = "💾 保存此项";
                    btn.classList.remove('saved');
                }, 1800);
            }
        }

        async function saveAllData() {
            const st = document.getElementById('save-status');
            st.textContent = "⏳ 正在保存至服务器并重建网页...";
            st.style.color = "#60a5fa";
            try {
                const res = await fetch('/api/save', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(items)
                });
                const data = await res.json();
                if (!res.ok || !data.success) throw new Error(data.error || 'Save failed');
                st.textContent = "✅ " + data.message + " (" + new Date().toLocaleTimeString('zh-MY', { hour12: false }) + ")";
                st.style.color = "#4ade80";
                return true;
            } catch (err) {
                st.textContent = "⚠️ 保存失败（请通过 server.py / server.js 打开本页）：" + err.message;
                st.style.color = "#f87171";
                return false;
            }
        }

        window.onload = loadData;
    </script>
</body>
</html>
'''

with open(r'X:\scripts_custom\iflow-edugames-kata-ganti-nama-diri\editjson.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated X:\\scripts_custom\\iflow-edugames-kata-ganti-nama-diri\\editjson.html successfully!")
