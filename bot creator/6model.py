import os
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import speech_recognition as sr
import pyttsx3
from tensorflow.keras.models import load_model
import webbrowser
import settings_file as sf

# Load the necessary data
lemmatizer = WordNetLemmatizer()
intents = json.loads(open(sf.JSON_FILE).read())
words = pickle.load(open(sf.WORDS_PKL_FILE, 'rb'))
classes = pickle.load(open(sf.CLASSES_PKL_FILE, 'rb'))
model = load_model(sf.MODEL_FILE)

# Function to clean up the input sentence
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

# Function to create a bag of words from the input sentence
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

# Function to predict the class of the input sentence
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = sf.E_THRESHOLD_VALUE
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

# Function to make the chatbot speak the text
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[sf.SPEAK_VOICE].id)
    engine.setProperty('rate', sf.SPEAK_SPEED)
    print(text)
    engine.say(text)
    engine.runAndWait()


# Greet the user
speak(sf.WELCOME_MESSAGE)
counter = 0
# Main loop to listen for user input and respond accordingly
while True:
    # Use speech recognition to get user input
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = sf.ENERGY_THRESHOLD
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("You: ", end='')
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print(user_input)
    except sr.UnknownValueError:
        speak("Can you please try again?")
        continue
    except sr.RequestError as e:
        print("Please try again later.".format(e))
        continue

    # Check if the user wants to exit the program
    if user_input.lower() == 'get out':
        break

    # Get the predicted class and response from the input sentence
    predictions = predict_class(user_input)
    yt_url = f'https://www.youtube.com/results?search_query={user_input}'
    wk_url = f'https://en.wikipedia.org/wiki/{user_input}'
    gl_url = f'https://www.google.com/search?q={user_input}'

    if not predictions:
        webbrowser.open(gl_url)


        continue

    response = predictions[0]['intent']
    confidence = float(predictions[0]['probability'])

    # If the predicted class is confident enough, respond with a random response from the corresponding intent
    if confidence > sf.PREDICTED_CLASS_VALUE:
        for intent in intents['intents']:
            if intent['tag'] == response:
                response_text = random.choice(intent['responses'])

                finish_question = ["let me know if you need anything else.", "can i help you with something else?", " what else do you want to know?", " yeah pertty much...what else?"]
                finish_question = random.choice(finish_question)
                
                if "why" in user_input.lower():
                    response_text = f"its because {response_text} {finish_question}"

                if "how" in user_input.lower():
                    how_ans = ["well, ", "look, ", "it very simple"]
                    how_ans = random.choice(how_ans)
                    response_text = f"{how_ans} {response_text} {finish_question}"
                    
                speak(response_text)  # Speak the response text
    else:
        response_text = "Can you please try again?"
