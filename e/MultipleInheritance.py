class class1(object):
    def method1(self):
        print("Class 1 method 1")
    
    def method2(self):
        print("Class 1 method 2")
        
class class2(object):
    def method1(self):
        print("Class 2 method 1")
    
    def method2(self):
        print("Class 2 method 2")

class class3(class2, class1):
    
    def __init__(self):
        super(class2, self).method1() #class 1 method 1
        super().method1()
        
cl = class3()