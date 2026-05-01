#!/usr/bin/env python3
import os
import sys
import json
import random
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FORTUNE_DIR = os.path.join(BASE_DIR, "4tunes")

print ("Load your cookie and crack the fortune awaiting!");

def slow_print(text, delay=0.03):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

def crack():
    print("\n  *crack*\n")
    time.sleep(0.5)

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"ERROR loading {path}: {e}")
        sys.exit(1)

def discover_files():
    if not os.path.exists(FORTUNE_DIR):
        print("ERROR: /4tunes directory not found.")
        sys.exit(1)

    files = [
        f for f in os.listdir(FORTUNE_DIR)
        if os.path.isfile(os.path.join(FORTUNE_DIR, f)) and f.lower().endswith(".json")
    ]

    if not files:
        print("ERROR: no fortune files in /4tunes.")
        sys.exit(1)

    return sorted(files)

def build_menu(files):
    print("=" * 50)
    for i, f in enumerate(files, 1):
        name = f.replace(".json", "")
        print(f"  [{i}] {name}")
    print("=" * 50)

def choose_file(files):
    while True:
        choice = input("\n  choose your poison: ").strip()

        if not choice.isdigit():
            print("  numbers only. don't get creative.")
            continue

        idx = int(choice) - 1

        if 0 <= idx < len(files):
            return files[idx]

        print("  invalid choice.")

def run_machine(data):
    fortunes = data.get("fortunes", [])
    quit_msgs = data.get("quit_messages", ["goodbye."])
    interrupt_msg = data.get("interrupt_message", "you escaped.")
    name = data.get("name", "unknown set")

    if not fortunes:
        print("ERROR: no fortunes inside file.")
        sys.exit(1)

    print(f"\n  {name} loaded.")
    print("  press ENTER to break a cookie.")
    print("  type Q and press ENTER to leave.\n")

    pool = fortunes.copy()
    seen = []

    while True:
        user = input().strip().lower()

        if user == "q":
            print(f"\n  {random.choice(quit_msgs)}\n")
            sys.exit(0)

        if not pool:
            pool = [f for f in fortunes if f not in seen[-5:]] or fortunes.copy()

        fortune = random.choice(pool)
        pool.remove(fortune)
        seen.append(fortune)

        crack()
        slow_print(f'  "{fortune}"')
        print("\n  press ENTER for another. type Q to leave.\n")

def main():
    files = discover_files()
    build_menu(files)

    chosen = choose_file(files)
    path = os.path.join(FORTUNE_DIR, chosen)

    data = load_json(path)

    try:
        run_machine(data)
    except KeyboardInterrupt:
        msg = data.get("interrupt_message", "interrupted.")
        print(f"\n\n  {msg}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()