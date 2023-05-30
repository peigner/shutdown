import tkinter as tk
import os

shutdown_process = None
eingabe_text = None
bestaetigung_label = None

def check_shutdown():
    global shutdown_process, bestaetigung_label
    if shutdown_process is not None:
        os.system('shutdown /a')  # Windows-Befehl zum Abbrechen des Herunterfahrens
        shutdown_process = None
        bestaetigung_label.config(text="Herunterfahren abgebrochen")

def shutdown(minutes):
    global shutdown_process
    seconds = minutes * 60
    check_shutdown()  # Überprüfen und ggf. Abbrechen des vorherigen Herunterfahrens
    shutdown_process = os.system(f'shutdown /s /t {seconds}')  # Windows-Befehl zum Herunterfahren

def herunterfahren():
    global eingabe_text, bestaetigung_label
    eingabe = eingabe_text.get()
    try:
        minuten = int(eingabe)
        shutdown(minuten)
        bestaetigung_label.config(text="PC wird in {} Minuten heruntergefahren".format(minuten))
    except ValueError:
        bestaetigung_label.config(text="Ungültige Eingabe")

def create_gui():
    global eingabe_text, bestaetigung_label
    # GUI erstellen
    window = tk.Tk()
    window.title("PC-Abschaltung")

    eingabe_label = tk.Label(window, text="Anzahl der Minuten:")
    eingabe_label.pack()
    eingabe_text = tk.Entry(window)
    eingabe_text.pack()

    # Bestätigungs-Button
    bestaetigen_button = tk.Button(window, text="Bestätigen", command=herunterfahren)
    bestaetigen_button.pack()

    # Bestätigungstext
    bestaetigung_label = tk.Label(window, text="")
    bestaetigung_label.pack()

    # Button zum Überprüfen und Abbrechen des Herunterfahrens
    check_button = tk.Button(window, text="Shutdown abbrechen", command=check_shutdown)
    check_button.pack()

    # Button für 60 Minuten
    button_60 = tk.Button(window, text="1 Stunde", command=lambda: shutdown(60))
    button_60.pack()

    # Button für 90 Minuten
    button_90 = tk.Button(window, text="1,5 Stunden", command=lambda: shutdown(90))
    button_90.pack()

    # Button für 120 Minuten
    button_120 = tk.Button(window, text="2 Stunden", command=lambda: shutdown(120))
    button_120.pack()

    # Button für 150 Minuten
    button_150 = tk.Button(window, text="2,5 Stunden", command=lambda: shutdown(150))
    button_150.pack()

    window.mainloop()

create_gui()
