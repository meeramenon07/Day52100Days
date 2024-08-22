import os,time
pizzaStuff = []

try:
  f = open("Stuff.txt","r")
  Stuff = eval(f.read())
  f.close()
except:
  print("Error: existing list is blank")

def view():
  name = "Name"
  size = "Size"
  quantity = "Quantity"
  total = "Total Cost"
  print(f"{name: ^10}{size:^7}{quantity:^10}{total:^10}")
  for row in pizzaStuff :
    print(f"{row[0]:^10}{row[1]:^7}{row[2]:^10}{row[3]:^10}")
    time.sleep(1)

def add():
    time.sleep(1)
    os.system("clear")
    name = input("Your Name ? > ")
    size = input("What size : small,medium or large? > ")
    while True:
      try:
        quantity = int(input("Quantity > "))
        break
      except:
        print("Error: Quanity must be a whole number >  ")
    cost = 0
    if size == "small":
      cost = 7.00
    elif size == "medium":
      cost = 10.00
    else:
      cost = 15.00
    total = cost * quantity 
    total = round(total,2)

    print(name, "Your total cost is", total)
    row = [name,size,quantity, total]
    pizzaStuff.append(row)

while True:
  time.sleep(1)
  os.system("clear")
  print("Pizza Stuff Pizza ")
  print()
  menu = input("1: Add Pizza \n 2: View Pizza  \n")
  if menu == "1":
    add()
  else:
    view()
  f = open("pizzaStuff.txt", "w")
  f.write(str(pizzaStuff))
  f.close()

    

  





















































































































































































































#pizza = []

#try:
  #f = open("pizza.txt", "r")
  #pizza = eval(f.read())
  #f.close()
#except:
  #print("ERROR: No existing #pizza list, using a blank #list")

#def viewPizza():
  #h1 = "Name"
  #h2 = "Topping"
  #h3 = "Size"
  #h4 = "Quantity"
  #h5 = "Total"
  #print(f"{h1:^10}{h2:^20}{h3:^10}{h4:^10}{h5:^10}")
  #for row in pizza:
    #print(f"{row[0]:^10}#{row[1]:^20}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
  #time.sleep(2)

#def addPizza():
  #time.sleep(1)
  #os.system("clear")
  #name = input("Name: ")
  #toppings = input("Toppings: ")
  #size = input("Size (s/m/l): ").lower()
  #while True:
    #try:
      #qty = int(input("Quantity: "))
      #break
    #except:
      #print("Error: Quanity must be a whole number")
  #cost = 0
  #if size=="s":
    #cost = 5.99
  #elif size=="m":
    #cost = 9.99
  #else:
    #cost = 14.99
  #total = cost * qty
  #total = round(total, 2)
  #row = [name, toppings, size, qty, total]
  #pizza.append(row)

#while True:
  #time.sleep(1)
  #os.system("clear")
  #print("Rominos Pizza")
  #print()
  #menu = input("1: Add Pizza\n2: View Pizzas\n> ")
  #if menu == "1":
    #addPizza()
  #else:
    #viewPizza()
  #f = open("pizza.txt", "w")
  #f.write(str(pizza))
  #f.close()



