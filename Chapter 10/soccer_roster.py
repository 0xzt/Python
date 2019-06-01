count = 1
my_dict = {}
new_dict = {}

#list_jersey = sorted(list_jersey) #Sort the new "list"

while count <= 5:
  jersey_num = int(input("Enter player %d's jersey number:\n" % count))
  rate_num = int(input("Enter player %d's rating:\n" % count))
  my_dict[jersey_num] = rate_num
  list_jersey = list(my_dict.keys())
  list_jersey = sorted(list_jersey)
  count += 1
  print()


print("ROSTER")
for i in list_jersey:
  print("Jersey number: %d, Rating: %d" % (i, my_dict[i]))
  
while True:
  list_jersey = list(my_dict.keys())
  list_jersey = sorted(list_jersey)
  print()
  print("MENU")
  print("a - Add player")
  print("d - Remove player")
  print("u - Update player rating")
  print("r - Output players above a rating")
  print("o - Output roster")
  print("q - Quit") 
  option = input("\nChoose an option:\n")
  if option == "q":
    exit()
  elif option == "o":
    print()
    print("ROSTER")
    for i in list_jersey:
      print("Jersey number: %d, Rating: %d" % (i, my_dict[i]))
  elif option == "a":
    jersey_num2 = int(input("Enter a new player's jersey number:\n"))
    rate_num2 = int(input("Enter the player's rating:"))
    new_dict[jersey_num2] = rate_num2
    my_dict.update(new_dict)
  elif option == "d":
    jersey_remove = int(input("Enter a jersey number:\n"))
    my_dict.pop(jersey_remove)
  elif option == "u":
    jersey_update = int(input("Enter a jersey number:\n"))
    rate_update = int(input("Enter a new rating for player:\n"))
    my_dict[jersey_update] = rate_update
  elif option == "r":
    rate_above = int(input("Enter a rating:\n"))
    print()
    print("ABOVE %d" % rate_above)
    for jersey, rate in my_dict.items():
      if rate > rate_above:
        print("Jersey number: %d, Rating: %d" % (jersey, rate))
      if rate <= rate_above:
        continue