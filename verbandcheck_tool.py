
from datetime import datetime

# --- Eingabe: Patientendaten ---
NAME = input("PATIENTEN_NAME: ")
GEBURTSTAG = input("GEBURTSDATUM (Format: TT.MM.JJJJ): ")
WUNDE = input("Wunddiagnose: ")

# --- Eingabe & Prüfung: Letzter Verbandwechsel ---
while True:
    datum_str = input("Wann war der letzte Verbandwechsel? (Format: TT.MM.JJJJ): ")
    try:
        letzter_wechsel = datetime.strptime(datum_str, "%d.%m.%Y")
        break
    except ValueError:
        print("Ungültiges Datum! Bitte nochmal im Format TT.MM.JJJJ eingeben.")

# --- Eingabe & Prüfung: Letzte Fotodokumentation ---
while True:
    datum_wd = input("Wann war die letzte Fotodokumentation? (Format: TT.MM.JJJJ): ")
    try:
        letzte_wd = datetime.strptime(datum_wd, "%d.%m.%Y")
        break
    except ValueError:
        print("Ungültiges Datum! Bitte nochmal im Format TT.MM.JJJJ eingeben.")

# --- Berechnungen ---
heute = datetime.now()
tage_seit_wechsel = (heute - letzter_wechsel).days
tage_seit_wd = (heute - letzte_wd).days

# --- Ausgabe ---
print("\n--- Zusammenfassung ---")
print(f"Patient: {NAME}")
print(f"Geburtsdatum: {GEBURTSTAG}")
print(f"Wunddiagnose: {WUNDE}")
print(f"Letzter Verbandwechsel: {datum_str} ({tage_seit_wechsel} Tage her)")
print(f"Letzte Fotodokumentation: {datum_wd} ({tage_seit_wd} Tage her)")

# --- Hinweise zum Verbandwechsel ---
if tage_seit_wechsel >= 2:
    print("Hinweis: Bitte Verbandwechsel prüfen!")
else:
    print("Kein Wechsel nötig – sofern Verband in Ordnung ist.")

# --- Hinweise zur Fotodokumentation ---
if tage_seit_wd >= 30:
    print("Hinweis: Bitte neue Fotodokumentation erstellen.")
else:
    print("Fotodokumentation nur bei Wundveränderung nötig.")
