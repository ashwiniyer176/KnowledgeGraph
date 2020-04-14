import os
import time
class Operations:
    def add(self):
        a=int(input("Enter number 1:"))
        b=int(input("Enter number 2:"))
        res=a+b
        print(res)

    def subtract(self):
        a=int(input("Enter number 1:"))
        b=int(input("Enter number 2:"))
        res=a-b
        print(res)

    def divide(self):
        a=int(input("Enter number 1:"))
        b=int(input("Enter number 2:"))
        res=a/b
        print(round(res,3))
    def multiply(self):
        a=int(input("Enter number 1:"))
        b=int(input("Enter number 2:"))
        res=a*b
        print(res)

def menu():
    choice=0
    obj1=Operations()
    while choice!=5:
        choice=int(input("1.Add\n,2.subtract\n3.multiply\n4.divide\n5.exit\nChoice:"))
        os.system("cls")
        if choice==1:
            obj1.add()
        elif choice==2:
            obj1.subtract()
        elif choice==3:
            obj1.multiply()
        elif choice==4:
            obj1.divide()
        elif choice==5:
            exit
menu()
