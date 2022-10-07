import pywhatkit

with open("hello.txt", "r", encoding = "utf-8") as b: 
    a = b.read()

pywhatkit.text_to_handwriting(a, "a.png", rgb = [0, 0, 0])