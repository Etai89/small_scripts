import json
import settings_file as sf

# define the list of strings to filter out
filter_strings = sf.FILTER_JSON_WORDS

with open(sf.JSON_FILE, 'r') as f:
    data = json.load(f)

# loop through each intent
for intent in data['intents']:
    unique_questions = []
    # loop through each question and add it to a list of unique questions
    for question in intent['patterns']:
        # check if the question contains any of the filter strings and skip it if it does
        if any(fs in question for fs in filter_strings):
            continue
        if question not in unique_questions:
            unique_questions.append(question)
    # replace the original list of questions with the list of unique questions
    intent['patterns'] = unique_questions

# write the updated data to the same file
with open(sf.JSON_FILE, 'w') as f:
    json.dump(data, f, indent=4)
    print(f"Questions copies and filter strings are deleted successfully!\nThe file {sf.JSON_FILE} Updated...")
