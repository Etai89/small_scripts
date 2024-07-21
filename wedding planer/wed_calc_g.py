import tkinter as tk
from tkinter import Frame
import json




# Variables
FONT1 = 'Tahoma'
SIZE1 = '12'
SIZE2 = '13'
C1 = 'lightblue'
C2 = 'blue'
C3 = 'lightblue'
C4 = 'purple'
CB1 = 'gold'
CB2 = 'green'
SIZE3 = '15'

def calculate_wedding_expenses():
    global guest_presents_entry  # Declare the variable as global

    num_guests = int(num_guests_entry.get())
    meal_cost = int(meal_cost_entry.get())
    food_cost = num_guests * meal_cost
    
    dj_cost = int(dj_cost_entry.get())
    rav_cost = int(rav_entry.get())
    akum_cost = int(akum_entry.get())
    rabanut = int(rabanut_entry.get())
    bride_guide = int(bride_guide_entry.get())
    groom_guide = int(groom_guide_entry.get())
    wedding_rings = int(wedding_rings_entry.get())
    photographer = int(photographer_cost_entry.get())
    photographer_magnets = int(photographer_magnets_entry.get())
    present_for_guests = int(present_for_guests_entry.get())
    design = int(design_cost_entry.get())
    bride_flower = int(bride_flower_cost_entry.get())
    bride_dress = int(bride_dress_cost_entry.get())
    bride_shoes = int(bride_shoes_cost_entry.get())
    groom_suit = int(groom_suit_cost_entry.get())
    groom_shoes = int(groom_shoes_entry.get())
    bride_hair = int(bride_hair_design_entry.get())
    make_up = int(make_up_entry.get())
    groom_hair = int(groom_hair_design_entry.get())
    car_design = int(car_design_entry.get())
    bar = int(bar_cost_entry.get())
    alcohol = int(alcohol_cost_entry.get())
    lights_music = int(lights_music_entry.get())
    pre_presents = int(pre_presents_entry.get())
    hotel = int(hotel_entry.get())
    guest_presents = int(guest_presents_entry.get())

    total_expenses = food_cost + \
        dj_cost + \
        rav_cost + \
        akum_cost + \
        rabanut + \
        bride_guide + \
        groom_guide + \
        wedding_rings + \
        photographer + \
        photographer_magnets + \
        present_for_guests + \
        design + \
        bride_flower + \
        bride_dress + \
        bride_shoes + \
        groom_suit + \
        groom_shoes + \
        bride_hair + \
        make_up + \
        groom_hair + \
        car_design + \
        bar + \
        alcohol + \
        lights_music + \
        hotel + \
        guest_presents
    
    if total_expenses > 100000:
        fg_color3 = 'red'
        bg_color3 = 'lightyellow'
    else:
        fg_color3 = 'green'
        bg_color3 = 'lightgreen'
        
    total_expenses_label.config(text='סה"כ הוצאות\n {:,.2f} ש"ח'.format(total_expenses), bg=bg_color3, fg=fg_color3, font=(FONT1, 17))
    cost_per_guest_label.config(text='עלות אורח\n {:,.2f} ש"ח'.format(total_expenses / num_guests), bg=bg_color3, fg=fg_color3, font=(FONT1, 17))
    
    guest_presents = int(guest_presents_entry.get())
    
    guest_expenses = total_expenses / num_guests
    guest_worth = guest_presents - guest_expenses
    guests_money = guest_presents * num_guests
    
    if guests_money > 80000:
        fg_color2 = 'green'
        bg_color2 = 'lightgreen'
    else:
        fg_color2 = 'red'
        bg_color2 = 'lightyellow'
    
    if guest_worth > 500:
        fg_color = 'green'
        bg_color = 'lightgreen'
    elif guest_worth < 0:
        fg_color = 'red'
        bg_color = 'lightyellow'
    else:
        fg_color = 'green'
        bg_color = 'lightyellow'
    
    guest_presents_label.config(text='סה"כ מתנות\n {:,.2f} ש"ח'.format(guests_money), bg=bg_color2, fg=fg_color2, font=(FONT1, 17))
    guest_worth_label.config(text='רווח ממוצע מאורח\n {:,.2f} ש"ח'.format(guest_worth), bg=bg_color, fg=fg_color, font=(FONT1, 17))

    final_result = guests_money - total_expenses + pre_presents

    if final_result > 0:
        fg_color1 = 'green'
        bg_color1 = 'lightgreen'
    else:
        fg_color1 = 'red'
        bg_color1 = 'lightyellow'

    final_result_label.config(text='\nסה"כ נטו רווחים או הפסדים\n {:,.2f} ש"ח\n'.format(int(final_result)), fg=fg_color1, bg=bg_color1, font=(FONT1, 19))



