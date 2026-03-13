import os

print("PolyShell Demo v0.1")
print("Type 'exit' to quit")
print("")

# ------------------------
# PolyShell DSL
# ------------------------

# core actions
actions = {
    "install": "install",
    "安装": "install",

    "create": "create",
    "创建": "create",

    "open": "open",
    "打开": "open",

    "delete": "delete",
    "删除": "delete",

    "show": "show",
    "显示": "show",

    "update": "update",
    "更新": "update",

    "search": "search",
    "搜索": "search",

    "run": "run",
    "运行": "run",

    "stop": "stop",
    "停止": "stop",

    "help": "help",
    "帮助": "help"
}

# core objects
objects = {
    "python": "python",
    "node": "node",

    "folder": "folder",
    "文件夹": "folder",

    "file": "file",
    "文件": "file",

    "browser": "browser",
    "浏览器": "browser",

    "project": "project",
    "项目": "project",

    "cpu": "cpu",
    "memory": "memory",
    "disk": "disk",
    "network": "network"
}

# ------------------------
# Command Executor
# ------------------------

def execute(action, obj, param):

    if action == "install" and obj == "python":
        print("→ Executing: install python")

    elif action == "create" and obj == "folder":
        if param:
            os.makedirs(param, exist_ok=True)
            print("→ Folder created:", param)
        else:
            print("→ Please specify folder name")

    elif action == "open" and obj == "browser":
        print("→ Opening browser")

    elif action == "delete" and obj == "file":
        print("→ Deleting file:", param)

    elif action == "show":
        print("→ Showing", obj)

    elif action == "help":
        print("")
        print("Available commands:")
        print("install python")
        print("create folder NAME")
        print("open browser")
        print("show cpu")
        print("delete file NAME")
        print("")

    else:
        print("→ Command recognized but not implemented yet")


# ------------------------
# Main Loop
# ------------------------

while True:

    command = input("PolyShell > ")

    if command == "exit":
        print("Exiting PolyShell")
        break

    words = command.split()

    if len(words) < 2:
        print("Invalid command")
        continue

    action_word = words[0]
    object_word = words[1]

    param = None
    if len(words) > 2:
        param = words[2]

    action = actions.get(action_word)
    obj = objects.get(object_word)

    if not action:
        print("Unknown action")
        continue

    if not obj:
        print("Unknown object")
        continue

    print("DSL →", action, obj, param)

    execute(action, obj, param)
