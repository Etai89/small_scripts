
import openai
import time
import pyttsx3
import random
import json
import os.path
import winsound
import settings_file as sf


openai.api_key = sf.API_TOKEN

# Define the path to the file containing the questions
QUESTIONS_FILE = sf.TXT_FILE

# Load the questions from the file into a list
with open(QUESTIONS_FILE, 'r') as f:
    questions = f.read().splitlines()

asked_questions = []

# Define the create_json() function to create a new JSON file for the questions and answers
def create_json():
    data = {
        "intents": []
    }
    with open(sf.JSON_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Create a new JSON file for the questions and answers if it does not exist
if not os.path.exists(sf.JSON_FILE):
    create_json()

# Load the questions and answers from the JSON file
with open(sf.JSON_FILE, 'r') as f:
    data = json.load(f)

# Add any new questions to the JSON file
def add_question(tag, question, answer):
    new_question = {
        "tag": tag,
        "patterns": [question],
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

voices = pyttsx3.init().getProperty('voices')

def female(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()

def male(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()

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
    for question in questions:
        tag = f"tag_{get_tag_number('tag')}"
        response = get_response(question)
        # male(question)
        print(f"Question: {question}")
        print(f"Answer: {response}")
        # female(response)
        add_question(tag, question, response)

if __name__ == "__main__":
    main()
    # Play a Windows sound when the program finishes running
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
