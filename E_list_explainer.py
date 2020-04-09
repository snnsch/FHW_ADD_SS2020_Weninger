# PLEASE NOTE: This snippet outlines some of the most basic functions in dealing with Python lists

### AUFGABE: Diese Methoden zeigen Ihnen, was Sie alles mit Python lists machen können.
# Bitte überlegen Sie sich für jede Methode, was der Output sein könnte, bevor Sie sie ausführen.

a = ["a", "b", "c", "d"]
b = ["d", "c", "b", "a"]
c = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

def lists_are_ordered():
  print()
  if a == b:
    print(">>> lists ARE identical")
  if a != b:
    print(">>> lists are NOT identical")
  else:
    print("You messed up your code somehow ;-)")

#lists_are_ordered()

def access_by_index():
  print(">>> accessed by index")
  print("'a' an der Stelle 3:",a[3])

#access_by_index()

def keyword_in():
  print("*** keyword in:")
  print("Kommt 'bar' in c vor?","bar" in c)

#keyword_in()

def append_to_list():
  print("List c without alterations")
  print (c)
  print ("Same list with alterations:")
  d = c + ['kitty', 'dog']
  print(d)
  d.append("ADD is cool")
  print(d)

#append_to_list()

def list_length():
  print("Länge von 'b'",len(b),"// Länge von 'c'",len(c))

#list_length()

def replace_items():
  print (c,"List d without alterations")
  c[2] = 10
  #c[-1] = 2.97
  #print (c,"List with alterations")

#replace_items()

def access_by_range():
  print(c)
  #print("Access 'c' von 1 bis 4:",c[0:1])

#access_by_range()

def insert_item():
  print("Was wurde hier eingefügt?")
  print(c)
  #c.insert(4,"added at index 4")
  #print(c)

#insert_item()

def remove_item():
  print("Was wurde hier entfernt und wie?")
  print("Original:",c)
  # remove by item (if item in list)
  #c.remove('quux')
  print(c)
  # remove by index
  #c.remove(c[3])
  #print(c)

#remove_item()



