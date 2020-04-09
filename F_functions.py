# PLEASE NOTE: This code snippet illustrates different types of functions (with/without input argument, with/without return statement)

### AUFGABE: Hier finden Sie eine beispielhafte Teilimplementierung des "Eierspeise"-Algorithmus.
# 4 Methoden wurden implementiert, die auch zeigen sollen, wie unterschiedlich Methoden verwendet werden können
# (mit/ohne input argument / return statement)
# Lesen Sie sich den Code durch, führen Sie ihn aus, verändern Sie sinnvolle Variablen, um zu verstehen, wie er funktioniert.

import random

# function is called without argument, returns Boolean
def rezept_gesucht():
    print("Ein Rezept auf Google gefunden?")
    return True

# function is called with one argument, returns value
def zutaten_pruefen(zu_testen):
    zutaten_needed = ["Eier", "Öl", "Milch", "Chilli", "Schwarzbrot", "Kräuter"]
    zutaten_daheim = zu_testen
    for habe_zutat in zutaten_daheim:
        if habe_zutat in zutaten_needed:
            print(habe_zutat,"- ok")
        else:
            print("Fehler")
    diff = list(set(zutaten_needed) - set(zutaten_daheim))
    return diff

# function is called without argument, returns no argument but executes code directly
def kochen():
    lucky_cooking = random.randint(1,3)
    if lucky_cooking == 1:
        print("Wow, dir ist die perfekte Eierspeise gelungen!")
    elif lucky_cooking == 2:
        print("Naja, die Eierspeise ist nur essbar, aber ok, hilft gegen Hunger, immerhin.")
    else:
        print("Oh Gott, kann man nicht essen - NEU ANFANGEN!")

# MAIN FUNCTION can work with all the other functions => needs to come last
def eierspeise_kochen():
    print("")
    print("*** SCHRITT 1:")
    if rezept_gesucht() == True:
        print("Ja, Rezept gefunden, weiter geht's! :)")
        print()
        print("*** SCHRITT 2:")
        zutaten_geprueft = zutaten_pruefen(["Kräuter", "Öl", "Milch", "Chilli", "Schwarzbrot"])
        if zutaten_geprueft == []:
            print("Perfekt, alles da")
            print("")
            print("*** FERTIG GEKOCHT:")
            kochen()
        else:
            print("Verdammt... Ich muss noch einkaufen gehen - es fehlen:", zutaten_geprueft)

# CALL MAIN
eierspeise_kochen()
