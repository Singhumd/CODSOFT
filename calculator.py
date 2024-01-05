#SIMPLE CALCULATOR USINGH PYTHON


Number1 = float(input("\nEnter the first number:"))
Number2 = float(input(" \n Enter the second number:"))

print("\n The Number given by the User is :", (Number1,Number2))

print("\n Press 1 for additon \n Press 2 for substraction \n Press 3 for multiplication \n Press 4 for division" )

choice = int(input("\n Enter your choice fron 1-4 :"))

if choice==1 :
    print("\n The Addition of Given two number is:", Number1+Number2)
elif choice==2 :
    print("\n The Subtraction of Given two number is:", Number1-Number2)
elif choice==3 :
    print("\n The mutliplication  of Given two number is:", Number1*Number2)
elif choice==4 :
     print("\n The Division of Given two number is:", Number1/Number2)
else :
    print("\n Invalid input by the user")