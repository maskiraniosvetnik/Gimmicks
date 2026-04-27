import time

from logic import build_exhibit
from display import slow_print, display, gallery
from archive import add_to_archive


def main():
    slow_print("\n  ╔══════════════════════════════════════╗", 0.01)
    slow_print("  ║   MUSEUM OF HUMAN SUFFERING          ║", 0.01)
    slow_print("  ║   Artifact Intake Terminal  v1.0     ║", 0.01)
    slow_print("  ╚══════════════════════════════════════╝\n", 0.01)

    slow_print("  Please describe your grievance below.")
    slow_print("  It will be treated with the utmost academic respect.\n")

    while True:
        print("  › ", end="")
        user_input = input().strip()

        if user_input.lower() in ["exit", "quit", "q"]:
            slow_print("\n  Archive closed. Thank you for your contribution.\n")
            break

        if user_input.lower() == "gallery":
            gallery()
            continue

        exhibit = build_exhibit(user_input)

        slow_print("\n  Processing artifact...", 0.04)
        time.sleep(0.5)
        slow_print("  Consulting the curatorial committee...", 0.04)
        time.sleep(0.5)
        slow_print("  Assigning wing placement...\n", 0.04)

        display(exhibit)

        save = input("  Save artifact? (y/n) › ").strip().lower()
        if save == "y":
            add_to_archive(exhibit)
            slow_print("  Artifact archived.\n")


if __name__ == "__main__":
    main()
