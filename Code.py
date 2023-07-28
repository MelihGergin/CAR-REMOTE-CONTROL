print("\nCAR REMOTE CONTROL")

print("\n1- Doors"
      "\n2- Lights"
      "\n3- Windows")

try:
  b = "-- No information"
  c = "-- No information"
  d = "-- No information"

  a = int(input("\nWhat do you want to do?"))
  if a == 1:
          b = input("What do you want to do about doors? (Open/Close)")
          if b == "Open":
            print("The doors opened")
          elif b == "Close":
            print("The doors closed.")
          else:
              print("Wrong expression entered...")
  elif a == 2:
          c = input("What do you want to do about lights? (On/Off)")
          if c == "On":
            print("The lights are on.")
          elif b == "Off":
            print("The lights are off.")
          else:
            print("Wrong expression entered...")
  elif a == 3:
          d = input("What do you want to do about windows? (Open/Close)")
          if d == "Open":
            print("The windows opened.")
          elif b == "Close":
            print("The windows closed.")
          else:
            print("Wrong expression entered....")
  else:
    print("Wrong expression entered...")

  e = input("What do you want to control? (Doors/Lights/Windows)")
  if e == "Doors":
    print("Doors", b)
  elif e == "Lights":
    print("Lights", c)
  elif e == "Windows":
    print("Windows", d)
  else:
    print("Wrong expression entered....")
