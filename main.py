import json

with open('config.json') as f:
    config = json.load(f)

if config['mode'] == 'production':
    print("Production mode activated!")
else:
    print("Development mode activated!")