def save_data():
    file_name = location_label_entry.get() + ".json"
    data = {
        "num_guests": num_guests_entry.get(),
        "meal_cost": meal_cost_entry.get(),
        "dj_cost": dj_cost_entry.get(),
        "rav": rav_entry.get(),
        "akum": akum_entry.get(),
        "rabanut": rabanut_entry.get(),
        "bride_guide": bride_guide_entry.get(),
        "groom_guide": groom_guide_entry.get(),
        "wedding_rings": wedding_rings_entry.get(),
        "photographer_cost": photographer_cost_entry.get(),
        "photographer_magnets": photographer_magnets_entry.get(),
        "present_for_guests": present_for_guests_entry.get(),
        "design_cost": design_cost_entry.get(),
        "bride_flower": bride_flower_cost_entry.get(),
        "bride_dress_cost": bride_dress_cost_entry.get(),
        "bride_shoes": bride_shoes_cost_entry.get(),
        "groom_suit_cost": groom_suit_cost_entry.get(),
        "groom_shoes": groom_shoes_entry.get(),
        "bride_hair_design": bride_hair_design_entry.get(),
        "make_up": make_up_entry.get(),
        "groom_hair_design": groom_hair_design_entry.get(),
        "car_design": car_design_entry.get(),
        "bar_cost": bar_cost_entry.get(),
        "alcohol_cost": alcohol_cost_entry.get(),
        "lights_music": lights_music_entry.get(),
        "pre_presents": pre_presents_entry.get(),
        "hotel": hotel_entry.get(),
        "guest_presents": guest_presents_entry.get(),
        "location": location_label_entry.get()

    }

    with open(file_name, "w") as file:
        json.dump(data, file)

def clear_entries():
    num_guests_entry.delete(0, tk.END)
    meal_cost_entry.delete(0, tk.END)
    dj_cost_entry.delete(0, tk.END)
    rav_entry.delete(0, tk.END)
    akum_entry.delete(0, tk.END)
    rabanut_entry.delete(0, tk.END)
    bride_guide_entry.delete(0, tk.END)
    groom_guide_entry.delete(0, tk.END)
    wedding_rings_entry.delete(0, tk.END)
    photographer_cost_entry.delete(0, tk.END)
    photographer_magnets_entry.delete(0, tk.END)
    present_for_guests_entry.delete(0, tk.END)
    design_cost_entry.delete(0, tk.END)
    bride_flower_cost_entry.delete(0, tk.END)
    bride_dress_cost_entry.delete(0, tk.END)
    bride_shoes_cost_entry.delete(0, tk.END)
    groom_suit_cost_entry.delete(0, tk.END)
    groom_shoes_entry.delete(0, tk.END)
    bride_hair_design_entry.delete(0, tk.END)
    make_up_entry.delete(0, tk.END)
    groom_hair_design_entry.delete(0, tk.END)
    car_design_entry.delete(0, tk.END)
    bar_cost_entry.delete(0, tk.END)
    alcohol_cost_entry.delete(0, tk.END)
    lights_music_entry.delete(0, tk.END)
    pre_presents_entry.delete(0, tk.END)
    hotel_entry.delete(0, tk.END)
    guest_presents_entry.delete(0, tk.END)
    location_label_entry.delete(0, tk.END)



