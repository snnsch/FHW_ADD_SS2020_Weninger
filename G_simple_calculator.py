# Sample code for a basic calculator => please complete this piece of code as outlined by A. Weninger in MS Teams

### AUFGABE: Wie in Teams beschrieben finden Sie hier die Anfänge eines calculator Programms.
# Lesen Sie den Code gut durch und führen Sie ihn mehrmals aus, um die Wirkungsweisen zu verstehen.
# Dann erfüllen Sie die Aufgabe wie in Teams beschrieben.

def calculateNumbers():
    calcs = []
    iterator = 1
    while True:
        print("Zahl Nummer #",iterator,"ODER *FERTIG*?")
        user_choice = input()
        if user_choice.lower() == "fertig":
            break
        else:
            try:
                number = int(user_choice)
                calcs.append(number)
                iterator += 1
                continue
            except ValueError:
                print("It's not an int")
                continue
    print("Hier ist Ihr Ergebnis:")
    print(calcs)
    if chosen_calc == "a":
        sum = 0
        print("Hier ist die Summe folgender Zahlen:", calcs)
        for number in calcs:
            sum += number
        print("SUMME:",sum)
    else:
        "Es gibt ein Problem oder es fehlt etwas!"

def chooseCalcType(choice):
    # Lagern Sie das Überprüfen in eine eigene Methode aus und überlegen Sie sich gut, wann Sie die Überprüfung machen
    pass

# Main programme

print("Wählen Sie ADDITION (A), SUBTRAKTION (S), MULTIPLIKATION (M), DIVISION (D)")
chosen_calc = input().lower()
print("Sie haben",chosen_calc,"gewählt")
calculateNumbers()