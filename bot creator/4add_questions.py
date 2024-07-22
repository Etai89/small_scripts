import openai
import time
import random
import json
import os.path
import winsound
import settings_file as sf

openai.api_key = sf.API_TOKEN
number_of_questions = sf.MORE_QUESTIONS

# Define the create_json() function to create a new JSON file for the questions and answers
def create_json():
    data = {
        "intents": []
    }
    with open(sf.JSON_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Create a new JSON file for the questions and answers if it does not exist
if not os.path.exists('intents.json'):
    create_json()

# Load the questions and answers from the JSON file
with open(sf.JSON_FILE, 'r') as f:
    data = json.load(f)

# Add any new questions to the JSON file
def add_question(tag, question, answer):
    num_pattern = r"^\d+\."
    question_added = False
    for intent in data["intents"]:
        if intent["tag"] == tag:
            intent["patterns"] += [q for q in question if q and q not in [num_pattern, 'Questions.append(', 'print(Questions)', 'Questions', 'Questions = [', 'Questions:', 'Questions =', '[', ']', '"']]
            question_added = True
            break
    if not question_added:
        new_question = {
            "tag": tag,
            "patterns": [q for q in question if q and q not in [num_pattern, 'Questions.append(', 'print(Questions)', 'Questions', 'Questions = [', 'Questions:', 'Questions =', '[', ']', '"']],
            "responses": [answer]
        }
        data["intents"].append(new_question)
    with open(sf.JSON_FILE, 'w') as f:
        json.dump(data, f, indent=4)




def get_tag_number(tag):
    tag_numbers = [int(intent["tag"].split("_")[1]) for intent in data["intents"] if intent["tag"].startswith(tag)]
    if tag_numbers:
        return max(tag_numbers) + 1
    else:
        return 1

def get_response(prompt):
    completions = openai.Completion.create(
        engine=sf.ENGINE_TYPE,
        prompt=prompt,
        max_tokens=sf.MAX_TOKENS,
        n=1,
        stop=None,
        temperature=sf.TEMPERATURE_LEVEL,
    )

    message = completions.choices[0].text
    return message.strip()

def main():
    for intent in data["intents"]:
        patterns = intent["patterns"]
        if len(patterns) == sf.MIN_QUESTIONS_GENERATE:
            generated_questions = []
            for pattern in patterns:
                current_question = f"rephrase the question '{pattern}' {number_of_questions} different times and print each set of questions in a list"
                print("\n" + current_question + "\n")
                response = get_response(current_question)
                generated_questions += response.split("\n")
                time.sleep(1)
            print(f"Generated questions: {generated_questions}")
            add_question(intent["tag"], generated_questions, response)


if __name__ == "__main__":
    main()
    # Play a Windows sound when the program finishes running
    print("done!")
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