def load_data():
    file_path = location_label_entry.get() + ".json"
    location_label_entry.delete(0, tk.END)
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        
        
        num_guests_entry.insert(0, data["num_guests"])
        meal_cost_entry.insert(0, data["meal_cost"])
        dj_cost_entry.insert(0, data["dj_cost"])
        rav_entry.insert(0, data["rav"])
        akum_entry.insert(0, data["akum"])
        rabanut_entry.insert(0, data["rabanut"])
        bride_guide_entry.insert(0, data["bride_guide"])
        groom_guide_entry.insert(0, data["groom_guide"])
        wedding_rings_entry.insert(0, data["wedding_rings"])
        photographer_cost_entry.insert(0, data["photographer_cost"])
        photographer_magnets_entry.insert(0, data["photographer_magnets"])
        present_for_guests_entry.insert(0, data["present_for_guests"])
        design_cost_entry.insert(0, data["design_cost"])
        bride_flower_cost_entry.insert(0, data["bride_flower"])
        bride_dress_cost_entry.insert(0, data["bride_dress_cost"])
        bride_shoes_cost_entry.insert(0, data["bride_shoes"])
        groom_suit_cost_entry.insert(0, data["groom_suit_cost"])
        groom_shoes_entry.insert(0, data["groom_shoes"])
        bride_hair_design_entry.insert(0, data["bride_hair_design"])
        make_up_entry.insert(0, data["make_up"])
        groom_hair_design_entry.insert(0, data["groom_hair_design"])
        car_design_entry.insert(0, data["car_design"])
        bar_cost_entry.insert(0, data["bar_cost"])
        alcohol_cost_entry.insert(0, data["alcohol_cost"])
        lights_music_entry.insert(0, data["lights_music"])
        pre_presents_entry.insert(0, data["pre_presents"])
        hotel_entry.insert(0, data["hotel"])
        guest_presents_entry.insert(0, data["guest_presents"])
        location_label_entry.insert(0, data["location"])
    except FileNotFoundError:
        pass



# Create the main window
window = tk.Tk()
window.title("איתי - תכנון חתונה")
window.geometry('700x800+400+0')
window.config(bg='lightblue')

title_label = tk.Label(window, text="תכנון חתונה",bg=C3, fg=C4, font=(FONT1, 22))
title_label.pack()

entries_frame = Frame(window, bg=C3)
entries_frame.pack(side="right")
check_states = []
# Create input fields
num_guests_label = tk.Label(entries_frame, text="כמות אורחים",bg=C1, fg=C2, font=(FONT1, SIZE1))
num_guests_label.grid(row=0, column=1, padx=5)
num_guests_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
num_guests_entry.grid(row=0, column=0, padx=5)

meal_cost_label = tk.Label(entries_frame, text="מחיר מנה",bg=C1, fg=C2, font=(FONT1, SIZE1))
meal_cost_label.grid(row=1, column=1, padx=5)
meal_cost_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
meal_cost_entry.grid(row=1, column=0, padx=5)

dj_cost_label = tk.Label(entries_frame, text="DJ",bg=C1, fg=C2, font=(FONT1, SIZE1))
dj_cost_label.grid(row=2, column=1, padx=5)
dj_cost_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
dj_cost_entry.grid(row=2, column=0, padx=5)

rav_label = tk.Label(entries_frame, text="רב",bg=C1, fg=C2, font=(FONT1, SIZE1))
rav_label.grid(row=3, column=1, padx=5)
rav_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
rav_entry.grid(row=3, column=0, padx=5)

akum_label = tk.Label(entries_frame, text='אקו"ם',bg=C1, fg=C2, font=(FONT1, SIZE1))
akum_label.grid(row=4, column=1, padx=5)
akum_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
akum_entry.grid(row=4, column=0, padx=5)

rabanut_label = tk.Label(entries_frame, text="רבנות",bg=C1, fg=C2, font=(FONT1, SIZE1))
rabanut_label.grid(row=5, column=1, padx=5)
rabanut_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
rabanut_entry.grid(row=5, column=0, padx=5)

bride_guide_label = tk.Label(entries_frame, text="הדרכת כלות",bg=C1, fg=C2, font=(FONT1, SIZE1))
bride_guide_label.grid(row=6, column=1, padx=5)
bride_guide_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
bride_guide_entry.grid(row=6, column=0, padx=5)

groom_guide_label = tk.Label(entries_frame, text="הדרכת חתנים",bg=C1, fg=C2, font=(FONT1, SIZE1))
groom_guide_label.grid(row=7, column=1, padx=5)
groom_guide_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
groom_guide_entry.grid(row=7, column=0, padx=5)

wedding_rings_label = tk.Label(entries_frame, text='טבעות נישואין',bg=C1, fg=C2, font=(FONT1, SIZE1))
wedding_rings_label.grid(row=8, column=1, padx=5)
wedding_rings_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
wedding_rings_entry.grid(row=8, column=0, padx=5)

