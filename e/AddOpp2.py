class One:
    
    def __init__(self, a, b):
        self.a = a;
        self.b = b;
        
    def __add__(self, other):
        c = Two((self.a + self.b) + (other.a + other.b))
        return c

class Two:
    
    def __init__(self, a):
        self.f = a;


a = One(1, 2)
b = One(4, 3)

d = a + b

print(d.f)
