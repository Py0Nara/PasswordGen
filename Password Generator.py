import random

passlen = int(input("Enter password length : "))

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"

p = "".join(random.sample(s,passlen))

print(p)
