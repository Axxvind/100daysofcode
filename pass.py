import string
import random
a=int(input("Enter the no.: "))
l='!@#$%^&*~'
fin = ""
for i in range(0,a):
    ran=random.choice(string.ascii_letters+string.digits+l)
    fin +=ran
print("Your password is: ",fin)    