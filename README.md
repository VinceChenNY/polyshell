# PolyShell 🚀

PolyShell is a natural language CLI that allows users to control computers using human language.

Instead of learning complex commands, users can simply describe what they want.

---

## ✨ Features

* 🌍 Multi-language support (Chinese / English / more)
* ⚡ Local execution (no token cost for common commands)
* 🤖 AI fallback (only when needed)
* 🧠 Smart path management (`~/projects`)
* 🔒 Safe mode (confirmation before AI usage)
* 🖥️ Semi-real system interaction (files, disk, browser)

---

## 🧠 How it works

Human Language
→ AI / Local Parser
→ PolyShell DSL
→ Command Execution

---

## 🚀 Demo

```bash
open google
创建文件 test.txt
scan disk
```

---

## 🔑 Setup

Run:

```bash
python3 polyshell.py
```

You will be guided to get your OpenAI API key.

---

## 📌 Example

```bash
>> 帮我创建一个python文件 demo.py
>>> mkdir -p ~/projects/python && touch ~/projects/python/demo.py
```

---

## 🛠️ Tech

* Python
* OpenAI API
* Linux CLI

---

## 📈 Roadmap

* [ ] Better language understanding
* [ ] Smarter file organization
* [ ] GUI version
* [ ] Plugin system

---

## 💡 Vision

PolyShell reverses computing:

Human language → Machine execution

---

## 📄 License

MIT
