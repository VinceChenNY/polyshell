# -*- coding: utf-8 -*-
import os,json

CONF=os.path.expanduser("~/.polyshell_keys.json")

TOOLS=[
("Ollama","本地大模型","Local AI","local"),
("LM Studio","本地AI界面","Local GUI","local"),
("Qwen","阿里模型","Model","local"),
("DeepSeek","推理模型","Model","local"),
("n8n","自动化工具","Automation","local"),
("NodeRED","流程工具","Flow","local"),
("Playwright","浏览器自动化","Browser","local"),
("Selenium","网页自动化","Web","local"),
("Jupyter","数据分析","Notebook","local"),
("Metabase","数据看板","Dashboard","local"),
("OpenAI","GPT接口","API","api"),
("DeepSeekAPI","推理接口","API","api"),
("QwenAPI","阿里接口","API","api"),
("GLM","智谱接口","API","api"),
("Dify","AI平台","Platform","api"),
("LangChain","开发框架","Framework","api"),
("NewsAPI","新闻接口","Data","api"),
("Twitter","社交接口","Social","api"),
("Reddit","社区接口","Community","api"),
("Polymarket","预测市场","Market","api")
]

def load():
    if os.path.exists(CONF):
        try:return json.load(open(CONF))
        except:return {}
    return {}

def save(d):
    try:json.dump(d,open(CONF,"w"))
    except:pass

def run(words=None,lang="en"):
    k=load()
    while True:
        print("\n🚀 Deploy\n")

        for i,t in enumerate(TOOLS,1):
            name,zh,en,typ=t
            desc=zh if lang=="zh" else en
            print(f"{i}. {name}（{desc}）")

        print("0 back")

        c=input("Select: ").strip()
        if c=="0":break

        try:c=int(c)
        except:continue

        if 1<=c<=20:
            name,zh,en,typ=TOOLS[c-1]

            if typ=="local":
                print("🟢 OK")
            else:
                if input("⚠️ cost? y/n: ")!="y":continue
                key=input("API key: ").strip()
                if not key:continue
                k[name]=key
                save(k)
                print("saved")
