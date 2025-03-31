import yaml
import os

def validate_rule_file(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    required_keys = ['description', 'category', 'tags', 'status', 'version', 'risk', 'rule']
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required field: {key}")
    print(f"{file_path} is valid.")

if __name__ == "__main__":
    import sys
    rules_dir = sys.argv[1]
    for root, _, files in os.walk(rules_dir):
        for file in files:
            if file.endswith('.yml') or file.endswith('.yaml'):
                validate_rule_file(os.path.join(root, file))
