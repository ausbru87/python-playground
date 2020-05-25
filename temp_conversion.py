def c_to_f(ctemp):
    ftemp = round(ctemp * (9 / 5) + 32, 2)
    response = str(ctemp) + " degrees Celsius is " + str(ftemp) + " degrees Fahrenheit."
    return response

def f_to_c(ftemp):
    ctemp = round((ftemp - 32) * (5 / 9), 2)
    response = str(ftemp) + " degrees Fahrenheit is " + str(ctemp) + " degrees Celsius."
    return response

user_response = input("Hello welcome to the Temperature converter application!\n would you like to continue? 'y' or 'n'\n").lower()
while user_response != "n" and user_response != "y":
    user_response = input("Invalid selection.\n Please type 'y' or 'n'\n").lower()
while user_response != "n":
    start_scale = input("Are you converting from Celsius 'C' or Fahrenheit 'F'? \n please type 'F' or C' or 'done' to stop: ").lower()
    while start_scale != "c" and start_scale != "f":
        start_scale = input("please enter a 'C' or a 'F': ").lower()
    try:
        temp = float(input("Enter the temp in %s: " % start_scale))
    except:
        temp = float(input("please type in a number that you want to convert "))
    if start_scale == "f":
        print(f_to_c(temp))
    else:
        print(c_to_f(temp))
    user_response = input("Would you like to keep converting? 'y' or 'n': ").lower()
    if user_response != "y":
        print("Thank you, goodbye!")
        break