photographer_cost_label = tk.Label(entries_frame, text="צלם",bg=C1, fg=C2, font=(FONT1, SIZE1))
photographer_cost_label.grid(row=9, column=1, padx=5)
photographer_cost_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
photographer_cost_entry.grid(row=9, column=0, padx=5)

photographer_magnets_label = tk.Label(entries_frame, text="צלם מגנטים",bg=C1, fg=C2, font=(FONT1, SIZE1))
photographer_magnets_label.grid(row=10, column=1, padx=5)
photographer_magnets_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
photographer_magnets_entry.grid(row=10, column=0, padx=5)

present_for_guests_label = tk.Label(entries_frame, text="מתנות לאורחים",bg=C1, fg=C2, font=(FONT1, SIZE1))
present_for_guests_label.grid(row=11, column=1, padx=5)
present_for_guests_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
present_for_guests_entry.grid(row=11, column=0, padx=5)

design_cost_label = tk.Label(entries_frame, text="עיצוב אולם",bg=C1, fg=C2, font=(FONT1, SIZE1))
design_cost_label.grid(row=12, column=1, padx=5)
design_cost_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
design_cost_entry.grid(row=12, column=0, padx=5)

bride_flower_cost_label = tk.Label(entries_frame, text="זר כלה",bg=C1, fg=C2, font=(FONT1, SIZE1))
bride_flower_cost_label.grid(row=13, column=1, padx=5)
bride_flower_cost_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
bride_flower_cost_entry.grid(row=13, column=0, padx=5)

bride_dress_cost_label = tk.Label(entries_frame, text="שמלת כלה",bg=C1, fg=C2, font=(FONT1, SIZE1))
bride_dress_cost_label.grid(row=14, column=1, padx=5)
bride_dress_cost_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
bride_dress_cost_entry.grid(row=14, column=0, padx=5)

bride_shoes_cost_label = tk.Label(entries_frame, text="נעלי כלה",bg=C1, fg=C2, font=(FONT1, SIZE1))
bride_shoes_cost_label.grid(row=15, column=1, padx=5)
bride_shoes_cost_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
bride_shoes_cost_entry.grid(row=15, column=0, padx=5)

groom_suit_cost_label = tk.Label(entries_frame, text="חליפת חתן",bg=C1, fg=C2, font=(FONT1, SIZE1))
groom_suit_cost_label.grid(row=16, column=1, padx=5)
groom_suit_cost_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
groom_suit_cost_entry.grid(row=16, column=0, padx=5)

groom_shoes_label = tk.Label(entries_frame, text="נעלי חתן",bg=C1, fg=C2, font=(FONT1, SIZE1))
groom_shoes_label.grid(row=17, column=1, padx=5)
groom_shoes_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
groom_shoes_entry.grid(row=17, column=0, padx=5)

bride_hair_design_label = tk.Label(entries_frame, text="עיצוב שיער כלה",bg=C1, fg=C2, font=(FONT1, SIZE1))
bride_hair_design_label.grid(row=18, column=1, padx=5)
bride_hair_design_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
bride_hair_design_entry.grid(row=18, column=0, padx=5)

make_up_label = tk.Label(entries_frame, text="איפור כלה",bg=C1, fg=C2, font=(FONT1, SIZE1))
make_up_label.grid(row=19, column=1, padx=5)
make_up_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
make_up_entry.grid(row=19, column=0, padx=5)

groom_hair_design_label = tk.Label(entries_frame, text="עיצוב שיער חתן",bg=C1, fg=C2, font=(FONT1, SIZE1))
groom_hair_design_label.grid(row=20, column=1, padx=5)
groom_hair_design_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
groom_hair_design_entry.grid(row=20, column=0, padx=5)

car_design_label = tk.Label(entries_frame, text="עיצוב רכב",bg=C1, fg=C2, font=(FONT1, SIZE1))
car_design_label.grid(row=21, column=1, padx=5)
car_design_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
car_design_entry.grid(row=21, column=0, padx=5)

bar_cost_label = tk.Label(entries_frame, text="בר אולם",bg=C1, fg=C2, font=(FONT1, SIZE1))
bar_cost_label.grid(row=22, column=1, padx=5)
bar_cost_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
bar_cost_entry.grid(row=22, column=0, padx=5)

