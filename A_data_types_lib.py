# PLEASE NOTE: This snippet deals with the most basic data types in Python

### AUFGABE: Um welchen Datentypen handelt es sich bei a bis j?

a = "Welcome to this course!"
b = 42
c = 13.7603
d = 1j
e = ["FRA", "LHR", "VIE", "BER", "BRU", "JFK"]
f = ("Waldviertel", "Weinviertel", "Mostviertel", "Industrieviertel")
g = range(4,10)
h = {"item": "jeans", "category": "trousers"}
i = {"jeans", "leggings", "tights"}
j = True

def showDataTypes(VAR):
    print()
    print("***WERT:***")
    print(VAR)
    print()
    print("***DATENTYP***")
    print(type(VAR))

####### MAIN - replace letters here
showDataTypes(i)

# FYI: what "range" does
#for numbers in range(8):
#    print(numbers)