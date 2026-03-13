import tkinter as tk

# -------- DSL actions --------

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

    "help": "help",
    "帮助": "help"
}

# -------- DSL objects --------

objects = {
    "python": "python",
    "folder": "folder",
    "文件夹": "folder",
    "browser": "browser",
    "浏览器": "browser",
    "cpu": "cpu"
}

# -------- command logic --------

def execute_command():

    command = entry.get()
    words = command.split()

    if len(words) < 2:
        output.insert(tk.END, "Invalid command\n")
        return

    action_word = words[0]
    object_word = words[1]

    action = actions.get(action_word)
    obj = objects.get(object_word)

    if not action:
        output.insert(tk.END, "Unknown action\n")
        return

    if not obj:
        output.insert(tk.END, "Unknown object\n")
        return

    output.insert(tk.END, f"DSL → {action} {obj}\n")

    if action == "install" and obj == "python":
        output.insert(tk.END, "Installing Python...\n")

    elif action == "create" and obj == "folder":
        output.insert(tk.END, "Creating folder...\n")

    elif action == "open" and obj == "browser":
        output.insert(tk.END, "Opening browser...\n")

    elif action == "show" and obj == "cpu":
        output.insert(tk.END, "Showing CPU info...\n")

    elif action == "help":
        output.insert(tk.END, "Commands: install python | create folder | open browser | show cpu\n")

    else:
        output.insert(tk.END, "Command recognized but not implemented\n")

    output.insert(tk.END, "\n")

# -------- GUI window --------

root = tk.Tk()
root.title("PolyShell Demo")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, width=40)
entry.pack()

button = tk.Button(frame, text="Run Command", command=execute_command)
button.pack(pady=5)

output = tk.Text(frame, height=15, width=50)
output.pack()

root.mainloop()
