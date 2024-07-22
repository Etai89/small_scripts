import json
from tabulate import tabulate
import settings_file as sf


with open(sf.JSON_FILE, 'r') as file:
    data = json.load(file)

intents = []

for intent in data['intents']:
    patterns = intent['patterns']
    responses = intent['responses']
    tag = intent['tag']
    if 'context' in intent:
        context = intent['context']
    else:
        context = None
    intents.append({'patterns': patterns, 'responses': responses, 'tag': tag, 'context': context})

print(tabulate(intents, headers="keys"))


with open(sf.JSON_FILE, 'w') as file:
    json.dump({'intents': []}, file)
    print(f"JSON file '{sf.JSON_FILE}' was cleared.")

