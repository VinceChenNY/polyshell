"""
PolyShell Enhanced Demo
Natural Language AI Shell Prototype

Features
- Language Pack Loader
- IR Parser
- Plugin System
- Command Registry
- Command Learning
- Autocomplete
- Suggestion Engine
"""

import os
import json

# =============================
# Storage Files
# =============================

LEARNED_COMMANDS_FILE = "learned_commands.json"


# =============================
# Default Language Packs
# =============================

LANGUAGE_PACKS = {

    "english": {
        "install python": ("install", "python"),
        "install node": ("install", "node"),
        "open browser": ("open", "browser"),
        "create folder": ("create", "folder")
    },

    "chinese": {
        "安装 python": ("install", "python"),
        "安装 node": ("install", "node"),
        "打开浏览器": ("open", "browser"),
        "创建文件夹": ("create", "folder")
    },

    "hindi": {
        "पायथन इंस्टॉल": ("install", "python"),
        "नोड इंस्टॉल": ("install", "node"),
        "ब्राउज़र खोलो": ("open", "browser"),
        "फोल्डर बनाओ": ("create", "folder")
    }

}


# =============================
# Command Registry
# =============================

COMMAND_REGISTRY = {

    ("install", "python"): "winget install Python.Python",

    ("install", "node"): "winget install OpenJS.NodeJS",

    ("open", "browser"): "start chrome",

    ("create", "folder"): "mkdir"

}


# =============================
# Plugin System
# =============================

PLUGINS = []

def register_plugin(func):
    PLUGINS.append(func)


def run_plugins(ir):

    for plugin in PLUGINS:
        plugin(ir)


# Example plugin
def security_plugin(ir):

    if ir["intent"] == "install":
        print("Security Check: verifying installer source")


register_plugin(security_plugin)


# =============================
# Load Learned Commands
# =============================

def load_learned_commands():

    if os.path.exists(LEARNED_COMMANDS_FILE):

        with open(LEARNED_COMMANDS_FILE, "r") as f:
            return json.load(f)

    return {}


def save_learned_commands(data):

    with open(LEARNED_COMMANDS_FILE, "w") as f:
        json.dump(data, f, indent=2)


LEARNED_COMMANDS = load_learned_commands()


# =============================
# IR Parser
# =============================

def parse_to_ir(language, text):

    pack = LANGUAGE_PACKS.get(language, {})

    for phrase in pack:

        if text.startswith(phrase):

            intent, target = pack[phrase]

            value = text.replace(phrase, "").strip()

            return {
                "intent": intent,
                "target": target,
                "value": value
            }

    # check learned commands

    if text in LEARNED_COMMANDS:

        return LEARNED_COMMANDS[text]

    return None


# =============================
# Autocomplete
# =============================

def autocomplete(language, text):

    pack = LANGUAGE_PACKS.get(language, {})

    suggestions = []

    for phrase in pack:

        if phrase.startswith(text):

            suggestions.append(phrase)

    return suggestions


# =============================
# Suggestion Engine
# =============================

def suggest_actions(ir):

    if not ir:
        return

    if ir["target"] == "python":

        print("\nSuggestions:")

        print("- install pip")

        print("- create virtual environment")

        print("- create project folder")

    if ir["target"] == "node":

        print("\nSuggestions:")

        print("- install npm packages")

        print("- initialize node project")


# =============================
# Command Executor
# =============================

def execute_command(ir):

    key = (ir["intent"], ir["target"])

    command = COMMAND_REGISTRY.get(key)

    if not command:

        print("Command not supported")

        return

    if ir["intent"] == "create" and ir["value"]:

        command = command + " " + ir["value"]

    print("\nExecuting command:")

    print(command)

    # Disabled for safety
    # os.system(command)


# =============================
# Command Learning
# =============================

def learn_command(text):

    print("Teach PolyShell this command.")

    intent = input("Intent: ")

    target = input("Target: ")

    value = ""

    ir = {
        "intent": intent,
        "target": target,
        "value": value
    }

    LEARNED_COMMANDS[text] = ir

    save_learned_commands(LEARNED_COMMANDS)

    print("Command learned.")


# =============================
# Language Selection
# =============================

def select_language():

    print("Select Language")

    print("1 English")

    print("2 Chinese")

    print("3 Hindi")

    choice = input("> ")

    if choice == "1":
        return "english"

    if choice == "2":
        return "chinese"

    if choice == "3":
        return "hindi"

    return "english"


# =============================
# Main Loop
# =============================

def main():

    print("PolyShell AI Shell Demo")

    language = select_language()

    print("\nPolyShell ready")

    print("Type 'exit' to quit\n")

    while True:

        text = input(">>> ")

        if text == "exit":
            break

        suggestions = autocomplete(language, text)

        if suggestions:

            print("Autocomplete:", suggestions)

        ir = parse_to_ir(language, text)

        if not ir:

            print("Unknown command")

            learn = input("Teach this command? (y/n): ")

            if learn == "y":

                learn_command(text)

            continue

        print("\nIR:", ir)

        run_plugins(ir)

        execute_command(ir)

        suggest_actions(ir)


if __name__ == "__main__":

    main()
