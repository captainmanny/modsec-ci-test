import sys

CONFIG_FILE = "modsecurity.conf"

def main():
    try:
        with open(CONFIG_FILE, "r") as f:
            content = f.read()
        if "SecRuleEngine On" in content:
            print("✅ SecRuleEngine is enabled.")
            sys.exit(0)
        else:
            print("❌ SecRuleEngine directive missing or misconfigured.")
            sys.exit(1)
    except FileNotFoundError:
        print(f"❌ Config file {CONFIG_FILE} not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()

