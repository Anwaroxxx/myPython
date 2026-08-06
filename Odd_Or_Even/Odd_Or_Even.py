number = int(input("type a number : "))
if(number % 4 == 0):
    print("thats a number devided by 4")

elif (number % 2 == 0):
    print("thats an even number")

else:
    print("thats an odd number")

check = int(input("type a num to devide ur choosen number with : "))
if (number % check == 0):
    print(str(number) + " is devided by " + str(check))
else:
    print(str(number) + " is not devided by " + str(check))