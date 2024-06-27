import random

print("WELCOME TO RANDOM PASSWORD GENERATOR!")
randomechars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*_-"
nbrofpwds = int(input("Please enter the no of password to be generated: "))
pwdlen = int(input("please enter length of password"))

print("Here are  your random passwords:")
for x in range(nbrofpwds):
    pwd= " "
    for chars in range(pwdlen):
        pwd = pwd + random.choice(randomechars)
        print(pwd)