#Password Geneartor Using Python

import string
import random

str1=string.ascii_lowercase
str2=string.ascii_uppercase
str3=string.digits
str4=string.punctuation
str5=string.__annotations__
passlen=int(input("\nEnter the length of Password :"))
P=[]
P.extend(list(str1))
P.extend(list(str2))
P.extend(list(str3))
P.extend(list(str4))
P.extend(list(str5))
print("\nYour Password IS :")
print('\n')
print("".join(random.sample(P,passlen)))