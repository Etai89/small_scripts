import tkinter as tk
import tkinter.messagebox as mbox
import datetime
import json

# Function to save the data in a JSON file
def save_data():
    data = {
        'last_period': last_period.get(),
        'cycle_length': cycle_length.get(),
        'data_log': data_log
    }

    with open('period_tracker.json', 'w') as file:
        json.dump(data, file)

    mbox.showinfo('Save', 'Data saved successfully.')

# Function to load the data from a JSON file
def load_data():
    try:
        with open('period_tracker.json', 'r') as file:
            data = json.load(file)

            last_period.set(data['last_period'])
            cycle_length.set(data['cycle_length'])
            data_log.extend(data['data_log'])

            mbox.showinfo('Load', 'Data loaded successfully.')

    except FileNotFoundError:
        mbox.showwarning('Load', 'No saved data found.')

# Function to calculate and display the next period and alerts
def calculate_period():
    try:
        last_period_date = datetime.datetime.strptime(last_period.get(), '%Y-%m-%d').date()
        cycle_days = int(cycle_length.get())

        next_period_date = last_period_date + datetime.timedelta(days=cycle_days)
        today_date = datetime.datetime.now().date()

        days_left = (next_period_date - today_date).days

        if days_left < 0:
            message = f"Your period is {abs(days_left)} days late!"
        elif days_left == 0:
            message = "Your period is expected today!"
        else:
            message = f"Your period is expected in {days_left} days."

        mbox.showinfo('Next Period', message)

        # Add entry to data log
        data_log.append({
            'date': str(today_date),
            'message': message
        })

        # Calculate clean days and fertility window
        end_of_period_date = last_period_date + datetime.timedelta(days=cycle_days - 1)
        clean_days_date = end_of_period_date + datetime.timedelta(days=1)
        fertility_window_start_date = clean_days_date + datetime.timedelta(days=7)
        fertility_window_end_date = clean_days_date + datetime.timedelta(days=19)

        # Check if clean days have started
        if today_date >= clean_days_date:
            clean_days_left = (fertility_window_start_date - today_date).days

            if clean_days_left < 0:
                message = f"You are in your fertility window. Get ready to conceive!"
            else:
                message = f"You are in your clean days. {clean_days_left} days remaining until fertility window."

            mbox.showinfo('Clean Days', message)

            # Add entry to data log
            data_log.append({
                'date': str(today_date),
                'message': message
            })

        # Check if ready to conceive
        if today_date >= fertility_window_start_date and today_date <= fertility_window_end_date:
            message = "You are ready to conceive!"

            mbox.showinfo('Fertility Window', message)

            # Add entry to data log
            data_log.append({
                'date': str(today_date),
                'message': message
            })

    except ValueError:
        mbox.showerror('Error', 'Invalid date or cycle length.')

# Function to display the log of information
def display_log():
    log_text.delete('1.0', tk.END)

    for entry in data_log:
        log_text.insert(tk.END, f"{entry['date']}: {entry['message']}\n")

# Create the main window
window = tk.Tk()
window.title("Period Tracker")

# Variables
last_period = tk.StringVar()
cycle_length = tk.StringVar()
data_log = []

# Load saved data (if available)
load_data()

# Labels
tk.Label(window, text="Last Period Date:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(window, text="Cycle Length (in days):").grid(row=1, column=0, padx=10, pady=10)

# Entry fields
last_period_entry = tk.Entry(window, textvariable=last_period)
last_period_entry.grid(row=0, column=1, padx=10, pady=10)
cycle_length_entry = tk.Entry(window, textvariable=cycle_length)
cycle_length_entry.grid(row=1, column=1, padx=10, pady=10)

# Buttons
calculate_button = tk.Button(window, text="Calculate", command=calculate_period)
calculate_button.grid(row=2, column=0, padx=10, pady=10)

save_button = tk.Button(window, text="Save", command=save_data)
save_button.grid(row=2, column=1, padx=10, pady=10)

log_button = tk.Button(window, text="Display Log", command=display_log)
log_button.grid(row=2, column=2, padx=10, pady=10)

# Log text
log_text = tk.Text(window, height=10, width=40)
log_text.grid(row=3, columnspan=3, padx=10, pady=10)

# Start the main loop
window.mainloop()
