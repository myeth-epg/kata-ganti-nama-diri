# 华小国语人称代词连连乐（SJK(C) Kata Ganti Nama Diri EduGame）项目开发记录

**最后更新日期：** 2026年11月22日  
**项目目录：** `X:\scripts_custom\iflow-edugames-kata-ganti-nama-diri`  
**线上游戏地址（Netlify）：** `https://kata-ganti-nama-diri.netlify.app/`  
**线上总入口主页（Master Portal）：** `https://sjkc-edugames.netlify.app/`（本地目录：`X:\scripts_custom\iflow-edugames-portal`）  
**GitHub 仓库：** `myeth-epg/kata-ganti-nama-diri`  
**本地 / NAS 服务端口：** `8084`

---

## 1. 核心架构与文件说明

| 文件 / 目录 | 用途说明 |
| :--- | :--- |
| `index.html` | 学生端主游戏网页（句子填充 4 选 1、内嵌备用题库、Supabase 登录/断点续答、历史记录弹窗） |
| `build_html.py` | 自动读取 `kata_ganti_nama_data.json` 并生成最新 `index.html` 的构建脚本 |
| `editjson.html` | 题库可视化编辑器（深灰护眼主题，卡片式编辑 ID、组别、句子、正确答案、3 个干扰项、翻译与语法解析） |
| `build_editjson.py` | 自动读取 `kata_ganti_nama_data.json` 并生成最新 `editjson.html` 的构建脚本 |
| `admin.html` | 老师 / 管理员监控后台（密码解锁、学生管理、测验派发/补派/归档、高频错题排行、CSV 导出） |
| `kata_ganti_nama_data.json` | 核心国语人称代词填充题库（当前共 **240 题**，Groups A–E） |
| `supabase_kgnd_tables.sql` | Supabase 建表与 RLS 权限 SQL 脚本 |
| `server.js` / `server.py` | 零依赖本地与 NAS 后端服务（端口 `8084`，支持 `/api/data` 与 `/api/save` 在线保存并重建网页） |
| `Run_Game_Server.bat` / `start_server.sh` | Windows / Ugreen NAS 一键启动脚本 |
| `bgm.mp3`, `correct.mp3`, `wrong.mp3`, `timeout.mp3` | 背景音乐与答题音效（本游戏已跳过单字 TTS 语音，保留音效与 BGM） |

---

## 2. 马来西亚华小（SJK(C) KSSR）题库进度：共 240 题

每道题目均为**句子填充题（4 选 1）**，包含：
- `id`（题号，如 `A001`–`E050`）
- `group` / `category`（所属组别单元）
- `sentence`（国语句子，含 `( ________ )` 空格）
- `answer`（唯一正确答案，匹配空格大小写）
- `distractors`（3 个干扰选项，与空格大小写一致）
- `translation_zh`（华语句意翻译）
- `explanation_zh`（华语语法解析）

### 题目分布（总计 240 题）
| 组别单元 | 题号范围 | 题数 | 重点内容 |
| :--- | :---: | :---: | :--- |
| **Group A: Kata Ganti Nama Diri** | `A001`–`A040` | 40 | 基础人称代词综合练习（用户提供原题） |
| **Group B: Kata Ganti Nama Diri** | `B001`–`B050` | 50 | 第一、二、三人称与皇室/常见校园情境 |
| **Group C: Sekolah & Keluarga (校园与家庭)** | `C001`–`C050` | 50 | 马来西亚华小校园生活、师长同学与家庭日常 |
| **Group D: Masyarakat & Nilai (社区与道德)** | `D001`–`D050` | 50 | 社区互助、环保运动、道德价值观与社会人物 |
| **Group E: Istana & Lanjutan (皇室与进阶)** | `E001`–`E050` | 50 | 皇室用语（`beta`, `patik`, `tuanku`, `baginda`）、历史故事与 UASA 进阶 |
| **总计** | — | **240** | 全部通过唯一性及同义词互斥校验（`Errors: []`） |

### 选项防混淆核心规则（已写入题库与前端生成器）
- **第二人称同义词互斥：** `awak`、`anda`、`kamu`、`engkau` **绝对不同时出现**在同一题的 4 个选项中。
- **第一人称同义词互斥：** `saya`、`aku` **绝对不同时出现**在同一题的 4 个选项中。

---

## 3. Supabase 云端架构（共享学生账号，独立题库数据）

与 **Perkataan BM** 及 **English Vocabulary** 共用同一个 Supabase 项目（`https://kuybhocpdsttmmjkihcv.supabase.co`）：
- **共享表：** `public.students`（三科游戏共用同一套学生账号、班级与 4 位密码 PIN）
- **独立表与字段（由 `supabase_kgnd_tables.sql` 创建）：**
  1. `public.quiz_history_kgnd` — 每次练习/测验成绩、用时与错题记录
  2. `public.quizzes_kgnd` — 老师创建的测验（含 `is_archived boolean default false` 支持归档/取消归档）
  3. `public.quiz_assignments_kgnd` — 派发给学生的测验任务与重做次数（`attempt_no`）
  4. `public.students.active_quiz_state_kgnd` — 断线/中途退出强制续答状态

---

## 4. 老师监控后台（`admin.html`）已实现功能

- **📋 最新答题记录：** 按班级、单元、学生姓名或错题搜索筛选，支持一键导出 Excel (CSV)。
- **👩‍🎓 学生账号管理：** 共享全科 `students` 表，支持 `➕ Add New`、`📋 批量导入`、`🔑 改密码`、`⏸️ 停用 / ▶️ 启用`。
- **📝 测验派发管理：**
  - 从 Groups A–E 多选单元创建测验（如 `Quiz 001`），派发给全体启用学生、指定班级或手动勾选学生。
  - **➕ 补派：** 针对后来新加入的学生单独补派已有测验。
  - **➕ 一键补派新学生：** 一键将测验补派给所有尚未收到该测验的启用中学生。
  - **🔁 重派 (Reassign)：** 针对弱生或需要重做的学生增加作答次数重新派发。
  - **📦 归档 / ♻️ 取消归档 (Archive / Unarchive)：** 隐藏不需要再显示在学生端的旧测验或误建测验，完整保留历史数据，随时可勾选「📦 显示已归档测验」恢复。
- **❌ 高频错题排行榜：** 自动统计全班最常答错的题目与次数。

---

## 5. 华小趣味学习乐园总入口（Master Portal）

- **网址：** `https://sjkc-edugames.netlify.app/`
- **本地目录：** `X:\scripts_custom\iflow-edugames-portal\index.html`
- **整合三大游戏：**
  1. 📘 华小国语词汇连连乐 (`https://perkataan-bm.netlify.app/`)
  2. 📗 华小英文词汇连连乐 (`https://englishvocabulary88.netlify.app/`)
  3. ✏️ 华小国语人称代词 (`https://kata-ganti-nama-diri.netlify.app/`)
- 底部附带三个游戏对应的老师监控后台快捷入口。
