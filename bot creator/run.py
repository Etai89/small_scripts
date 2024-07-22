import os
import time
import webbrowser
import settings_file as sf
import subprocess


def open_json():
    print(f"\nOpen '{sf.JSON_FILE}' file !\n")
    time.sleep(1)
    file_path = sf.JSON_FILE
    firefox_path = sf.FIREFOXE_PATH
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
    webbrowser.get('firefox').open(file_path)

def creating_model():
    # creating bot process
    print("\n                      Creating a new Model                      \n")
    time.sleep(3)
    os.system(sf.GET_INFO)
    print("question list created!")
    time.sleep(3)
    os.system(sf.CREATE_LIST)
    print("list are rearranged!")
    time.sleep(3)

    print("learning the answers...")
    os.system(sf.ADD_LIST)
    print("answers have been learned successfully...")
    time.sleep(3)
    print("creating more questions...")
    os.system(sf.ADD_QUESTIONS)
    print("more questions added successfully...")
    time.sleep(3)

    print(f"The quenstions are being answered and saved in  '{sf.JSON_FILE}'")
    time.sleep(5)

    print("Filtering duplicates questions and unwanted values in the questions.")
    print(f"\nlist of values to filter:\n{sf.FILTER_JSON_WORDS}")
    time.sleep(1)
    os.system(sf.FILTER_JSON_FILE)
    time.sleep(1)

    open_json()
    print(f"Training the new Model '{sf.MODEL_FILE}' with the current subject...")
    os.system(sf.TRAIN_MODEL)
    print(f"The new Model '{sf.MODEL_FILE}' have been trained successfully and ready to use!")
    time.sleep(2)

    print(f"running new bot '{sf.MODEL_FILE}'  Model...")
    time.sleep(1)
    os.system(sf.RUN_MODEL)
    os.system(sf.SEQUENSER_FILE)

def add_to_model():
    # add new subject to bot process
    print("Deleting the 'chat_info.txt' and start new one")
    if os.path.exists(sf.TXT_FILE):
        os.remove(sf.TXT_FILE)
        print(f"File '{sf.TXT_FILE}' deleted successfully.")
        time.sleep(2)
    print("adding subject to the new Model..")
    time.sleep(2)
    os.system(sf.GET_INFO)
    print("question list created!")
    time.sleep(3)
    os.system(sf.CREATE_LIST)
    print("list are rearranged!")
    time.sleep(2)

    print("learning the answers...")
    os.system(sf.ADD_LIST)
    print("answers have been learned successfully...")
    time.sleep(3)
    print("creating more questions...")
    os.system(sf.ADD_QUESTIONS)
    print("more questions added successfully...")
    time.sleep(3)

    print(f"The quenstions are being answered and saved in  '{sf.JSON_FILE}'")
    time.sleep(3)

    print("Filtering duplicates questions and unwanted values in the questions.")
    print(f"\nlist of values to filter:\n{sf.FILTER_JSON_WORDS}")
    time.sleep(1)
    os.system(sf.FILTER_JSON_FILE)
    time.sleep(1)

    open_json()
    print(f"Training the new Model '{sf.MODEL_FILE}'with the current subject...")
    os.system(sf.TRAIN_MODEL)
    print(f"The new Model '{sf.MODEL_FILE}' have been trained successfully and ready to use!")
    time.sleep(2)

    print(f"running new bot Model '{sf.MODEL_FILE}'...")
    time.sleep(2)
    os.system(sf.RUN_MODEL)
    os.system(sf.SEQUENSER_FILE)

def add_questions():
    print(f"creating more {sf.MORE_QUESTIONS} questions to each question...")
    os.system(sf.ADD_QUESTIONS)
    print("more questions added successfully...")
    time.sleep(3)

def delete_model():
    # deleting sequence
    print("\n                      Deleting the previous version and create new                       \n")

    if os.path.exists(sf.WORDS_PKL_FILE):
        os.remove(sf.WORDS_PKL_FILE)
        print(f"File '{sf.WORDS_PKL_FILE}' deleted successfully.")
        time.sleep(1)

    if os.path.exists(sf.CLASSES_PKL_FILE):
        os.remove(sf.CLASSES_PKL_FILE)
        print(f"File '{sf.CLASSES_PKL_FILE}' deleted successfully.")
        time.sleep(1)

    if os.path.exists(sf.MODEL_FILE):
        os.remove(sf.MODEL_FILE)

        print(f"File '{sf.MODEL_FILE}' deleted successfully.")
        time.sleep(1)
    if os.path.exists(sf.TXT_FILE):
        os.remove(sf.TXT_FILE)
        print(f"File '{sf.TXT_FILE}' deleted successfully.")
        time.sleep(1)

    if os.path.exists(sf.CLEAR_JSON):
        os.system(sf.CLEAR_JSON)
        print(f"Json file: '{sf.CLEAR_JSON}', cleared successfully.")
        time.sleep(1)

def open_settings():
    print("\nOpen Settings:\n")
    file_path = r"settings_file.py"
    subprocess.Popen(["C:/py/Lib/idlelib/idle.bat", file_path])

def run_model():
    print(f"running  Model '{sf.MODEL_FILE}'...")
    time.sleep(2)
    os.system(sf.RUN_MODEL)

def filter_json():
    print(f"Filtering the Json file : '{sf.MODEL_FILE}'...")
    os.system(sf.FILTER_JSON_FILE)

try:
    print("\n\n                       BOT CREATOR                      \n                      MADE BY ETAI                      \n")
    time.sleep(2)
    choose_what = input(f'''\nMenu:
To Run MODEL '{sf.MODEL_FILE}' choose : '0'
Create a new Model : '1'
Add more Subject : '2'
Delete the current Model : '3'
Settings : '4'
Open JSON file : '5'
Filter the JSON file {sf.JSON_FILE}: '6'
Add more Questions : '7'
Exit : '8'

Terminal:
'''
                        )
    if choose_what == "0":
        run_model()
        os.system(sf.SEQUENSER_FILE)

    if choose_what == "1":
        creating_model()
        os.system(sf.SEQUENSER_FILE)

    if choose_what == "2":
        add_to_model()
        os.system(sf.SEQUENSER_FILE)

    if choose_what == "3":
        delete_model()
        os.system(sf.SEQUENSER_FILE)

    if choose_what == "4":
        open_settings()
        os.system(sf.SEQUENSER_FILE)

    if choose_what == "5":
        open_json()
        os.system(sf.SEQUENSER_FILE)

    if choose_what == "6":
        filter_json()
        os.system(sf.SEQUENSER_FILE)

    if choose_what == "7":
        add_questions()
        os.system(sf.SEQUENSER_FILE)

    if choose_what == "8":
        print("\nExit from program!\n")
        time.sleep(1)
        exit()
    else:
        print(f'''\nMenu:
To Run MODEL '{sf.MODEL_FILE}' choose : '0'
Create a new Model : '1'
Add more Subject : '2'
Delete the current Model : '3'
Settings : '4'
Open JSON file : '5'
Filter the JSON file {sf.JSON_FILE}: '6'
Add more Questions : '7'
Exit : '8'
'''
)
        os.system(sf.SEQUENSER_FILE)
except FileNotFoundError:
    print("Error: one or more files to delete or run could not be found.")
except OSError:
    print("Error: an error occurred while deleting files or running scripts.") 
