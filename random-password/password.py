import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"
numbers = "0123456789"
symbols = ".,<>"

all = lower + upper + numbers + symbols

question = int(input("Length: "))
length = question

password = " ".join(random.sample(all, length))
print(password)