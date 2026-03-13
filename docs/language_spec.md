# PolyShell Language Specification v0.1

PolyShell defines a simple domain-specific language (DSL) for interacting with computer systems.

The goal of PolyShell DSL is to provide a stable internal command language while allowing users to interact with computers using natural language through AI interpretation and language packs.

Natural language inputs are translated into PolyShell DSL before execution.

---

# Command Structure

PolyShell commands follow a simple structure:

action object parameter

Examples:

install python  
create folder project  
open browser  
delete file example.txt  
show cpu  

---

# Core Actions (v0.1)

PolyShell v0.1 defines a minimal set of core actions.

install  
create  
open  
delete  
show  
update  
search  
run  
stop  
help  

These actions represent the most common system operations.

---

# Core Objects (v0.1)

PolyShell v0.1 defines a basic set of system objects.

python  
node  
folder  
file  
browser  
project  
cpu  
memory  
disk  
network  

---

# Example Commands

install python  
create folder test  
open browser  
delete file example.txt  
show cpu  

---

# Language Pack Mapping

Users do not need to type PolyShell DSL directly.

Language packs map natural language into PolyShell commands.

Example mappings:

Chinese

安装 python → install python  
创建 文件夹 test → create folder test  
打开 浏览器 → open browser  

Spanish

instalar python → install python  
crear carpeta test → create folder test  

Hindi

पायथन इंस्टॉल → install python  

---

# Design Principles

PolyShell DSL is stable and minimal.

Natural language, language packs, and AI interpretation translate user input into PolyShell DSL commands.

This architecture allows PolyShell to support many human languages while keeping the internal command system simple and stable.
