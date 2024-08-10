num1 : int = int(input("Enter the first number:"))
num2 : int = int(input("Enter the second number:"))
print("press 1 for addition \npress 2 for subtraction \npress 3 for division \npress 4 for multiplication")
choice = int(input("enter the number between 1-4: "))
if choice == 1:
    print("The addition of given two numbers is:",num1+num2)
elif choice==2 :
    print("The subtraction of given two numbers is:",num1-num2)
elif choice==3 :
    print("The  division of given two numbers is:",num1/num2)
elif choice==4 :
    print("The multiplication of given two numbers is:",num1*num2)
else:
     print("invalid input")