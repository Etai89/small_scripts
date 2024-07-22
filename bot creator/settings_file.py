
FIREFOXE_PATH = "C:/Program Files/Mozilla Firefox/firefox.exe"

SEQUENSER_FILE = "run.py"
JSON_FILE = "intents.json"
WORDS_PKL_FILE = "words.pkl"
CLASSES_PKL_FILE = "classes.pkl"
MODEL_FILE = "Etai_model.h5"
TXT_FILE = "chat_info.txt"
CLEAR_JSON = "clear_json.py"
FILTER_JSON_FILE = "filter_json.py"


GET_INFO  = "1getinfo.py"
CREATE_LIST =  "2print_list.py"
ADD_LIST = "3add.py"
ADD_QUESTIONS = "4add_questions,py"
TRAIN_MODEL = "5train.py"
RUN_MODEL = "6model.py"

API_TOKEN = "Get you own API Token from here (https://platform.openai.com/account/api-keys)"
ENGINE_TYPE = "text-davinci-003"
MAX_TOKENS = 2500
TEMPERATURE_LEVEL = 0.1


# Wellcome Message:
WELCOME_MESSAGE = f"welcome, i am {MODEL_FILE}"
#  Speed of Speek:
SPEAK_SPEED = 150
#  Speak Voice:
SPEAK_VOICE = 1
#  Number of questions to Multiply:
MORE_QUESTIONS = 5
#  Number of minimum exists questions to allow Multiplication of questions:
MIN_QUESTIONS_GENERATE = 1
#  Speech Recognition Energy Threshold:
ENERGY_THRESHOLD = 400
#  Function to predict the class of the input sentence Threshold:
E_THRESHOLD_VALUE = 0.25
# If the predicted class is confident enough, respond with a random response from the corresponding intent
PREDICTED_CLASS_VALUE = 0.5



#  Words to Filter in the JSON Filter file:
FILTER_JSON_WORDS = [
    "Questions",
     "Questions 3:",
     "Questions = []",
     "print(questions)",
     "Questions 1:",
     "Questions 2:",
     "questions.append(",
     ")",
     "1. ",
     "Questions = [",
     "]]",
     "[]",
     "[[",
     "[",
     "]",
     "("
    ]
# Questions  Start with:
QUESTIONS_START_WITH = ['"How" or "Why" or "What" or "Does" or "If"or "Can" or "Which" or "Who" or "When" or "Where" or "is"']
# Questions  End with:
QUESTION_END_WITH = "?"






