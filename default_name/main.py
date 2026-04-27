import argparse
from config import USER_SCOPES
from scanner import scan
from renamer import rename_files
from logger import write_log

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("\n🎭 GIMMICK RENAMER STARTED\n")

    files = scan(USER_SCOPES)

    print(f"📁 Found {len(files)} target files")

    if not files:
        print("Nothing to do.")
        return

    level, log = rename_files(files, dry_run=args.dry_run)

    write_log(level, log)

    print(f"\n📊 Final Chaos Level: {level}")

if __name__ == "__main__":
    main()