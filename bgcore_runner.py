import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="BiasGuard CORE Runner")
    parser.add_argument("--rules", required=True, help="Path to rules YAML file")
    parser.add_argument("--data", required=True, help="Path to dataset CSV file")
    args = parser.parse_args()

    rules_path = Path(args.rules)
    data_path = Path(args.data)

    if not rules_path.exists():
        raise FileNotFoundError(f"Rules file not found: {rules_path}")
    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found: {data_path}")

    print(f"Running BiasGuard on rules: {rules_path} with dataset: {data_path}")
    # Placeholder for rule engine integration

if __name__ == "__main__":
    main()
