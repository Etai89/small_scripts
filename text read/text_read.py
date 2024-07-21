from gtts import gTTS
import os
import pyperclip
import time
import pygame
import pyautogui

# Initialize the pygame mixer
pygame.mixer.init()

# Store the previously copied text
previous_text = None

def minimize():
    pyautogui.hotkey('win', 'down')  # Sending the key combination twice to ensure minimization

def run_this(new_text):
    minimize()
    print("New text detected:", new_text)

    def text_to_speech(text):
        tts = gTTS(text=text, lang='en')
        tts.save('output.mp3')
        pygame.mixer.music.load('output.mp3')
        pygame.mixer.music.play()

    # Use the copied text from the clipboard
    text_to_speech(new_text)
    time.sleep(1)  # Wait for a second to allow the player window to open

if __name__ == "__main__":
    while True:
        # Get the current copied text
        copied_text = pyperclip.paste()

        # Check if the current text is different from the previous one
        if copied_text != previous_text:
            run_this(copied_text)
            previous_text = copied_text
