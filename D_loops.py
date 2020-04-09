# PLEASE NOTE: This snippet is about basic "for" and "while" loops in Python and showcases their functionality in five basic functions

### AUFGABE: In dieser Einheit üben wir das Lesen von Code am Beispiel von Schleifen.
# Lesen Sie sich jede Methode durch, überlegen Sie sich den möglichen Output.
# Dann führen Sie jede Methode aus - be prepared to run your colleagues through the code.

def noten_geber():
    grades = ["1er", "2er", "3er", "4er", "5er"]
    for grade in grades:
        print("Dies ist eine gültige Note:", grade)

#noten_geber()

def iterator():
    for number in range(1, 6):
        print(number,"er")

#iterator()

def student_name_checker_FOR():
    student_list = ["Julia", "Stephan", "Jasmina", "Martin Josef", "Petra", "Manuel"]
    for name in student_list:
        if "e" in name:
            print("Der Name", name, "enthält den Buchstaben >>E<<")
        else:
            print("** Kein >>E<< im Namen", name, "enthalten")
        print()

#student_name_checker_FOR()

def student_name_checker_WHILE():
    student_list = ["Julia", "Stephan", "Jasmina", "Martin Josef", "Petra", "Manuel"]
    iterator = 0
    while iterator < len(student_list):
        if "e" in student_list[iterator]:
            print("Der Name", student_list[iterator], "enthält den Buchstaben >>E<<")
        else:
            print("** Kein >>E<< im Namen", student_list[iterator], "enthalten")
        iterator += 1                                                                   # SCOPE!
        print()                                                                         # SCOPE!
    print("END: This text will only be displayed once while has finished iterating")    # SCOPE!

#student_name_checker_WHILE()

def collect_user_input():
    print("I am your MEMORY - as long as you want to, I shall memorize everything you write.")
    print("Let's begin, please write your first text:")
    users_memory = []
    while True:
        to_memorize = input().lower()
        if to_memorize != "stop":
            users_memory.append(to_memorize)
            print("YOUR MEMORY:",users_memory)
            print("What else do you want to memorize? ** End this by writing STOP **")
        elif to_memorize == "stop":
            print("Thank you - here's your final memory:")
            print(users_memory)
        else:
            print("Oops, something bad has happened :-(")
        print()

#collect_user_input()





