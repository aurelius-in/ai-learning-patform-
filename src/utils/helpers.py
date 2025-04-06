import os
import json

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
