import json
import os


def save(filename, data):
    with open('cache/' + filename, 'w+') as f:
        f.write(json.dumps(data))

    return True


def load(filename):
    if not os.path.exists('cache/' + filename):
        return False

    with open('cache/' + filename, 'r') as f:
        data = json.loads(f.read())

    return data