alcohol_cost_label = tk.Label(entries_frame, text="אלכוהול",bg=C1, fg=C2, font=(FONT1, SIZE1))
alcohol_cost_label.grid(row=23, column=1, padx=5)
alcohol_cost_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
alcohol_cost_entry.grid(row=23, column=0, padx=5)

lights_music_label = tk.Label(entries_frame, text="הגברה ותאורה",bg=C1, fg=C2, font=(FONT1, SIZE1))
lights_music_label.grid(row=24, column=1, padx=5)
lights_music_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
lights_music_entry.grid(row=24, column=0, padx=5)

pre_presents_label = tk.Label(entries_frame, text="מתנות מראש",bg=C1, fg=C2, font=(FONT1, SIZE1))
pre_presents_label.grid(row=25, column=1, padx=5)
pre_presents_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
pre_presents_entry.grid(row=25, column=0, padx=5)

hotel_label = tk.Label(entries_frame, text="מלון",bg=C1, fg=C2, font=(FONT1, SIZE1))
hotel_label.grid(row=26, column=1, padx=5)
hotel_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
hotel_entry.grid(row=26, column=0, padx=5)

guest_presents_label = tk.Label(entries_frame, text="ממוצע מתנות מאורח",bg=C1, fg=C2, font=(FONT1, SIZE1))
guest_presents_label.grid(row=27, column=1, padx=5)
guest_presents_entry = tk.Entry(entries_frame,bg=C3, fg=C4, font=(FONT1, SIZE2))
guest_presents_entry.grid(row=27, column=0, padx=5)


buttons_frame = Frame(window, bg=C3)
buttons_frame.pack(side="top")

calculate_button = tk.Button(buttons_frame, text="חישוב החתונה",bg='lightgreen', fg=CB2, font=(FONT1, 18), command=calculate_wedding_expenses)
calculate_button.grid(padx=5, pady=5, row=0, column=0, columnspan=4)

# Load data from the file (if available)
#load_data()

# Create save and clear buttons
save_button = tk.Button(buttons_frame, text="שמירה",bg='lightgreen', fg=CB2, font=(FONT1, 15), command=save_data)
save_button.grid(row=1, column=1, padx=5, pady=10)

clear_button = tk.Button(buttons_frame, text="ניקוי",bg='lightgreen', fg=CB2, font=(FONT1, 15), command=clear_entries)
clear_button.grid(row=1, column=2, padx=5, pady=10)

load_button = tk.Button(buttons_frame, text="טען אולם",bg='lightgreen', fg='green', font=(FONT1, 15), command=load_data)
load_button.grid(row=1, column=3, padx=5, pady=10)

location = Frame(window, bg=C3)
location.pack(side="top")

location_label = tk.Label(location, text="שם האולם",bg=C3, fg='purple', font=(FONT1, 16))
location_label.grid(row=2, column=1, padx=5)
location_label_entry = tk.Entry(location,width=15, bg='lightgreen', fg=C4, font=(FONT1, 18))
location_label_entry.grid(row=2, column=0, padx=5, pady=10)
location_label_entry.focus_set()

SIZE3 = '15'

results_frame = Frame(window, bg=C3)
results_frame.pack(side="top")

# Create result labels
total_expenses_label = tk.Label(results_frame, text='------------------------------------------\n:סה"כ הוצאות',bg=C3, fg='purple', font=(FONT1, SIZE3))
total_expenses_label.grid(row=2, column=0, padx=5)

cost_per_guest_label = tk.Label(results_frame, text='------------------------------------------\n:עלות מנה',bg=C3, fg='purple', font=(FONT1, SIZE3))
cost_per_guest_label.grid(row=3, column=0, padx=5)

guest_presents_label = tk.Label(results_frame, text='------------------------------------------\n:סה"כ מתנות',bg=C3, fg='purple', font=(FONT1, SIZE3))
guest_presents_label.grid(row=4, column=0, padx=5)

guest_worth_label = tk.Label(results_frame, text='------------------------------------------\n:רווח מכל אורח',bg=C3, fg='purple', font=(FONT1, SIZE3))
guest_worth_label.grid(row=5, column=0, padx=5)

final_result_label = tk.Label(results_frame, text='------------------------------------------\n:סה"כ נטו רווחים או הפסדים\n------------------------------------------',bg=C3, fg='purple', font=(FONT1, SIZE3))
final_result_label.grid(row=6, column=0, padx=5)

# Start the GUI event loop
window.mainloop()

