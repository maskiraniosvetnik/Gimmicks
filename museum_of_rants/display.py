import sys
import time

from archive import load_archive


def slow_print(text, d=0.015):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(d * 6 if c in ".!?" else d)
    print()


def display(e):
    border = "═" * 60
    print()
    slow_print("  " + border)

    if e["anomaly"]:
        slow_print(f"      [ANOMALY DETECTED: {e['anomaly']}]", 0.02)

    slow_print(f"      {e['name'].upper()}", 0.03)
    slow_print(f"      {e['subtitle']}")
    slow_print(f"      {e['wing']}")
    slow_print("  " + border + "\n")

    slow_print("  DESCRIPTION")
    slow_print("  " + e["desc"] + "\n")

    slow_print("  SIGNIFICANCE")
    slow_print("  " + e["sig"] + "\n")

    slow_print("  CURATOR NOTE")
    slow_print("  " + e["note"] + "\n")

    slow_print("  " + border)
    slow_print("  " + e["foot"])
    slow_print("  " + border + "\n")


def gallery():
    archive = load_archive()
    if not archive:
        slow_print("\n  The archive is currently empty.\n")
        return

    i = 0
    while True:
        display(archive[i])
        cmd = input("  (n=next, p=prev, q=exit) › ").strip().lower()

        if cmd == "n":
            i = (i + 1) % len(archive)
        elif cmd == "p":
            i = (i - 1) % len(archive)
        elif cmd == "q":
            break
