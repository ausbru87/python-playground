grocery_list = []
grocery_item = ""
while grocery_item != "done":
    grocery_item = input("Please write down an item to add to your grocery list. When you are done writing the list simply type: done \n")
    if grocery_item != "done":
        grocery_list.append(grocery_item)
    else:
        break

print(grocery_list)

# check if you got it all
for item in grocery_list:
    answer = input("Did you get %s \n" % item)
    if answer == "yes":
        grocery_list.remove(item)
    else:
        pass

if grocery_list != []:
    print("Looks like you missed some items:")
    for item in grocery_list:
        print(item)
else:
    print("looks like you got everything, have a safe drive home!")