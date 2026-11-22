import json

with open(r'X:\scripts_custom\iflow-edugames-kata-ganti-nama-diri\kata_ganti_nama_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

json_str = json.dumps(data, ensure_ascii=False)

html_content = '''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>华小国语人称代词连连乐 | SJK(C) Kata Ganti Nama Diri Quiz</title>
    <style>
        * {
            box-sizing: border-box;
            user-select: none;
            -webkit-user-select: none;
        }

        body {
            font-family: 'Comic Sans MS', 'Chalkboard SE', 'Segoe UI', 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #70e1f5 0%, #ffd194 100%);
            margin: 0;
            padding: 10px;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow-x: hidden;
        }

        .game-area {
            position: relative;
            width: 880px;
            max-width: 98vw;
            min-height: 600px;
            background: linear-gradient(to bottom, #ffffff 0%, #f4faff 100%);
            border: 6px solid #4CAF50;
            border-radius: 24px;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25);
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow: hidden;
        }

        /* Top Header Bar */
        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
            padding-bottom: 10px;
        }

        .level-wrapper {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 5px;
        }

        .user-name-tag {
            background: linear-gradient(135deg, #fff8e1 0%, #ffecb3 100%);
            border: 2px solid #ffb300;
            color: #b78103;
            font-weight: 800;
            font-size: 0.95em;
            padding: 3px 14px;
            border-radius: 14px;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 2px 6px rgba(255, 179, 0, 0.25);
            cursor: pointer;
            transition: all 0.2s;
        }

        .user-name-tag:hover {
            transform: scale(1.04);
            border-color: #ffa000;
        }

        .user-avatar { font-size: 1.1em; }

        .level-badge {
            background: #e8f5e9;
            color: #1b5e20;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 1.15em;
            font-weight: bold;
            border: 2px solid #81c784;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .score-box {
            display: flex;
            gap: 10px;
            font-size: 0.95em;
        }

        .score-item {
            padding: 2px 10px;
            border-radius: 12px;
            font-weight: bold;
        }
        .score-betul { background: #c8e6c9; color: #2e7d32; }
        .score-salah { background: #ffcdd2; color: #c62828; }

        .control-buttons {
            display: flex;
            gap: 8px;
            align-items: center;
            flex-wrap: wrap;
        }

        .category-select {
            padding: 6px 12px;
            border-radius: 14px;
            border: 2px solid #2196F3;
            background: #e3f2fd;
            color: #1565c0;
            font-weight: bold;
            font-size: 0.95em;
            cursor: pointer;
            outline: none;
        }

        .top-btn {
            background: #f5f5f5;
            border: 2px solid #ccc;
            border-radius: 14px;
            padding: 6px 12px;
            font-size: 0.9em;
            cursor: pointer;
            font-weight: bold;
            color: #333;
            transition: all 0.2s;
        }
        .top-btn:hover { background: #e0e0e0; transform: scale(1.05); }
        .top-btn.active { background: #fff3e0; border-color: #ff9800; color: #e65100; }

        /* Progress Bar */
        .progress-container {
            width: 100%;
            height: 10px;
            background: #e0e0e0;
            border-radius: 5px;
            margin: 6px 0 12px 0;
            overflow: hidden;
        }
        .progress-bar {
            height: 100%;
            width: 5%;
            background: linear-gradient(90deg, #4CAF50, #8BC34A);
            border-radius: 5px;
            transition: width 0.4s ease;
        }

        /* Instruction */
        .instruction-box {
            text-align: center;
            margin-bottom: 12px;
        }
        .instruction-text {
            font-size: 1.2em;
            color: #d84315;
            font-weight: bold;
        }
        .sub-instruction {
            font-size: 0.9em;
            color: #666;
        }

        /* Question Card */
        .question-card-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 6px 0 14px 0;
        }

        .question-card {
            background: linear-gradient(135deg, #fffdf5 0%, #f0f9ff 100%);
            border: 4px solid #ffb300;
            border-radius: 22px;
            padding: 20px 26px;
            width: 100%;
            text-align: center;
            box-shadow: 0 8px 20px rgba(255, 179, 0, 0.18);
            position: relative;
        }

        .question-meta-row {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 12px;
        }

        .cat-tag {
            display: inline-block;
            background: #ffe082;
            color: #795548;
            font-size: 0.85em;
            font-weight: bold;
            padding: 3px 12px;
            border-radius: 12px;
        }

        .qid-tag {
            display: inline-block;
            background: #e3f2fd;
            color: #1565c0;
            font-size: 0.85em;
            font-weight: bold;
            padding: 3px 10px;
            border-radius: 12px;
            border: 1px solid #90caf9;
        }

        .sentence-prompt {
            font-size: 1.48em;
            font-weight: 700;
            color: #1a237e;
            line-height: 1.55;
            margin: 6px 0;
            user-select: text;
        }

        .blank-pill {
            display: inline-block;
            min-width: 96px;
            padding: 2px 14px;
            margin: 0 4px;
            border-bottom: 3.5px solid #ff6f00;
            background: #fff8e1;
            color: #e65100;
            border-radius: 10px;
            font-weight: 900;
            letter-spacing: 1px;
            transition: all 0.25s ease;
        }

        .blank-pill.filled {
            background: #c8e6c9;
            border-bottom-color: #2e7d32;
            color: #1b5e20;
            box-shadow: 0 2px 8px rgba(46, 125, 50, 0.25);
        }

        /* 4 Options Grid */
        .options-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 14px;
            width: 100%;
            margin-bottom: 12px;
        }

        .option-btn {
            background: #ffffff;
            border: 3px solid #2196F3;
            border-radius: 18px;
            padding: 15px 18px;
            font-size: 1.38em;
            font-weight: bold;
            color: #1565c0;
            cursor: pointer;
            transition: all 0.18s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 5px 0 #1976D2;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            gap: 14px;
            position: relative;
        }

        .option-btn:hover:not(:disabled) {
            transform: translateY(-3px);
            background: #e3f2fd;
            box-shadow: 0 8px 0 #1565c0;
        }

        .option-btn:active:not(:disabled) {
            transform: translateY(3px);
            box-shadow: 0 2px 0 #1565c0;
        }

        .option-btn:disabled { cursor: default; }

        .option-badge {
            background: #2196F3;
            color: white;
            width: 34px;
            height: 34px;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 0.78em;
            flex-shrink: 0;
        }

        .option-btn.correct {
            background: #4CAF50 !important;
            border-color: #2E7D32 !important;
            color: white !important;
            box-shadow: 0 5px 0 #1B5E20 !important;
            animation: pop 0.4s ease;
        }
        .option-btn.correct .option-badge { background: #1B5E20; }

        .option-btn.incorrect {
            background: #ef5350 !important;
            border-color: #c62828 !important;
            color: white !important;
            box-shadow: 0 5px 0 #b71c1c !important;
            animation: shake 0.4s ease;
        }
        .option-btn.incorrect .option-badge { background: #b71c1c; }

        .option-btn.grayed-out {
            opacity: 0.48;
            transform: scale(0.97);
        }

        /* Feedback Banner & Learning Card */
        .feedback-area {
            min-height: 32px;
            text-align: center;
            font-size: 1.15em;
            font-weight: bold;
            margin-bottom: 8px;
        }

        .learning-card {
            display: none;
            background: #e8f5e9;
            border: 2.5px solid #66bb6a;
            border-radius: 16px;
            padding: 14px 20px;
            margin-top: 4px;
            text-align: left;
            animation: fadeIn 0.35s ease;
        }

        .learning-card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 6px;
        }

        .learning-word {
            font-size: 1.25em;
            font-weight: bold;
            color: #1b5e20;
        }

        .learning-example-bm {
            font-size: 1.05em;
            color: #0d47a1;
            font-weight: 700;
            margin: 4px 0;
        }
        .learning-example-zh {
            font-size: 0.98em;
            color: #37474f;
            margin: 3px 0;
        }
        .learning-explain-zh {
            font-size: 0.94em;
            color: #5d4037;
            background: #fff8e1;
            border-left: 4px solid #ffb300;
            padding: 6px 10px;
            border-radius: 6px;
            margin-top: 6px;
        }

        .next-btn {
            display: none;
            margin: 12px auto 0 auto;
            background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 12px 35px;
            font-size: 1.2em;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(245, 124, 0, 0.4);
            transition: all 0.2s;
        }
        .next-btn:hover { transform: scale(1.06); }

        /* Welcome / Login Modal */
        .name-modal-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.65);
            backdrop-filter: blur(4px);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 200;
            padding: 16px;
        }

        .name-modal-card {
            background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%);
            border: 5px solid #4CAF50;
            border-radius: 26px;
            padding: 28px 26px;
            width: 440px;
            max-width: 95vw;
            text-align: center;
            box-shadow: 0 18px 45px rgba(0, 0, 0, 0.35);
            animation: pop 0.4s ease;
        }

        .name-modal-icon { font-size: 3em; margin-bottom: 4px; }
        .name-modal-title {
            font-size: 1.55em;
            font-weight: 900;
            color: #1565c0;
            margin: 0 0 6px 0;
        }
        .name-modal-subtitle {
            font-size: 0.95em;
            color: #555;
            margin: 0 0 14px 0;
        }

        .name-input-box {
            width: 100%;
            padding: 12px 16px;
            font-size: 1.1em;
            font-weight: bold;
            text-align: center;
            border: 3px solid #2196F3;
            border-radius: 16px;
            outline: none;
            color: #1a237e;
            background: #ffffff;
            margin-bottom: 12px;
        }
        .name-input-box:focus {
            border-color: #ff9800;
            box-shadow: 0 0 0 4px rgba(255, 152, 0, 0.2);
        }

        .start-challenge-btn {
            background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
            color: white;
            border: none;
            border-radius: 24px;
            padding: 12px 32px;
            font-size: 1.15em;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 6px 18px rgba(46, 125, 50, 0.35);
            transition: all 0.2s;
            width: 100%;
        }
        .start-challenge-btn:hover { transform: scale(1.03); }

        .auth-tabs {
            display: flex;
            gap: 6px;
            background: #e3f2fd;
            padding: 5px;
            border-radius: 16px;
            margin-bottom: 16px;
        }
        .auth-tab {
            flex: 1;
            border: none;
            background: transparent;
            padding: 8px 6px;
            border-radius: 12px;
            font-weight: 800;
            font-size: 0.92em;
            color: #1565c0;
            cursor: pointer;
            transition: all 0.2s;
        }
        .auth-tab.active {
            background: #ffffff;
            color: #0d47a1;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
        }
        .auth-panel { display: none; }
        .auth-panel.active { display: block; }
        .auth-error {
            color: #c62828;
            font-size: 0.9em;
            font-weight: bold;
            min-height: 20px;
            margin-bottom: 8px;
        }

        /* History Modal */
        .history-modal-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.65);
            backdrop-filter: blur(4px);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 210;
            padding: 16px;
        }
        .history-modal-card {
            background: #ffffff;
            border: 5px solid #2196F3;
            border-radius: 24px;
            padding: 22px;
            width: 680px;
            max-width: 96vw;
            max-height: 86vh;
            display: flex;
            flex-direction: column;
            gap: 14px;
            box-shadow: 0 18px 45px rgba(0, 0, 0, 0.35);
            animation: pop 0.3s ease;
        }
        .history-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #e3f2fd;
            padding-bottom: 10px;
        }
        .history-stats-row {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
        }
        .history-stat-box {
            background: #f0f9ff;
            border: 2px solid #bbdefb;
            border-radius: 14px;
            padding: 10px;
            text-align: center;
        }
        .history-stat-val { font-size: 1.5em; font-weight: 900; color: #1565c0; }
        .history-stat-lbl { font-size: 0.85em; color: #546e7a; font-weight: bold; }
        .history-list {
            overflow-y: auto;
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 10px;
            padding-right: 4px;
        }
        .history-item {
            background: #fafafa;
            border: 2px solid #e0e0e0;
            border-radius: 14px;
            padding: 12px 14px;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        .history-item-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 8px;
            font-weight: bold;
        }
        .wrong-word-pill {
            display: inline-block;
            background: #ffebee;
            color: #c62828;
            border: 1px solid #ef9a9a;
            border-radius: 10px;
            padding: 2px 8px;
            font-size: 0.85em;
            font-weight: bold;
            margin: 2px 4px 2px 0;
        }
        .cloud-status-badge {
            font-size: 0.92em;
            font-weight: bold;
            padding: 6px 14px;
            border-radius: 12px;
            background: #e8f5e9;
            color: #2e7d32;
            border: 1px solid #a5d6a7;
        }

        /* Celebration Overlay */
        .celebrate-overlay {
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(255, 255, 255, 0.96);
            z-index: 100;
            display: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 25px;
            border-radius: 18px;
            animation: fadeIn 0.5s ease;
        }

        .celebrate-title {
            font-size: 2.3em;
            color: #ff6f00;
            margin: 8px 0;
            font-weight: 900;
        }

        .celebrate-player-badge {
            background: linear-gradient(135deg, #fff8e1 0%, #ffe082 100%);
            border: 3px solid #ffb300;
            color: #e65100;
            font-size: 1.5em;
            font-weight: 900;
            padding: 6px 26px;
            border-radius: 24px;
            margin: 6px 0 4px 0;
            box-shadow: 0 4px 12px rgba(255, 179, 0, 0.28);
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .celebrate-stats {
            background: #f1f8e9;
            border: 3px solid #8bc34a;
            border-radius: 18px;
            padding: 15px 30px;
            margin: 15px 0;
            font-size: 1.2em;
            line-height: 1.8;
            color: #33691e;
            font-weight: bold;
        }

        .celebrate-buttons {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 10px;
        }

        .action-round-btn {
            padding: 12px 26px;
            font-size: 1.15em;
            font-weight: bold;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            color: white;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s;
        }
        .action-round-btn:hover { transform: scale(1.06); }

        @keyframes pop {
            0% { transform: scale(0.92); }
            50% { transform: scale(1.04); }
            100% { transform: scale(1); }
        }
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-8px); }
            75% { transform: translateX(8px); }
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @media (max-width: 650px) {
            body { padding: 4px; }
            .game-area {
                padding: 12px;
                border-width: 4px;
                border-radius: 18px;
                min-height: auto;
            }
            .top-bar { gap: 6px; padding-bottom: 6px; }
            .level-badge { font-size: 0.98em; padding: 5px 12px; gap: 8px; }
            .control-buttons { gap: 5px; width: 100%; justify-content: space-between; }
            .category-select { font-size: 0.84em; padding: 5px 8px; flex: 1; min-width: 120px; }
            .top-btn { font-size: 0.84em; padding: 5px 8px; }
            .sentence-prompt { font-size: 1.18em; }
            .options-grid { grid-template-columns: 1fr; gap: 10px; }
            .option-btn { padding: 12px 14px; font-size: 1.2em; border-radius: 14px; }
            .celebrate-buttons { flex-direction: column; width: 90%; }
            .action-round-btn { width: 100%; font-size: 1.05em; padding: 10px 15px; }
        }
    </style>
</head>
<body>

    <!-- Audio SFX -->
    <audio id="sfx-correct"><source src="correct.mp3" type="audio/mpeg"></audio>
    <audio id="sfx-wrong"><source src="wrong.mp3" type="audio/mpeg"></audio>
    <audio id="sfx-timeout"><source src="timeout.mp3" type="audio/mpeg"></audio>
    <audio id="bgm-music" loop><source src="bgm.mp3" type="audio/mpeg"></audio>

    <div class="game-area" id="game-area">
        <!-- Welcome / Login Modal -->
        <div class="name-modal-overlay" id="name-modal-overlay">
            <div class="name-modal-card">
                <div class="name-modal-icon">🌟</div>
                <h2 class="name-modal-title">华小国语人称代词连连乐<br><span style="font-size:0.72em; color:#2e7d32;">Kata Ganti Nama Diri</span></h2>

                <div class="auth-tabs">
                    <button class="auth-tab active" id="tab-login" onclick="switchAuthTab('login')">🔑 学生登录</button>
                    <button class="auth-tab" id="tab-guest" onclick="switchAuthTab('guest')">🚀 游客试玩</button>
                </div>

                <!-- Tab 1: Login -->
                <div class="auth-panel active" id="panel-login">
                    <p class="name-modal-subtitle">请输入老师分配的账号与密码登录，自动保存学习记录！</p>
                    <input type="text" class="name-input-box" id="login-name-input" placeholder="登录账号 (例: johnny)" maxlength="20" onkeydown="if(event.key==='Enter') document.getElementById('login-pin-input').focus()">
                    <input type="password" inputmode="numeric" class="name-input-box" id="login-pin-input" placeholder="密码 / PIN (例: 1234)" maxlength="12" onkeydown="if(event.key==='Enter') loginStudent()">
                    <div class="auth-error" id="login-error"></div>
                    <button class="start-challenge-btn" id="btn-login-submit" onclick="loginStudent()">🔑 登录并开始第一题 ➔</button>
                </div>

                <!-- Tab 2: Guest -->
                <div class="auth-panel" id="panel-guest">
                    <p class="name-modal-subtitle">无需账号直接练习（不保存到云端记录）</p>
                    <input type="text" class="name-input-box" id="player-name-input" placeholder="输入你的名字 (例: Johnny / Ali)..." maxlength="15" onkeydown="if(event.key==='Enter') confirmPlayerName()">
                    <button class="start-challenge-btn" onclick="confirmPlayerName()">🚀 开始第一题 (Start) ➔</button>
                </div>
            </div>
        </div>

        <!-- Student History Modal -->
        <div class="history-modal-overlay" id="history-modal-overlay" onclick="if(event.target===this) closeHistoryModal()">
            <div class="history-modal-card">
                <div class="history-header">
                    <h2 style="margin:0; color:#1565c0; font-size:1.3em;">📊 学习记录与错题本 (<span id="hist-player-title"></span>)</h2>
                    <button class="top-btn" onclick="closeHistoryModal()">✖ 关闭</button>
                </div>
                <div class="history-stats-row">
                    <div class="history-stat-box">
                        <div class="history-stat-val" id="hist-total-rounds">0</div>
                        <div class="history-stat-lbl">完成练习组数</div>
                    </div>
                    <div class="history-stat-box">
                        <div class="history-stat-val" id="hist-avg-acc">0%</div>
                        <div class="history-stat-lbl">平均正确率</div>
                    </div>
                    <div class="history-stat-box">
                        <div class="history-stat-val" id="hist-total-correct">0</div>
                        <div class="history-stat-lbl">累计答对题数</div>
                    </div>
                </div>
                <div class="history-list" id="history-list">
                    <p style="text-align:center; color:#777;">正在加载记录...</p>
                </div>
                <div style="display:flex; justify-content:space-between; align-items:center; padding-top:6px; border-top:1px solid #eee;">
                    <span id="hist-account-mode" style="font-size:0.88em; color:#546e7a; font-weight:bold;"></span>
                    <button class="top-btn" onclick="switchAccount()">🔄 切换账号 / 退出登录</button>
                </div>
            </div>
        </div>

        <!-- Mid-Quiz Quit Warning Modal -->
        <div class="history-modal-overlay" id="quit-warn-overlay" style="z-index:220;">
            <div class="history-modal-card" style="max-width:440px; text-align:center; padding:24px 22px;">
                <div style="font-size:2.6em; margin-bottom:6px;">⚠️</div>
                <h2 style="margin:0 0 8px 0; color:#e65100; font-size:1.35em;">测验尚未完成！(Quiz Not Finished)</h2>
                <p style="margin:0 0 14px 0; color:#455a64; font-size:0.95em;">你正在作答中，确定要中途退出吗？</p>
                <div style="background:#fff8e1; border:2px solid #ffe082; border-radius:14px; padding:14px; margin-bottom:16px;">
                    <div style="font-size:1.25em; font-weight:900; color:#1565c0; margin-bottom:6px;" id="quit-warn-progress">当前进度：0 / 20</div>
                    <div style="font-size:1.05em; font-weight:800; display:flex; justify-content:center; gap:18px;">
                        <span style="color:#2e7d32;">✅ 答对：<span id="quit-warn-correct">0</span></span>
                        <span style="color:#c62828;">❌ 答错：<span id="quit-warn-wrong">0</span></span>
                    </div>
                </div>
                <p style="margin:0 0 16px 0; font-size:0.85em; color:#78909c;">☁️ 当前作答进度与错题已实时保存至云端。</p>
                <div style="display:flex; gap:10px; justify-content:center; flex-wrap:wrap;">
                    <button class="action-round-btn" style="background:linear-gradient(135deg,#43a047,#2e7d32); padding:10px 22px; font-size:1em;" onclick="cancelQuitQuiz()">▶️ 继续作答 (Continue)</button>
                    <button class="action-round-btn" style="background:linear-gradient(135deg,#e53935,#c62828); padding:10px 22px; font-size:1em;" onclick="confirmQuitQuiz()">🚪 确定退出 (Quit)</button>
                </div>
            </div>
        </div>

        <!-- Top status bar -->
        <div class="top-bar">
            <div class="level-wrapper">
                <div class="user-name-tag" id="user-name-display" title="点击可修改名字" onclick="editUserName()">
                    <span class="user-avatar">👤</span> <span id="display-user-name"></span>
                </div>
                <div class="level-badge">
                    <span id="level-text">第 1 题 / 共 20 题</span>
                    <div class="score-box">
                        <span class="score-item score-betul">✅ <span id="score-b">0</span></span>
                        <span class="score-item score-salah">❌ <span id="score-s">0</span></span>
                    </div>
                </div>
            </div>

            <div class="control-buttons">
                <select class="category-select" id="category-filter" onchange="onCategoryFilterChange()">
                    <option value="ALL">🌟 全部题目 (All)</option>
                </select>

                <button class="top-btn" id="history-btn" onclick="openHistoryModal()">📊 记录</button>
                <button class="top-btn" id="sfx-toggle-btn" onclick="toggleSFX()">🔊 音效</button>
                <button class="top-btn" id="bgm-toggle-btn" onclick="toggleBGM()">🎵 音乐</button>
                <button class="top-btn" id="quit-quiz-btn" style="color:#c62828; border-color:#ef9a9a;" onclick="requestQuitQuiz('reset')">🚪 退出</button>
            </div>
        </div>

        <!-- Progress Bar -->
        <div class="progress-container">
            <div class="progress-bar" id="progress-bar"></div>
        </div>

        <!-- Assigned Quiz Banner -->
        <div id="assigned-quiz-banner" style="display:none; background:linear-gradient(135deg,#e3f2fd,#ede7f6); border:2px solid #5c6bc0; border-radius:14px; padding:10px 14px; margin:8px 0; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:8px;">
            <div id="assigned-quiz-text" style="font-weight:800; color:#283593; font-size:0.95em;"></div>
            <div id="assigned-quiz-actions" style="display:flex; gap:8px; flex-wrap:wrap;"></div>
        </div>

        <!-- Instructions -->
        <div class="instruction-box">
            <div class="instruction-text">请细读句子，选出最正确的人称代词 (Kata Ganti Nama Diri) 填入空格！</div>
            <div class="sub-instruction">Baca ayat di bawah dan pilih Kata Ganti Nama Diri yang paling sesuai.</div>
        </div>

        <!-- Central Question Prompt (Fill-in-the-Blank Sentence) -->
        <div class="question-card-container">
            <div class="question-card" id="question-card">
                <div class="question-meta-row">
                    <span class="cat-tag" id="cat-tag">Group A</span>
                    <span class="qid-tag" id="qid-tag">A001</span>
                </div>
                <div class="sentence-prompt" id="sentence-prompt">...</div>
            </div>
        </div>

        <!-- 4 Multiple Choice Options -->
        <div class="options-grid" id="options-grid"></div>

        <!-- Feedback & Learning Card -->
        <div class="feedback-area" id="feedback-banner"></div>

        <div class="learning-card" id="learning-card">
            <div class="learning-card-header">
                <span class="learning-word">✅ 正确答案：<span id="card-answer"></span></span>
            </div>
            <div class="learning-example-bm" id="card-complete-bm"></div>
            <div class="learning-example-zh" id="card-translation-zh"></div>
            <div class="learning-explain-zh" id="card-explain-zh"></div>
        </div>

        <button class="next-btn" id="next-btn" onclick="nextQuestion()">下一题 (Next Question) ➔</button>

        <!-- Celebration Screen -->
        <div class="celebrate-overlay" id="celebrate-screen">
            <div style="font-size: 4em; margin-bottom: 4px;">🏆🎉</div>
            <div class="celebrate-player-badge">👤 <span id="celebrate-player-name">同学</span></div>
            <h1 class="celebrate-title">Tahniah! 恭喜完成本组练习！</h1>
            <p style="font-size: 1.15em; color: #555; margin: 4px 0;"><strong id="final-user-name"></strong> 太棒了！你已经掌握了这些国语人称代词！</p>
            <div class="celebrate-stats">
                ✅ 一次答对：<span id="final-correct">0</span> / <span id="final-total">20</span> 题<br>
                ❌ 答错次数：<span id="final-wrong">0</span> 次<br>
                🎯 正确率：<span id="final-accuracy">100%</span>
            </div>
            <div class="cloud-status-badge" id="cloud-save-status">☁️ 正在同步成绩...</div>
            <div class="celebrate-buttons">
                <button class="action-round-btn" style="background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%);" onclick="startNewSet()">▶️ 开始新的一组 20 题 (New Set)</button>
                <button class="action-round-btn" style="background: linear-gradient(135deg, #4caf50 0%, #388e3c 100%);" onclick="repeatCurrentSet()">🔄 重温本组 20 题 (Repeat Set)</button>
                <button class="action-round-btn" style="background: linear-gradient(135deg, #1e88e5 0%, #1565c0 100%);" onclick="openHistoryModal()">📊 我的记录 (History)</button>
            </div>
        </div>
    </div>

    <!-- Embedded Fallback Data -->
    <script id="embedded-data" type="application/json">
''' + json_str + '''
    </script>

    <script>
        const QUESTIONS_PER_SET = 20;
        const SUPABASE_URL = "https://kuybhocpdsttmmjkihcv.supabase.co";
        const SUPABASE_KEY = "sb_publishable_kdVxbLe5qMPNkjMhccq52w_ia8RseMQ";

        // Synonym exclusion groups: words in the same group must NEVER appear together in 4 choices
        const SYNONYM_GROUPS = [
            ["awak", "anda", "kamu", "engkau"],
            ["saya", "aku"]
        ];

        // Default pronoun pool used as fallback if a question has fewer than 3 distractors
        const DEFAULT_PRONOUN_POOL = [
            "saya", "kamu", "beliau", "mereka", "kita",
            "kami", "kalian", "dia", "baginda", "patik",
            "beta", "tuanku"
        ];

        let currentStudentId = null;
        let currentUsername = "";
        let currentClassName = "";
        let currentUserName = "";
        let isNameConfirmed = false;
        let quizStartTime = Date.now();
        let wrongWordsThisSet = [];
        let sessionHistory = [];

        async function sbFetch(path, options = {}) {
            const headers = {
                "apikey": SUPABASE_KEY,
                "Authorization": "Bearer " + SUPABASE_KEY,
                "Content-Type": "application/json",
                ...(options.headers || {})
            };
            const res = await fetch(SUPABASE_URL + "/rest/v1/" + path, { ...options, headers });
            const text = await res.text();
            let data = null;
            try { data = text ? JSON.parse(text) : null; } catch (e) { data = text; }
            if (!res.ok) {
                throw new Error((data && (data.message || data.hint || data.details)) || ("HTTP " + res.status));
            }
            return data;
        }

        function switchAuthTab(tab) {
            ['login', 'guest'].forEach(t => {
                document.getElementById('tab-' + t).classList.toggle('active', t === tab);
                document.getElementById('panel-' + t).classList.toggle('active', t === tab);
            });
            document.getElementById('login-error').textContent = "";
            setTimeout(() => {
                if (tab === 'login') document.getElementById('login-name-input').focus();
                else document.getElementById('player-name-input').focus();
            }, 50);
        }

        async function loginStudent() {
            const nameRaw = document.getElementById('login-name-input').value.trim();
            const pin = document.getElementById('login-pin-input').value.trim();
            const errEl = document.getElementById('login-error');
            const btn = document.getElementById('btn-login-submit');
            errEl.textContent = "";

            if (!nameRaw || !pin) {
                errEl.textContent = "请输入账号和密码！";
                return;
            }
            const uname = nameRaw.toLowerCase().replace(/\s+/g, '');
            btn.disabled = true;
            btn.textContent = "⏳ 正在登录...";
            try {
                const rows = await sbFetch(`students?username=eq.${encodeURIComponent(uname)}&select=*`);
                if (!rows || rows.length === 0) {
                    errEl.textContent = "❌ 找不到该账号，请联系老师创建账号";
                    return;
                }
                const stu = rows[0];
                if (stu.is_active === false) {
                    errEl.textContent = "⏸️ 该账号已被老师停用，请联系老师";
                    return;
                }
                if (stu.pin !== pin) {
                    errEl.textContent = "❌ 密码错误，请重试";
                    return;
                }
                currentStudentId = stu.id;
                currentUsername = stu.username;
                currentUserName = stu.display_name;
                currentClassName = stu.class_name || "";
                pendingResumeState = stu.active_quiz_state_kgnd || null;
                localStorage.setItem('kgnd_auth', JSON.stringify({ id: stu.id, username: stu.username, display_name: stu.display_name, class_name: stu.class_name }));
                sbFetch(`students?id=eq.${stu.id}`, { method: "PATCH", body: JSON.stringify({ last_login: new Date().toISOString() }) }).catch(() => {});
                await finishAuthEnterGame();
            } catch (err) {
                errEl.textContent = "⚠️ 连接失败：" + err.message;
            } finally {
                btn.disabled = false;
                btn.textContent = "🔑 登录并开始第一题 ➔";
            }
        }

        function confirmPlayerName() {
            const input = document.getElementById('player-name-input');
            const val = input.value.trim();
            currentStudentId = null;
            currentUsername = "";
            currentClassName = "";
            currentUserName = val || "同学 (Murid)";
            finishAuthEnterGame();
        }

        async function finishAuthEnterGame() {
            isNameConfirmed = true;
            updateUserNameDisplay();
            document.getElementById('name-modal-overlay').style.display = 'none';

            if (bgmEnabled) {
                bgmAudio.play().catch(() => {});
            }

            if (currentStudentId) {
                await loadPendingAssignments(currentStudentId);
            } else {
                pendingAssignments = [];
                activeAssignment = null;
                renderAssignedQuizBanner();
            }

            if (pendingResumeState && Array.isArray(pendingResumeState.pool_ids) && pendingResumeState.pool_ids.length > 0 && pendingResumeState.current_index < pendingResumeState.pool_ids.length) {
                const st = pendingResumeState;
                pendingResumeState = null;
                resumeIncompleteQuiz(st);
            } else {
                isForcedResume = false;
                setQuizLockUI(false);
                if (allVocabulary.length > 0) {
                    startNewSet();
                }
            }
        }

        function switchAccount() {
            if (isForcedResume) {
                alert("🔒 你有一份尚未完成的测验，请先完成测验后才能切换账号！");
                return;
            }
            closeHistoryModal();
            localStorage.removeItem('kgnd_auth');
            currentStudentId = null;
            currentUsername = "";
            currentClassName = "";
            currentUserName = "";
            isNameConfirmed = false;
            pendingAssignments = [];
            activeAssignment = null;
            pendingResumeState = null;
            isForcedResume = false;
            setQuizLockUI(false);
            renderAssignedQuizBanner();
            document.getElementById('login-pin-input').value = "";
            document.getElementById('name-modal-overlay').style.display = 'flex';
            switchAuthTab('login');
        }

        function updateUserNameDisplay() {
            const label = currentClassName ? `${currentUserName} (${currentClassName})` : (currentUserName || "同学 (Murid)");
            const displayEl = document.getElementById('display-user-name');
            if (displayEl) displayEl.textContent = label;
            const celebNameEl = document.getElementById('celebrate-player-name');
            if (celebNameEl) celebNameEl.textContent = currentUserName || "同学 (Murid)";
            const finalNameEl = document.getElementById('final-user-name');
            if (finalNameEl) finalNameEl.textContent = currentUserName || "同学 (Murid)";
        }

        function editUserName() {
            if (currentStudentId) {
                openHistoryModal();
                return;
            }
            const newName = prompt("请输入你的名字 / Sila masukkan nama anda:", currentUserName || "");
            if (newName !== null && newName.trim()) {
                currentUserName = newName.trim();
                updateUserNameDisplay();
            }
        }

        let allVocabulary = [];
        let activePool = [];
        let savedCurrentSet = [];
        let pendingAssignments = [];
        let activeAssignment = null;
        let currentIndex = 0;
        let currentQuestion = null;
        let gameActive = false;

        let scoreBetul = 0;
        let scoreSalah = 0;
        let hasMadeMistakeThisRound = false;
        let currentHistoryRowId = null;
        let liveSyncPromise = Promise.resolve();
        let pendingResumeState = null;
        let isForcedResume = false;
        let lastConfirmedCategory = "ALL";
        let pendingQuitAction = null;

        function setQuizLockUI(locked) {
            const catSel = document.getElementById('category-filter');
            const quitBtn = document.getElementById('quit-quiz-btn');
            if (catSel) catSel.disabled = !!locked;
            if (quitBtn) quitBtn.style.display = locked ? 'none' : 'inline-block';
        }

        function populateCategoryFilter() {
            const sel = document.getElementById('category-filter');
            if (!sel) return;
            const prev = sel.value || 'ALL';
            const catCounts = {};
            allVocabulary.forEach(item => {
                const c = item.category || 'Group A: Kata Ganti Nama Diri';
                catCounts[c] = (catCounts[c] || 0) + 1;
            });
            const cats = Object.keys(catCounts);
            let html = `<option value="ALL">🌟 全部题目 (All: ${allVocabulary.length}题)</option>`;
            cats.forEach(c => {
                html += `<option value="${c}">📘 ${c} (${catCounts[c]}题)</option>`;
            });
            sel.innerHTML = html;
            if (prev === 'ALL' || cats.includes(prev)) {
                sel.value = prev;
            }
        }

        function resumeIncompleteQuiz(st) {
            const vocabMap = {};
            allVocabulary.forEach(w => {
                if (w.id) vocabMap[w.id] = w;
            });
            let pool = st.pool_ids.map(id => vocabMap[id]).filter(Boolean);
            if (pool.length === 0) {
                isForcedResume = false;
                setQuizLockUI(false);
                startNewSet();
                return;
            }
            activePool = pool;
            savedCurrentSet = [...activePool];
            scoreBetul = st.score_correct || 0;
            scoreSalah = st.score_wrong || 0;
            currentIndex = Math.max(st.current_index || 0, scoreBetul + scoreSalah);
            wrongWordsThisSet = Array.isArray(st.wrong_words) ? st.wrong_words : [];
            currentHistoryRowId = st.history_row_id || null;
            quizStartTime = Date.now() - ((st.elapsed_sec || 0) * 1000);
            isForcedResume = true;

            if (st.assignment_id) {
                activeAssignment = pendingAssignments.find(a => a.id === st.assignment_id) || {
                    id: st.assignment_id,
                    quiz_code: st.quiz_code || "测验",
                    attempt_no: 1,
                    quizzes_kgnd: { question_count: activePool.length }
                };
            } else {
                activeAssignment = null;
                const catSel = document.getElementById('category-filter');
                if (catSel && st.category) {
                    catSel.value = st.category;
                    lastConfirmedCategory = st.category;
                }
            }

            document.getElementById('score-b').textContent = scoreBetul;
            document.getElementById('score-s').textContent = scoreSalah;
            document.getElementById('celebrate-screen').style.display = 'none';
            setQuizLockUI(true);
            renderAssignedQuizBanner();
            loadNextQuestion();
        }

        function isQuizInProgress() {
            const celebrateEl = document.getElementById('celebrate-screen');
            const isCelebrating = celebrateEl && celebrateEl.style.display === 'flex';
            return activePool.length > 0 && (scoreBetul + scoreSalah) > 0 && currentIndex < activePool.length && !isCelebrating;
        }

        function onCategoryFilterChange() {
            const sel = document.getElementById('category-filter');
            if (isForcedResume) {
                sel.value = lastConfirmedCategory;
                alert("🔒 请先完成上次未完成的测验，才能切换单元！");
                return;
            }
            if (isQuizInProgress()) {
                requestQuitQuiz('switch_cat');
            } else {
                lastConfirmedCategory = sel.value;
                startNewSet();
            }
        }

        function requestQuitQuiz(action) {
            if (isForcedResume) {
                alert("🔒 请先完成上次未完成的测验！");
                return;
            }
            if (!isQuizInProgress()) {
                startNewSet();
                return;
            }
            pendingQuitAction = action;
            const answered = scoreBetul + scoreSalah;
            const totalQ = activePool.length || QUESTIONS_PER_SET;
            document.getElementById('quit-warn-progress').textContent = `当前进度：${answered} / ${totalQ}`;
            document.getElementById('quit-warn-correct').textContent = scoreBetul;
            document.getElementById('quit-warn-wrong').textContent = scoreSalah;
            document.getElementById('quit-warn-overlay').style.display = 'flex';
        }

        function cancelQuitQuiz() {
            if (pendingQuitAction === 'switch_cat') {
                document.getElementById('category-filter').value = lastConfirmedCategory;
            }
            pendingQuitAction = null;
            document.getElementById('quit-warn-overlay').style.display = 'none';
        }

        function confirmQuitQuiz() {
            const action = pendingQuitAction;
            pendingQuitAction = null;
            document.getElementById('quit-warn-overlay').style.display = 'none';
            if (action === 'switch_cat') {
                lastConfirmedCategory = document.getElementById('category-filter').value;
            }
            startNewSet();
        }

        window.addEventListener('beforeunload', (e) => {
            if (isQuizInProgress()) {
                e.preventDefault();
                e.returnValue = '';
            }
        });

        let sfxEnabled = true;
        let bgmEnabled = false;
        const bgmAudio = document.getElementById('bgm-music');
        bgmAudio.volume = 0.22;

        function toggleSFX() {
            sfxEnabled = !sfxEnabled;
            const btn = document.getElementById('sfx-toggle-btn');
            btn.textContent = sfxEnabled ? "🔊 音效" : "🔇 静音";
        }

        function toggleBGM() {
            bgmEnabled = !bgmEnabled;
            const btn = document.getElementById('bgm-toggle-btn');
            if (bgmEnabled) {
                btn.textContent = "🎵 音乐开";
                btn.classList.add('active');
                bgmAudio.play().catch(() => {});
            } else {
                btn.textContent = "🎵 音乐";
                btn.classList.remove('active');
                bgmAudio.pause();
            }
        }

        function playSound(id) {
            if (!sfxEnabled) return;
            const el = document.getElementById(id);
            if (el) {
                el.currentTime = 0;
                el.play().catch(() => {});
            }
        }

        function shuffle(arr) {
            const a = [...arr];
            for (let i = a.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [a[i], a[j]] = [a[j], a[i]];
            }
            return a;
        }

        async function initGameData() {
            try {
                const res = await fetch('kata_ganti_nama_data.json', { cache: 'no-store' });
                if (res.ok) {
                    allVocabulary = await res.json();
                } else {
                    throw new Error("HTTP error");
                }
            } catch (err) {
                allVocabulary = JSON.parse(document.getElementById('embedded-data').textContent);
            }

            populateCategoryFilter();

            let restored = false;
            try {
                const saved = JSON.parse(localStorage.getItem('kgnd_auth') || 'null');
                if (saved && saved.id) {
                    const rows = await sbFetch(`students?id=eq.${saved.id}&select=*`);
                    if (rows && rows[0] && rows[0].is_active !== false) {
                        currentStudentId = rows[0].id;
                        currentUsername = rows[0].username;
                        currentUserName = rows[0].display_name;
                        currentClassName = rows[0].class_name || "";
                        pendingResumeState = rows[0].active_quiz_state_kgnd || null;
                        document.getElementById('name-modal-overlay').style.display = 'none';
                        await finishAuthEnterGame();
                        restored = true;
                    } else {
                        localStorage.removeItem('kgnd_auth');
                    }
                }
            } catch (e) {}
            if (!restored) {
                setTimeout(() => {
                    const inp = document.getElementById('login-name-input');
                    if (inp) inp.focus();
                }, 100);
            }
        }

        async function loadPendingAssignments(studentId) {
            try {
                const rows = await sbFetch(`quiz_assignments_kgnd?student_id=eq.${studentId}&status=eq.pending&order=assigned_at.asc&select=*,quizzes_kgnd(*)`);
                pendingAssignments = (rows || []).filter(r => r.quizzes_kgnd && r.quizzes_kgnd.is_archived !== true);
            } catch (err) {
                pendingAssignments = [];
            }
            renderAssignedQuizBanner();
        }

        function renderAssignedQuizBanner() {
            const banner = document.getElementById('assigned-quiz-banner');
            const textEl = document.getElementById('assigned-quiz-text');
            const actEl = document.getElementById('assigned-quiz-actions');
            if (!banner) return;
            if (!currentStudentId || pendingAssignments.length === 0) {
                banner.style.display = 'none';
                return;
            }
            banner.style.display = 'flex';
            if (activeAssignment) {
                const q = activeAssignment.quizzes_kgnd || {};
                const attemptLabel = (activeAssignment.attempt_no || 1) > 1 ? ` (第 ${activeAssignment.attempt_no} 次重做)` : '';
                textEl.innerHTML = `📝 正在作答老师派发的测验：<span style="color:#d84315;">${activeAssignment.quiz_code}${attemptLabel}</span> ${q.title ? `— ${q.title}` : ''}（共 ${activePool.length} 题）`;
                actEl.innerHTML = isForcedResume
                    ? `<span style="font-size:0.85em; color:#c62828; font-weight:bold;">🔒 请完成此测验</span>`
                    : `<button class="top-btn" onclick="exitAssignedQuiz()" style="background:#fff3e0; border-color:#ff9800; color:#e65100;">↩️ 返回自由练习</button>`;
            } else {
                textEl.innerHTML = `📢 老师派发了 <strong>${pendingAssignments.length}</strong> 份待完成测验！请点击开始：`;
                actEl.innerHTML = pendingAssignments.map(a => {
                    const q = a.quizzes_kgnd || {};
                    const att = (a.attempt_no || 1) > 1 ? ` (第${a.attempt_no}次)` : '';
                    return `<button class="top-btn" onclick="startAssignedQuiz('${a.id}')" style="background:#3949ab; color:#fff; border-color:#283593;">📝 开始 ${a.quiz_code}${att} (${q.question_count || 20}题)</button>`;
                }).join('');
            }
        }

        function startAssignedQuiz(assignmentId) {
            if (isForcedResume) {
                alert("🔒 请先完成当前未完成的测验！");
                return;
            }
            const assign = pendingAssignments.find(a => a.id === assignmentId);
            if (!assign || !assign.quizzes_kgnd) return;
            activeAssignment = assign;
            const q = assign.quizzes_kgnd;
            const idSet = Array.isArray(q.question_ids) ? q.question_ids : [];
            const vocabMap = {};
            allVocabulary.forEach(w => {
                if (w.id) vocabMap[w.id] = w;
            });
            let pool = idSet.map(id => vocabMap[id]).filter(Boolean);
            if (pool.length === 0) {
                const units = Array.isArray(q.units) ? q.units : [];
                const unitFiltered = allVocabulary.filter(w => units.includes(w.category));
                pool = shuffle(unitFiltered).slice(0, q.question_count || 20);
            } else {
                pool = shuffle(pool);
            }
            activePool = pool;
            savedCurrentSet = [...activePool];
            currentIndex = 0;
            scoreBetul = 0;
            scoreSalah = 0;
            quizStartTime = Date.now();
            wrongWordsThisSet = [];
            currentHistoryRowId = null;
            document.getElementById('score-b').textContent = "0";
            document.getElementById('score-s').textContent = "0";
            document.getElementById('celebrate-screen').style.display = 'none';
            renderAssignedQuizBanner();
            loadNextQuestion();
        }

        function exitAssignedQuiz() {
            if (isForcedResume) {
                alert("🔒 请先完成当前未完成的测验！");
                return;
            }
            activeAssignment = null;
            renderAssignedQuizBanner();
            startNewSet();
        }

        function startNewSet() {
            activeAssignment = null;
            renderAssignedQuizBanner();
            const selectedCat = document.getElementById('category-filter').value;
            let filtered = selectedCat === "ALL"
                ? [...allVocabulary]
                : allVocabulary.filter(item => item.category === selectedCat);

            const shuffled = shuffle(filtered);
            const setLimit = Math.min(QUESTIONS_PER_SET, shuffled.length);
            activePool = shuffled.slice(0, setLimit);
            savedCurrentSet = [...activePool];

            currentIndex = 0;
            scoreBetul = 0;
            scoreSalah = 0;
            quizStartTime = Date.now();
            wrongWordsThisSet = [];
            currentHistoryRowId = null;
            document.getElementById('score-b').textContent = "0";
            document.getElementById('score-s').textContent = "0";
            document.getElementById('celebrate-screen').style.display = 'none';

            loadNextQuestion();
        }

        function repeatCurrentSet() {
            activePool = shuffle([...savedCurrentSet]);
            currentIndex = 0;
            scoreBetul = 0;
            scoreSalah = 0;
            quizStartTime = Date.now();
            wrongWordsThisSet = [];
            currentHistoryRowId = null;
            document.getElementById('score-b').textContent = "0";
            document.getElementById('score-s').textContent = "0";
            document.getElementById('celebrate-screen').style.display = 'none';

            loadNextQuestion();
        }

        function getSynonymGroupIndex(word) {
            const low = (word || '').trim().toLowerCase();
            for (let i = 0; i < SYNONYM_GROUPS.length; i++) {
                if (SYNONYM_GROUPS[i].includes(low)) return i;
            }
            return -1;
        }

        function matchCase(word, template) {
            if (!word) return "";
            const isCap = template && template[0] === template[0].toUpperCase() && template[0] !== template[0].toLowerCase();
            if (isCap) {
                return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
            }
            return word.toLowerCase();
        }

        // Distractor generator strictly enforcing synonym-group exclusion:
        // Never put (awak, anda, kamu) together or (saya, aku) together!
        function generateOptions(correctItem) {
            const ans = (correctItem.answer || "").trim();
            const ansLower = ans.toLowerCase();
            const usedWords = new Set([ansLower]);
            const usedGroups = new Set();
            const ansGroup = getSynonymGroupIndex(ansLower);
            if (ansGroup !== -1) usedGroups.add(ansGroup);

            const distractors = [];
            const preset = Array.isArray(correctItem.distractors) ? correctItem.distractors : [];

            for (const d of preset) {
                const dClean = (d || "").trim();
                const dLower = dClean.toLowerCase();
                if (!dLower || usedWords.has(dLower)) continue;
                const g = getSynonymGroupIndex(dLower);
                if (g !== -1 && usedGroups.has(g)) continue;
                usedWords.add(dLower);
                if (g !== -1) usedGroups.add(g);
                distractors.push(matchCase(dClean, ans));
                if (distractors.length >= 3) break;
            }

            if (distractors.length < 3) {
                const candidatePool = shuffle([...DEFAULT_PRONOUN_POOL]);
                for (const d of candidatePool) {
                    const dLower = d.toLowerCase();
                    if (usedWords.has(dLower)) continue;
                    const g = getSynonymGroupIndex(dLower);
                    if (g !== -1 && usedGroups.has(g)) continue;
                    usedWords.add(dLower);
                    if (g !== -1) usedGroups.add(g);
                    distractors.push(matchCase(d, ans));
                    if (distractors.length >= 3) break;
                }
            }

            const choices = [
                { text: ans, isCorrect: true },
                ...distractors.slice(0, 3).map(t => ({ text: t, isCorrect: false }))
            ];
            return shuffle(choices);
        }

        function escapeHtml(str) {
            return String(str || '')
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;');
        }

        function renderSentenceWithBlank(sentence, filledAnswer) {
            const safe = escapeHtml(sentence);
            const blankRegex = /\\(\\s*_+\\s*\\)|_{3,}/g;
            if (filledAnswer) {
                return safe.replace(blankRegex, `<span class="blank-pill filled">${escapeHtml(filledAnswer)}</span>`);
            }
            return safe.replace(blankRegex, `<span class="blank-pill">________</span>`);
        }

        function loadNextQuestion() {
            if (currentIndex >= activePool.length) {
                showCelebration();
                return;
            }

            gameActive = true;
            hasMadeMistakeThisRound = false;
            currentQuestion = activePool[currentIndex];

            document.getElementById('level-text').textContent = `第 ${currentIndex + 1} 题 / 共 ${activePool.length} 题`;
            const progressPct = ((currentIndex + 1) / activePool.length) * 100;
            document.getElementById('progress-bar').style.width = `${progressPct}%`;

            document.getElementById('cat-tag').textContent = currentQuestion.category || "Kata Ganti Nama Diri";
            document.getElementById('qid-tag').textContent = currentQuestion.id || `#${currentIndex + 1}`;
            document.getElementById('sentence-prompt').innerHTML = renderSentenceWithBlank(currentQuestion.sentence, null);

            document.getElementById('feedback-banner').textContent = "";
            document.getElementById('learning-card').style.display = "none";
            document.getElementById('next-btn').style.display = "none";

            const choices = generateOptions(currentQuestion);
            const grid = document.getElementById('options-grid');
            grid.innerHTML = "";

            const letters = ["A", "B", "C", "D"];
            choices.forEach((choice, idx) => {
                const btn = document.createElement('button');
                btn.className = "option-btn";
                btn.innerHTML = `
                    <span class="option-badge">${letters[idx]}</span>
                    <span class="option-label">${escapeHtml(choice.text)}</span>
                `;
                btn.onclick = () => onSelectChoice(choice, btn);
                grid.appendChild(btn);
            });
        }

        function onSelectChoice(choice, btn) {
            if (!gameActive) return;

            const banner = document.getElementById('feedback-banner');
            const allOptionBtns = document.querySelectorAll('.option-btn');

            if (choice.isCorrect) {
                gameActive = false;
                playSound('sfx-correct');

                if (!hasMadeMistakeThisRound) {
                    scoreBetul++;
                    document.getElementById('score-b').textContent = scoreBetul;
                    syncLiveProgress();
                }

                btn.classList.add('correct');
                allOptionBtns.forEach(b => {
                    if (b !== btn) b.classList.add('grayed-out');
                    b.disabled = true;
                });

                // Fill the blank in the sentence prompt with the green highlighted answer
                document.getElementById('sentence-prompt').innerHTML = renderSentenceWithBlank(currentQuestion.sentence, currentQuestion.answer);

                banner.innerHTML = "🎉 太棒了！答对了！(Tahniah! Jawapan tepat!)";
                banner.style.color = "#2e7d32";

                // Populate Learning Card
                document.getElementById('card-answer').textContent = currentQuestion.answer;
                document.getElementById('card-complete-bm').innerHTML = renderSentenceWithBlank(currentQuestion.sentence, currentQuestion.answer);
                document.getElementById('card-translation-zh').textContent = currentQuestion.translation_zh ? `🇨🇳 句意：${currentQuestion.translation_zh}` : "";
                const explainEl = document.getElementById('card-explain-zh');
                if (currentQuestion.explanation_zh) {
                    explainEl.textContent = `💡 语法解析：${currentQuestion.explanation_zh}`;
                    explainEl.style.display = "block";
                } else {
                    explainEl.style.display = "none";
                }
                document.getElementById('learning-card').style.display = "block";
                document.getElementById('next-btn').style.display = "inline-block";
            } else {
                playSound('sfx-wrong');
                btn.classList.add('incorrect');
                btn.disabled = true;

                if (!hasMadeMistakeThisRound) {
                    hasMadeMistakeThisRound = true;
                    scoreSalah++;
                    document.getElementById('score-s').textContent = scoreSalah;
                    wrongWordsThisSet.push({
                        id: currentQuestion.id,
                        bm: `${currentQuestion.id}: ${currentQuestion.answer}`,
                        chinese: currentQuestion.sentence
                    });
                    syncLiveProgress();
                }

                banner.innerHTML = `❌ 不对哦，<strong>“${escapeHtml(choice.text)}”</strong> 不适合填入这个句子，请再选一次！`;
                banner.style.color = "#c62828";
            }
        }

        function nextQuestion() {
            currentIndex++;
            loadNextQuestion();
        }

        function showCelebration() {
            gameActive = false;
            updateUserNameDisplay();
            document.getElementById('celebrate-screen').style.display = 'flex';
            document.getElementById('final-correct').textContent = scoreBetul;
            document.getElementById('final-total').textContent = activePool.length;
            document.getElementById('final-wrong').textContent = scoreSalah;
            const total = scoreBetul + scoreSalah;
            const acc = total > 0 ? Math.round((scoreBetul / total) * 100) : 100;
            document.getElementById('final-accuracy').textContent = acc + "%";
            playSound('sfx-correct');

            const record = buildCurrentRecord();
            sessionHistory.unshift(record);
            saveQuizHistory(record, activeAssignment);
        }

        function buildCurrentRecord() {
            const answered = scoreBetul + scoreSalah;
            const acc = answered > 0 ? Math.round((scoreBetul / answered) * 100) : 100;
            const durationSec = Math.max(1, Math.round((Date.now() - quizStartTime) / 1000));
            const cat = activeAssignment
                ? `📝 ${activeAssignment.quiz_code}`
                : document.getElementById('category-filter').value;
            return {
                student_id: currentStudentId,
                username: currentUsername || currentUserName,
                display_name: currentUserName,
                category: cat,
                score_correct: scoreBetul,
                score_wrong: scoreSalah,
                total_questions: activePool.length,
                accuracy: acc,
                duration_seconds: durationSec,
                wrong_words: wrongWordsThisSet,
                played_at: new Date().toISOString()
            };
        }

        function syncLiveProgress() {
            if (!currentStudentId || activePool.length === 0) return;
            const snapshot = buildCurrentRecord();
            const resumePayload = {
                history_row_id: currentHistoryRowId,
                assignment_id: activeAssignment ? activeAssignment.id : null,
                quiz_code: activeAssignment ? activeAssignment.quiz_code : null,
                category: snapshot.category,
                pool_ids: activePool.map(w => w.id),
                current_index: currentIndex,
                score_correct: snapshot.score_correct,
                score_wrong: snapshot.score_wrong,
                wrong_words: snapshot.wrong_words,
                elapsed_sec: snapshot.duration_seconds,
                updated_at: snapshot.played_at
            };
            liveSyncPromise = liveSyncPromise.then(async () => {
                try {
                    if (!currentHistoryRowId) {
                        const res = await sbFetch("quiz_history_kgnd", {
                            method: "POST",
                            headers: { "Prefer": "return=representation" },
                            body: JSON.stringify(snapshot)
                        });
                        if (Array.isArray(res) && res[0] && res[0].id) {
                            currentHistoryRowId = res[0].id;
                            resumePayload.history_row_id = currentHistoryRowId;
                        }
                    } else {
                        await sbFetch(`quiz_history_kgnd?id=eq.${currentHistoryRowId}`, {
                            method: "PATCH",
                            body: JSON.stringify({
                                score_correct: snapshot.score_correct,
                                score_wrong: snapshot.score_wrong,
                                accuracy: snapshot.accuracy,
                                duration_seconds: snapshot.duration_seconds,
                                wrong_words: snapshot.wrong_words,
                                played_at: snapshot.played_at
                            })
                        });
                    }
                    sbFetch(`students?id=eq.${currentStudentId}`, {
                        method: "PATCH",
                        body: JSON.stringify({ active_quiz_state_kgnd: resumePayload })
                    }).catch(() => {});
                } catch (e) {
                    console.warn("Live sync warning:", e.message);
                }
            });
        }

        async function saveQuizHistory(record, finishedAssign) {
            const statusEl = document.getElementById('cloud-save-status');
            if (!currentStudentId) {
                statusEl.textContent = "💡 游客模式：仅保存在本次页面（登录后可永久记录到云端）";
                statusEl.style.background = "#fff8e1";
                statusEl.style.color = "#f57c00";
                statusEl.style.borderColor = "#ffe082";
                return;
            }
            statusEl.textContent = "☁️ 正在上传成绩到云端...";
            statusEl.style.background = "#e3f2fd";
            statusEl.style.color = "#1565c0";
            statusEl.style.borderColor = "#90caf9";
            try {
                await liveSyncPromise;
                isForcedResume = false;
                pendingResumeState = null;
                setQuizLockUI(false);
                sbFetch(`students?id=eq.${currentStudentId}`, {
                    method: "PATCH",
                    body: JSON.stringify({ active_quiz_state_kgnd: null })
                }).catch(() => {});
                let savedViaPatch = false;
                if (currentHistoryRowId) {
                    try {
                        const updated = await sbFetch(`quiz_history_kgnd?id=eq.${currentHistoryRowId}`, {
                            method: "PATCH",
                            headers: { "Prefer": "return=representation" },
                            body: JSON.stringify({
                                score_correct: record.score_correct,
                                score_wrong: record.score_wrong,
                                total_questions: record.total_questions,
                                accuracy: record.accuracy,
                                duration_seconds: record.duration_seconds,
                                wrong_words: record.wrong_words,
                                played_at: record.played_at
                            })
                        });
                        if (Array.isArray(updated) && updated.length > 0) savedViaPatch = true;
                    } catch (patchErr) {
                        savedViaPatch = false;
                    }
                }
                if (!savedViaPatch) {
                    await sbFetch("quiz_history_kgnd", {
                        method: "POST",
                        body: JSON.stringify(record)
                    });
                }
                if (finishedAssign) {
                    await sbFetch(`quiz_assignments_kgnd?id=eq.${finishedAssign.id}`, {
                        method: "PATCH",
                        body: JSON.stringify({
                            status: "completed",
                            score_correct: record.score_correct,
                            score_wrong: record.score_wrong,
                            accuracy: record.accuracy,
                            completed_at: new Date().toISOString()
                        })
                    });
                    pendingAssignments = pendingAssignments.filter(a => a.id !== finishedAssign.id);
                    if (activeAssignment && activeAssignment.id === finishedAssign.id) {
                        activeAssignment = null;
                    }
                    renderAssignedQuizBanner();
                }
                statusEl.textContent = finishedAssign
                    ? `✅ 「${finishedAssign.quiz_code}」已提交并记录至云端！`
                    : "✅ 成绩与错题已成功保存至云端学习记录！";
                statusEl.style.background = "#e8f5e9";
                statusEl.style.color = "#2e7d32";
                statusEl.style.borderColor = "#a5d6a7";
            } catch (err) {
                statusEl.textContent = "⚠️ 云端保存失败：" + err.message;
                statusEl.style.background = "#ffebee";
                statusEl.style.color = "#c62828";
                statusEl.style.borderColor = "#ef9a9a";
            }
        }

        function openHistoryModal() {
            const label = currentClassName ? `${currentUserName} (${currentClassName})` : (currentUserName || "游客");
            document.getElementById('hist-player-title').textContent = label;
            document.getElementById('hist-account-mode').textContent = currentStudentId
                ? `☁️ 已登录账号：${currentUsername}`
                : "🚀 当前为游客模式（仅显示本次记录）";
            document.getElementById('history-modal-overlay').style.display = 'flex';
            loadStudentHistory();
        }

        function closeHistoryModal() {
            document.getElementById('history-modal-overlay').style.display = 'none';
        }

        async function loadStudentHistory() {
            const listEl = document.getElementById('history-list');
            listEl.innerHTML = `<p style="text-align:center; color:#777;">⏳ 正在读取学习记录...</p>`;
            let rows = [];
            if (currentStudentId) {
                try {
                    rows = await sbFetch(`quiz_history_kgnd?student_id=eq.${encodeURIComponent(currentStudentId)}&order=played_at.desc&limit=30`);
                } catch (err) {
                    listEl.innerHTML = `<p style="text-align:center; color:#c62828;">⚠️ 读取记录失败：${err.message}</p>`;
                    return;
                }
            } else {
                rows = sessionHistory;
            }

            document.getElementById('hist-total-rounds').textContent = rows.length;
            const totalCorrect = rows.reduce((sum, r) => sum + (r.score_correct || 0), 0);
            const avgAcc = rows.length ? Math.round(rows.reduce((sum, r) => sum + (r.accuracy || 0), 0) / rows.length) : 0;
            document.getElementById('hist-total-correct').textContent = totalCorrect;
            document.getElementById('hist-avg-acc').textContent = avgAcc + "%";

            if (rows.length === 0) {
                listEl.innerHTML = `<p style="text-align:center; color:#777; padding:24px;">暂无练习记录，完成一组练习后会自动出现在这里！</p>`;
                return;
            }

            listEl.innerHTML = rows.map(r => {
                const dt = r.played_at ? new Date(r.played_at).toLocaleString('zh-MY', { hour12: false }) : '';
                const mins = Math.floor((r.duration_seconds || 0) / 60);
                const secs = (r.duration_seconds || 0) % 60;
                const dur = mins > 0 ? `${mins}分${secs}秒` : `${secs}秒`;
                const wrongs = Array.isArray(r.wrong_words) ? r.wrong_words : [];
                const wrongHtml = wrongs.length > 0
                    ? `<div style="margin-top:4px;"><span style="font-size:0.82em; color:#666;">错题：</span>` +
                      wrongs.map(w => `<span class="wrong-word-pill">${escapeHtml(w.bm || w.id)}</span>`).join('') + `</div>`
                    : `<div style="font-size:0.82em; color:#2e7d32; font-weight:bold;">🌟 全对无错题！</div>`;
                return `
                    <div class="history-item">
                        <div class="history-item-top">
                            <span>📚 ${r.category === 'ALL' ? '全部题目' : escapeHtml(r.category)}</span>
                            <span style="color:#1565c0;">✅ ${r.score_correct}/${r.total_questions} · 🎯 ${r.accuracy}% · ⏱️ ${dur}</span>
                        </div>
                        <div style="font-size:0.8em; color:#78909c;">🕒 ${dt}</div>
                        ${wrongHtml}
                    </div>
                `;
            }).join('');
        }

        window.onload = () => {
            initGameData();
        };
    </script>
</body>
</html>
'''

with open(r'X:\scripts_custom\iflow-edugames-kata-ganti-nama-diri\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated X:\\scripts_custom\\iflow-edugames-kata-ganti-nama-diri\\index.html successfully!")
