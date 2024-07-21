from tkinter import *
from datetime import datetime, timedelta

def calculate_time():
    start_date = datetime(2023, 9, 8)
    current_datetime = datetime.now()
    elapsed_time = current_datetime - start_date

    seconds = elapsed_time.total_seconds()
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    weeks = days / 7
    months = current_datetime.month - start_date.month + 12 * (current_datetime.year - start_date.year)
    # Add 9 months to the start date
    estimated_time_of_birth = start_date + timedelta(days=9*30)
    
    # Calculate time left for birth
    time_left = estimated_time_of_birth - current_datetime
    days_left = time_left.days
    months_left = days_left // 30
    weeks_left = days_left // 7
    
    timer.config(text=f"כמה זמן אנחנו בהריון\n\n"
                 f"{int(seconds):,} שניות\n"
                 f"{int(minutes):,} דקות\n"
                 f"{int(hours):,} שעות\n"
                 f"{int(days):,} ימים\n"
                 f"{int(weeks):,} שבועות\n"
                 f"{int(months):,} חודשים\n"
                 f"\nכמה זמן נותר עד הלידה\n"
                 f"{days_left} ימים\n"
                 f"{weeks_left} שבועות\n"
                 f"{months_left} חודשים")
    etai.after(1000, calculate_time)

# Root window
etai = Tk()
etai.title("מעקב הריון")
etai.geometry('540x600+100+20')

# Background color
etai.configure(bg="#f0f0f0")

# Label for the title
title_label = Label(etai, text="מעקב הריון - איתי ומירב", font=("Tahoma", 20), bg="#f0f0f0", fg="#333")
title_label.pack(side="top", pady=20)

# Label for the start date
start_date_label = Label(etai, text="תאריך תחילת הספירה: 08.09.2023", font=("Tahoma", 14), bg="#f0f0f0", fg="#333")
start_date_label.pack()

# Label for the estimated time of birth
start_date = datetime(2023, 9, 8)
estimated_time_of_birth = start_date + timedelta(days=9*30)
etb_label = Label(etai, text=f"תאריך לידה משוער: {estimated_time_of_birth.strftime('%d.%m.%Y')}", font=("Tahoma", 14), bg="#f0f0f0", fg="#333")
etb_label.pack()

# Label for the timer
timer = Label(etai, text="", font=("Tahoma", 18), bg="#f0f0f0", fg="#333")
timer.pack(side="top", pady=20)

# Function call to update the timer
calculate_time()

# Run the application
etai.mainloop()
