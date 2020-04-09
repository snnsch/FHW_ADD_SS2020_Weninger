# PLEASE NOTE: This snippet is about conditionals (if / elif / else) and Booleans (true / false)

### AUFGABE: BEVOR Sie diesen Code ausführen, gehen Sie jedes Beispiel durch und
# überlegen Sie sich, ob die Snippets (1) bis (8) True oder False ergeben
# Schreiben Sie sich Ihre Vermutung auf, dann führen Sie den Code aus => wie haben Sie sich geschlagen? :)

x = 0
y = 5

print("1)",0 < 5)                               # (1) True or False?

print("2)",5 < 0)                               # (2) True or False?

# alles was nicht false ist, ist true => alles größer 0 ist true
if x:                                           # (3) True or False?
  print("3) True",x)
else:
  print("3) False:",x)

if y:                                           # (4) True or False?
  print("4) True", x)
else:
  print("4) False:", x)

if x==0 or y==11:                               # (5) True or False?
  print("5) True: x or y")
else:
  print('5) False: x or y')

if x==0 and y==11:                              # (6) True or False?
  print('6) True: x and y')
else:
  print('6) False: x and y')

if 'aul' in 'grault':                           # (7) True or False?
  print('7) True: aul in grault')
else:
  print('7) False: aul in grault')

if 'quux' in ['foo', 'bar', 'quuxy']:           # (8) True or False?
  print('8) True: quux in foo bar quuxy')
else:
  print('8) False: quux in foo bar quuxy')


# SAMPLE CODE #1: USING CONDITIONALS AND BOOLEANS

print()

# Was muss definiert werden, um "would be great but so tired" zu bekommen?
mood = "angry"
full_of_energy = 1

if mood == "happy" and full_of_energy:
  print("loving our session 2day")
elif mood == "so-so" and full_of_energy:
  print("well, today is a strange 'so lala' day")
elif mood == "happy" and full_of_energy == False:
  print("would be great but so tired")
else:
  print("Sorry, I don't understand your mood ")

# SAMPLE CODE #2: USING CONDITIONALS AND BOOLEANS IN A FUNCTION
# Könnte man erweitern: Liest Liste an Punkten und Namen ein und schleift durch: "Weninger: 5er, Fritsch: 3er" ;-)

def welcheNoteBekommeIch ():
  print("Bitte geben Sie Ihre Gesamtpunkte ein:")
  user_points = input()
  user_points = float(user_points)
  if user_points < 0 or user_points > 100:
    print("Bitte geben Sie eine (Komma-)Zahl zwischen 0 und 100 ein")
    user_points = input()
  else:
    if user_points > 90.1:
      print("Super, ein 1er")
    elif user_points < 90.1 and user_points > 75.1:
      print("2er")
    elif user_points < 75 and user_points > 60.1:
      print("3er")
    elif user_points < 60 and user_points > 50.1:
      print("4er")
    else:
      print("Leider ein 5er")

# MAIN PROGRAMME
print()
welcheNoteBekommeIch()

