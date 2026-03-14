# PolyShell Language System

PolyShell provides a multilingual interface for computer systems.

The goal of the PolyShell language system is to allow users to interact with their computer using their native language, while keeping the internal command system simple and stable.

PolyShell achieves this through a layered architecture.

---

# Architecture Overview

The PolyShell language system is built around a stable internal command language called **PolyShell DSL**.

Human languages are mapped to this DSL through language packs.

System outputs are also translated back to the user’s preferred language.

The full architecture:

User Natural Language  
↓  
Language Pack (Input Mapping)  
↓  
PolyShell DSL  
↓  
Workflow Engine  
↓  
System Executor  
↓  
Operating System  
↓  
System Output  
↓  
PolyShell Output Translator  
↓  
User Language

This architecture allows PolyShell to support multiple languages without changing the core command system.

---

# PolyShell DSL

PolyShell DSL is a minimal domain-specific language used internally by the system.

It defines a set of stable system actions.

Example DSL commands:

install python  
create folder project  
open browser  
show cpu  

These commands represent system-level operations.

DSL actions are designed to remain stable over time.

Human language expressions are translated into these commands.

---

# Language Packs

PolyShell uses language packs to map natural language inputs into DSL commands.

Each language pack contains mappings from user expressions to PolyShell actions.

Example:

Chinese language pack

安装 → install  
创建 → create  
打开 → open  
删除 → delete  

Spanish language pack

instalar → install  
crear → create  
abrir → open  
eliminar → delete  

Hindi language pack

इंस्टॉल → install  
बनाओ → create  
खोलो → open  

Language packs allow PolyShell to support global users without changing the DSL.

---

# Output Translation

PolyShell also translates system outputs into the user's language.

Operating systems typically return messages in English.

PolyShell intercepts these messages and translates them before displaying them to the user.

Example:

System output:

Python installed successfully

PolyShell output (Chinese):

Python 已成功安装

PolyShell output (Spanish):

Python instalado correctamente

This allows users to fully interact with the system in their own language.

---

# Workflow Explanation Layer

Before executing system actions, PolyShell may analyze the requested operation and display the planned workflow.

Example:

User input:

安装 openclaw

PolyShell analysis:

You want to install: openclaw

Required steps:

1 Install Python  
2 Install dependencies  
3 Download openclaw package  
4 Configure environment  
5 Start service  

Continue installation? (yes / no)

This explanation layer helps users understand what the system will do before execution.

---

# Design Principles

The PolyShell language system follows several key principles.

Stable DSL  
The PolyShell DSL remains stable even as language packs evolve.

Language independence  
Human languages are mapped to DSL commands through language packs.

Transparency  
PolyShell explains planned workflows before executing them.

Extensibility  
New languages can be added by creating additional language pack files.

---

# Future Development

Future versions of PolyShell may include:

Automatic language detection  
Expanded language packs  
Improved workflow planning  
Context-aware command interpretation  

These improvements will enhance the natural language experience while keeping the DSL stable.
