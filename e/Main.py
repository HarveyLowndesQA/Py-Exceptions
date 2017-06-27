#while True:
#    try:
#        x = int(input("Enter first number: "))
#        y = int(input("Enter second number: "))
#        print(x/y)
#        break
#    except (ValueError, ZeroDivisionError):
#        print("error")
#    print("got here")

#class B(Exception):
#    pass

#class C(B):
#    pass

#class D(C):
#    pass

#for cls in [D, C, B]:
#    try:
#        raise cls()
#    except D:
#        print("D")
#    except C:
#        print("C")
#    except B:
#        print("B")

#while True:
#    try:
#        x = int(input("Enter first number: "))
#        y = int(input("Enter second number: "))
#        print(x/y)
#        break
#    except (ValueError, ZeroDivisionError):
#        print("error")
#    finally:
#        print("got here")
while True:
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(x/y)
        break
    except ValueError, (Argument):
        print("error")
    except Exception:
        print("error")
    print("got here")