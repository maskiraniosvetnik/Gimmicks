#!/usr/bin/env python3
# requires: pip install readchar
import time
import sys
import random
import threading
import json
import os
import readchar

random.seed()

ROASTERS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "roasters")

def list_roasters():
    if not os.path.isdir(ROASTERS_DIR):
        print("ERROR: 'roasters' folder not found next to the script.")
        sys.exit(1)
    files = sorted([f for f in os.listdir(ROASTERS_DIR) if f.endswith(".json")])
    if not files:
        print(f"ERROR: No JSON files found in '{ROASTERS_DIR}' folder.")
        sys.exit(1)
    return files

def pick_roaster(files):
    print("\n  Who do you want to be roasted by?\n")
    for i, f in enumerate(files, 1):
        name = os.path.splitext(f)[0].replace("_", " ").title()
        print(f"  [{i}] {name}")
    print()
    while True:
        try:
            choice = int(input("  Enter number: ").strip())
            if 1 <= choice <= len(files):
                return files[choice - 1]
            print(f"  Pick a number between 1 and {len(files)}, you donkey.")
        except ValueError:
            print(f"  That's not a number. Try again.")

def load_roaster(filename):
    path = os.path.join(ROASTERS_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            R = json.load(f)
        return R
    except Exception as e:
        print(f"ERROR: Could not load {filename}: {e}")
        sys.exit(1)

state = {"toggle": False, "quit": False}

def format_time(seconds):
    m = seconds // 60
    s = seconds % 60
    return f"{m:02d}:{s:02d}"

def divider():
    print("=" * 62)

def get_break_roast(R, minutes):
    lst = R["break_roasts_by_minute"]
    idx = min(minutes - 1, len(lst) - 1)
    return lst[idx]

def keypress_listener():
    while not state["quit"]:
        try:
            key = readchar.readkey()
            if key in (readchar.key.CTRL_C, readchar.key.CTRL_D, 'q', 'Q'):
                state["quit"] = True
            else:
                state["toggle"] = True
        except Exception:
            break

def main():
    divider()
    print("            PRODUCTIVITY ENFORCER")
    divider()
    print("  Work counts DOWN. Breaks count UP.")
    print("  ANY KEY during work  -> break starts.")
    print("  ANY KEY during break -> back to work.")
    print("  Q or Ctrl+C to quit.")
    divider()

    files = list_roasters()
    chosen = pick_roaster(files)
    R = load_roaster(chosen)
    roaster_name = os.path.splitext(chosen)[0].replace("_", " ").title()

    print(f"\n  Roaster loaded: {roaster_name}")
    divider()

    while True:
        try:
            raw = input("\n  How long is your work session? (minutes): ").strip()
            total_seconds = int(raw) * 60
            if total_seconds <= 0:
                raise ValueError
            break
        except ValueError:
            print("  Enter a valid number of minutes, you donkey.")

    listener = threading.Thread(target=keypress_listener, daemon=True)
    listener.start()

    print(f"\n  Session: {format_time(total_seconds)}")
    print(f"  Press any key to toggle break/work. Starting in 3 seconds...\n")
    time.sleep(3)

    remaining = total_seconds
    total_break_seconds = 0
    break_seconds = 0
    break_roasted_minutes = 0
    mode = "work"
    acc = 0

    print(f"\r  WORK | {format_time(remaining)} remaining...  ", end="", flush=True)

    while remaining > 0 and not state["quit"]:
        time.sleep(0.1)
        acc += 1

        if state["toggle"]:
            state["toggle"] = False
            acc = 0

            if mode == "work":
                mode = "break"
                break_seconds = 0
                break_roasted_minutes = 0
                print(f"\n\n{'=' * 62}")
                print(f"  {random.choice(R['interrupt_roasts'])}")
                print(f"  Break counter running. Press any key to get back to work.")
                print(f"{'=' * 62}\n")
                print(f"\r  BREAK | {format_time(break_seconds)} wasted...  ", end="", flush=True)

            else:
                mode = "work"
                total_break_seconds += break_seconds
                print(f"\n\n{'=' * 62}")
                print(f"  {random.choice(R['resume_roasts'])}")
                print(f"  That break cost you {format_time(break_seconds)}. Remember that.")
                print(f"{'=' * 62}\n")
                print(f"\r  WORK | {format_time(remaining)} remaining...  ", end="", flush=True)

        if acc >= 10:
            acc = 0

            if mode == "work":
                remaining -= 1
                if remaining > 0:
                    print(f"\r  WORK | {format_time(remaining)} remaining...  ", end="", flush=True)

            elif mode == "break":
                break_seconds += 1
                print(f"\r  BREAK | {format_time(break_seconds)} wasted...  ", end="", flush=True)

                minutes_elapsed = break_seconds // 60
                if minutes_elapsed > break_roasted_minutes:
                    break_roasted_minutes = minutes_elapsed
                    print(f"\n\n  {roaster_name.upper()}: {get_break_roast(R, break_roasted_minutes)}\n")
                    print(f"\r  BREAK | {format_time(break_seconds)} wasted...  ", end="", flush=True)

    state["quit"] = True

    if remaining <= 0:
        print(f"\n\n{'=' * 62}")
        print(f"  SESSION COMPLETE.")
        print(f"  {random.choice(R['finish_lines'])}")
        if total_break_seconds > 0:
            print(f"  Total break time: {format_time(total_break_seconds)}. Pathetic.")
        print(f"{'=' * 62}\n")
    else:
        print(f"\n\n{'=' * 62}")
        print(f"  Running away? {format_time(remaining)} still on the clock.")
        print(f"  {R['quit_line']}")
        print(f"{'=' * 62}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCoward. Absolute coward. Goodbye.")
        sys.exit(0)