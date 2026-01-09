import json

with open('config.json') as f:
    config = json.load(f)

print(f"Running in {config['mode']} mode")
