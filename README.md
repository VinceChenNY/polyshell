# PolyShell 🚀

PolyShell is a natural language command system that lets you control your computer using plain language — no coding required.

It is designed for beginners and anyone who wants a simpler way to interact with computers.

---

## ✨ Features
- Natural language input (English + Chinese)
- Plugin-based architecture (easy to extend)
- AI fallback with user confirmation
- Safe execution (no automatic API usage)
- Beginner-friendly design

---

## 🧠 How it works
User Input → Intent Detection → Action Plugin → Execute

---

## 🚀 Quick Start
cd polyshell
python3 polyshell.py

---

## 🧪 Examples
open google  
create file  
帮我创建一个文件  

---

## 🔌 Plugins
Add new features by creating files in:
actions/

Each plugin should define:
def run(words, lang):
    pass

---

## 🔐 AI Usage
PolyShell will ask before using AI, warn about possible costs, and require users to input their own API key.

Your API key is never stored or shared.

---

## 🎯 Vision
Make computers usable for everyone — just by speaking naturally.

---

## ⚠️ Note
This is an early MVP version. More intelligent parsing and features will be added in the future.

EOF
