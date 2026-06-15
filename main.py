"""
Corporate Agent Hierarchy — Main Entry Point.

Usage:
    python main.py                     # Interactive mode
    python main.py --demo board_meeting  # Run a named demo
    python main.py --list-demos         # List available demos
"""

import sys
import json
from workflow import DEMO_WORKFLOWS


def print_banner():
    print()
    print("  ============================================================")
    print("    CORPORATE AGENT HIERARCHY v1.0")
    print("    Multi-Agent Corporate Simulation System")
    print("  ============================================================")
    print()


def print_menu():
    print("  Available Commands:")
    print("    1. Run a demo workflow")
    print("    2. List available demos")
    print("    3. Run board meeting demo")
    print("    4. Run security incident demo")
    print("    5. Run product launch demo")
    print("    6. Run quarterly planning demo")
    print("    7. Run custom pivot scenario")
    print("    8. Export company dashboard (JSON)")
    print("    0. Exit")
    print()


def interactive_mode():
    print_banner()
    ceo = None

    while True:
        print_menu()
        choice = input("  Enter choice: ").strip()

        if choice == "0":
            print("\n  Goodbye!\n")
            break
        elif choice == "1":
            print("\n  Available demos:")
            for name in DEMO_WORKFLOWS:
                print(f"    - {name}")
            demo_name = input("  Enter demo name: ").strip()
            if demo_name in DEMO_WORKFLOWS:
                ceo = DEMO_WORKFLOWS[demo_name]()
            else:
                print(f"  Unknown demo: {demo_name}")
        elif choice == "2":
            print("\n  Available demos:")
            for name, func in DEMO_WORKFLOWS.items():
                doc = func.__doc__ or "No description"
                print(f"    - {name}: {doc.strip()}")
        elif choice == "3":
            ceo = DEMO_WORKFLOWS["board_meeting"]()
        elif choice == "4":
            ceo = DEMO_WORKFLOWS["security_incident"]()
        elif choice == "5":
            ceo = DEMO_WORKFLOWS["product_launch"]()
        elif choice == "6":
            ceo = DEMO_WORKFLOWS["quarterly_planning"]()
        elif choice == "7":
            ceo = DEMO_WORKFLOWS["custom"]()
        elif choice == "8":
            if ceo:
                dashboard = ceo.get_company_dashboard()
                output_path = "company_dashboard.json"
                with open(output_path, "w") as f:
                    json.dump(dashboard, f, indent=2)
                print(f"  Dashboard exported to {output_path}")
            else:
                print("  Run a demo first to generate data.")
        else:
            print("  Invalid choice. Try again.")


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--list-demos":
            print("Available demo workflows:")
            for name, func in DEMO_WORKFLOWS.items():
                doc = func.__doc__ or "No description"
                print(f"  {name:25s}  {doc.strip()}")
        elif arg == "--demo" and len(sys.argv) > 2:
            demo_name = sys.argv[2]
            if demo_name in DEMO_WORKFLOWS:
                DEMO_WORKFLOWS[demo_name]()
            else:
                print(f"Unknown demo: {demo_name}")
                print("Available: " + ", ".join(DEMO_WORKFLOWS.keys()))
                sys.exit(1)
        elif arg == "--help":
            print(__doc__)
        else:
            print(f"Unknown argument: {arg}")
            print("Usage: python main.py [--demo NAME | --list-demos | --help]")
            sys.exit(1)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
\n# Data Analytics agent registered in departments/__init__.py\n# To use: from departments import DataAnalyticsAgent\n