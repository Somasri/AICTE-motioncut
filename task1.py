import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()."
numbers = "0123456789"

string = lower+upper+numbers+symbols

length = int(input("Enter the length of password you require:"))

no_of_pwds = int(input("How many password do you want me to suggest?"))

for i in range(no_of_pwds):
    password = "".join(random.sample(string,length))
    print("new password:"+password)
