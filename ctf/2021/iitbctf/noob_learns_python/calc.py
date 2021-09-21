#!/usr/bin/env python2.7
#Maybe my First Program here#
try:
    print("***********Welcome to my first calculator************")
    print("You can +, -, * and / some numbers")

    print("")

    first = int(input("Enter First number: "))
    second = int(input("Enter Second number: "))

    operation = str(raw_input("Operations (+, -, *, /): "))

    if first != 1 or second != 1:
        print("")
        print("Really Sorry, but my calculator supports operations only on number 1")

    if first == 1 and second == 1 and operation == "+":
        print("1+1 = 2")
    if first == 1 and second == 1 and operation == "-":
        print("1-1 = 0")
    if first == 1 and second == 1 and operation == "*":
        print("1*1 = 1")
    if first == 1 and second == 1 and operation == "/":
        print("1/1 = 1")
    else:
        print(first + second)
except ValueError:
    pass
    
# int('0x'+''.join([hex(ord(i))[2:] for i in open('flag.txt','rb').read().strip()]),16)