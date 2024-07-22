import os
import random
import schedule
import time
import pygame
import threading

# Function to play a random song from a specified folder
def play_random_song(folder_path):
    # Get a list of all audio files in the folder
    audio_files = [file for file in os.listdir(folder_path) if file.endswith(('.mp3', '.wav', '.ogg'))]
    
    if not audio_files:
        print("No audio files found in the specified folder.")
        return
    
    # Select a random audio file
    random_song = random.choice(audio_files)
    
    # Construct the full path to the selected song
    song_path = os.path.join(folder_path, random_song)
    
    # Initialize pygame mixer
    pygame.mixer.init()
    
    try:
        # Load and play the selected song
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        # Wait for the song to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Adjust the tick rate as needed
    except pygame.error as e:
        print(f"Error playing the audio: {e}")
    
    # Clean up resources
    pygame.mixer.quit()

# Function to add an alarm
def add_alarm(time_str, folder_path):
    schedule.every().day.at(time_str).do(play_random_song, folder_path)
    print(f"Alarm set for {time_str}")
    save_alarms()

# Function to cancel an alarm
def cancel_alarm(time_str):
    for job in schedule.get_jobs():
        if job.next_run.strftime("%H:%M") == time_str:
            schedule.cancel_job(job)
            print(f"Alarm at {time_str} canceled.")
            save_alarms()

# Function to save alarms to a text file
def save_alarms():
    with open("alarms.txt", "w") as f:
        for job in schedule.get_jobs():
            f.write(f"{job.next_run.strftime('%H:%M')}\n")

# Function to load alarms from a text file
def load_alarms():
    if os.path.exists("alarms.txt"):
        with open("alarms.txt", "r") as f:
            for line in f:
                time_str = line.strip()
                add_alarm(time_str, audio_folder)

# Function to run scheduler in a separate thread
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Specify the folder containing the audio files
    audio_folder = "C:/Users/senio/Downloads/432hz songs"

    # Load existing alarms from text file
    load_alarms()

    # Start scheduler thread
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True  # Set the thread as daemon
    scheduler_thread.start()

    # Main menu loop
    while True:
        print("\nMenu:")
        print("1. Add Alarm")
        print("2. Cancel Alarm")
        print("3. View All Alarms")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            time_str = input("Enter the time for the alarm (HH:MM): ")
            add_alarm(time_str, audio_folder)
        elif choice == "2":
            time_str = input("Enter the time of the alarm to cancel (HH:MM): ")
            cancel_alarm(time_str)
        elif choice == "3":
            print("Scheduled Alarms:")
            for job in schedule.get_jobs():
                print(job.next_run.strftime("%H:%M"))
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
