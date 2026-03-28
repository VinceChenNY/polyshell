# -*- coding: utf-8 -*-
import importlib

LANG="en"

TEXT={
"en":{"prompt":">> ","unknown":"I’m not sure 🤔"},
"zh":{"prompt":">> ","unknown":"我不太确定 🤔"},
"es":{"prompt":">> ","unknown":"No estoy seguro 🤔"},
"hi":{"prompt":">> ","unknown":"मैं निश्चित नहीं हूँ 🤔"},
"ar":{"prompt":">> ","unknown":"لست متأكدًا 🤔"}
}

def t(k):
    return TEXT.get(LANG,TEXT["en"]).get(k,k)

def select_lang():
    global LANG
    print("1 English\n2 中文\n3 Español\n4 हिन्दी\n5 العربية")
    c=input("Select: ").strip()
    LANG={"2":"zh","3":"es","4":"hi","5":"ar"}.get(c,"en")

def load(name):
    try:
        m=importlib.import_module("actions."+name)
        return m.run
    except:
        return None

select_lang()
print("🚀 PolyShell")

while True:
    q=input(t("prompt")).strip()

    if q in ["exit","quit","退出"]:
        break

    if q.lower() in ["deploy","部署"]:
        f=load("deploy")
        if f: f([],LANG)
        continue

    if q.lower().startswith("open") or "打开" in q:
        f=load("open")
        if f: f([],LANG)
        continue

    if q.lower().startswith("clean") or "清理" in q:
        f=load("clean")
        if f: f([],LANG)
        continue

    if q.lower().startswith("fix") or "修复" in q:
        f=load("fix")
        if f: f([],LANG)
        continue

    print(t("unknown"))
