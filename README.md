cat > README.md << 'EOF'
# PolyShell 🚀

## What is this?

PolyShell is a natural language command system.

You can control your computer without programming.

Just type what you want.

Example:
- open google
- create file
- deploy project

---

## Goal

Make computers usable for everyone.

No coding needed.

---

## Features

- Natural language input
- Multi-language support
- Plugin system (extend easily)
- Safe execution (user confirmation)
- Beginner-friendly guidance

---

## Architecture

User Input
→ Intent Detection
→ Action Plugin
→ Execute

---

## How to run

cd polyshell  
python3 main.py

---

## Add new feature

Create a new file in:

polyshell/actions/

Example:

```python
def run(words, lang):
    print("Hello world")
