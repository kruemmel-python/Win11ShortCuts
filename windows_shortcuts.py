import tkinter as tk


additional_shortcuts = {
    "ALT+ESC": "Durchlaufen sie geöffnete Fenster",
    "ALT+F4": "Aktives Fenster schließen",
    "ALT+F8": "Zeigt das eingegebene Kennwort auf dem Anmeldebildschirm an",
    "ALT+NACH-LINKS-TASTE": "Zurück",
    "ALT+BILD-AB": "Um einen Bildschirm nach unten navigieren",
    "ALT+BILD-AUF": "Um einen Bildschirm nach oben verschieben",
    "ALT+NACH-RECHTS-TASTE": "Vorwärts",
    "ALT+LEERTASTE": "Kontextmenü für das aktive Fenster öffnen",
    "ALT+TAB": "Wechseln Sie zwischen geöffneten Apps",
    "ALT+Unterstrichener Buchstabe": "Führt den Befehl für den unterstrichenen Buchstaben in Apps aus",
    "STRG+ALT+TAB": "Geöffnete Apps anzeigen",
    "STRG+PFEILTASTEN": "Startmenügröße ändern",
    "STRG+PFEILTASTEN (zur Auswahl) + LEERTASTE": "Wählen Sie mehrere Elemente auf dem Desktop oder Explorer aus",
    "STRG+Klicken auf eine gruppierte App-Schaltfläche": "Durchlaufen Sie Fenster in der Gruppe von der Taskleiste aus",
    "STRG+NACH-UNTEN-TASTE": "Bewegen Sie den Cursor an den Anfang des nächsten Absatzes",
    "STRG+F5 (oder) STRG+R": "Aktuelles Fenster aktualisieren",
    "STRG+NACH-LINKS-TASTE": "Bewegen Sie den Cursor an den Anfang des vorherigen Worts",
    "STRG+NACH-RECHTS-TASTE": "Bewegen Sie den Cursor an den Anfang des nächsten Worts",
    "STRG+UMSCHALT": "Tastaturlayout wechseln",
    "STRG+UMSCHALT+PFEILTASTE": "Textblock auswählen",
    "STRG+UMSCHALT+Schaltfläche 'App klicken'": "Führen Sie die App über die Taskleiste als Administrator aus",
    "STRG+UMSCHALT+ESC": "Task-Manager öffnen",
    "STRG+LEERTASTE": "Aktivieren oder deaktivieren Sie den chinesischen IME",
    "STRG+NACH-OBEN-TASTE": "Bewegen des Cursors an den Anfang des vorherigen Absatzes",
    "UMSCHALT+PFEILTASTEN": "Wählen Sie mehrere Elemente aus",
    "UMSCHALT+App-Schaltfläche klicken": "Öffnen Sie eine weitere Instanz einer App über die Taskleiste",
    "UMSCHALT+F10": "Kontextmenü für ausgewähltes Element öffnen",
    "UMSCHALT+Rechtsklick-App-Schaltfläche": "Fenstermenü für die App über die Taskleiste anzeigen",
    "UMSCHALT+Rechtsklick auf die Schaltfläche 'Gruppierte App'": "Fenstermenü für die Gruppe auf der Taskleiste anzeigen",
    "Windows-TASTE+TAB": "Vorgangsansicht öffnen",
    "Windows-Taste+STRG+D": "Hinzufügen eines virtuellen Desktops",
    "Windows-TASTE+STRG+NACH-RECHTS-TASTE": "Wechseln Sie zwischen virtuellen Desktops, die Sie auf der rechten Seite erstellt haben",
    "Windows-TASTE+STRG+NACH-LINKS-TASTE": "Wechseln Sie zwischen virtuellen Desktops, die Sie auf der linken Seite erstellt haben",
    "Windows-TASTE+STRG+F4": "Schließen Sie den virtuellen Desktop, den Sie verwenden",
    "Windows-Taste": "Startmenü öffnen",
    "Windows-Taste+A": "Öffnen Sie das Info-Center",
    "Windows-TASTE+ALT+D": "Datum und Uhrzeit des Öffnens in der Taskleiste",
    "Windows-Taste+ALT+Zahl (0-9)": "Öffnen Sie die Sprungliste der App in der Zahlenposition auf der Taskleiste",
    "Windows-Taste+B": "Legen Sie den Fokusbenachrichtigungsbereich auf der Taskleiste fest",
    "Windows-Taste+C": "Copilot öffnen/schließen",
    "Windows-Taste+Komma (,)": "Vorübergehender Blick auf den Desktop",
    "Windows-Taste+STRG+D": "Erstellen eines virtuellen Desktops",
    "Windows-TASTE+STRG+EINGABETASTE": "Sprachausgabe öffnen",
    "Windows-TASTE+STRG+F": "Öffnen Sie die Suche nach dem Gerät in einem Domänennetzwerk",
    "Windows-Taste+STRG+F4": "Schließen Sie den aktiven virtuellen Desktop",
    "Windows-TASTE+STRG+NACH-LINKS-TASTE": "Wechseln Sie zum virtuellen Desktop auf der linken Seite",
    "Windows-Taste+STRG+Zahl (0-9)": "Wechseln Sie zum letzten aktiven Fenster der App in der Nummernposition auf der Taskleiste",
    "Windows-Taste+STRG+Q": "Öffnen Sie Schnellhilfe",
    "Windows-TASTE+STRG+NACH-RECHTS-TASTE": "Wechseln Sie zum virtuellen Desktop auf der rechten Seite",
    "Windows-Taste+STRG+UMSCHALT+B": "Reaktivieren Sie das Gerät, wenn sie schwarz oder leer ist",
    "Windows-TASTE+STRG+UMSCHALT+Zahl (0-9)": "Öffnen Sie eine weitere Instanz als Administrator der App in der Nummerposition auf der Taskleiste",
    "Windows-Taste+STRG+LEERTASTE": "Ändern Sie die zuvor ausgewählte Eingabeoption",
    "Windows-Taste+D": "Anzeigen und Ausblenden des Desktops",
    "Windows-TASTE+NACH-UNTEN-TASTE": "App-Fenster minimieren",
    "Windows-Taste+E": "Öffnen Sie Explorer",
    "Windows-Taste+ESC": "Bildschirmlupe beenden",
    "Windows-Taste+F": "Starten Sie die Feedback-Hub-App",
    "Windows-Taste+Schrägstrich (/)": "Starten Sie die IME-Neuversion",
    "Windows-Taste+G": "Starten Sie die Spieleleisten-App",
    "Windows-Taste+H": "Funktion zum Öffnen des Diktats",
    "Windows-Taste+Start": "Minimieren oder maximieren Sie alle außer dem aktiven Desktopfenster",
    "Windows-Taste+I": "Einstellungen öffnen",
    "Windows-Taste+J": "Legen Sie den Fokus auf einen Tipp für Windows 10 fest, falls zutreffend",
    "Windows-Taste+K": "Öffnen Sie die Verbindungseinstellungen",
    "Windows-Taste+L": "Sperrt den Computer",
    "Windows-Taste+NACH-LINKS-TASTE": "App oder Fenster nach links ausrichten",
    "Windows-Taste+M": "Minimieren Sie alle Fenster",
    "Windows-TASTE+Minus (-)": "Verkleinern Sie die Bildschirmlupe",
    "Windows-Taste+Zahl (0-9)": "Öffnen Sie die App an der Position der Zahl auf der Taskleiste",
    "Windows-Taste+O": "Geräteausrichtung sperren",
    "Windows-Taste+P": "Öffnen Sie die Projekteinstellungen",
    "Windows-Taste+Pause": "Dialogfeld 'Systemeigenschaften anzeigen'",
    "Windows-Taste+Punkt (.) oder Semikolon (;)": "Emoji-Bereich öffnen",
    "Windows-Taste+Plus (+)": "Vergrößern Sie die Bildschirmlupe",
    "Windows-Taste+PrtScn": "Erfassen Sie einen vollständigen Screenshot im Ordner 'Screenshots'"
    
}
def update_search(*args):
    search_query = search_var.get().upper()
    text_box.delete(1.0, tk.END)
    for shortcut, description in additional_shortcuts.items():
        if shortcut.startswith(search_query):
            text_box.insert(tk.END, f"{shortcut}: {description}\n")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Windows 11 Tastenkombinationen")

# Suchfeld erstellen
search_var = tk.StringVar()
search_var.trace("w", update_search)
entry = tk.Entry(root, textvariable=search_var)
entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# Textbox erstellen und an das Fenster anpassen
text_box = tk.Text(root, height=20, width=80)
text_box.pack(fill=tk.BOTH, expand=True)

# Hauptloop starten
root.mainloop()
