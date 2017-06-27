class One:
    
    def __init__(self, a, b):
        self.a = a;
        self.b = b;
        
    def __add__(self, other):
        c = One((self.a + other.a), (self.b + other.b))
        return c

a = One(1, 2)
b = One(4, 3)
c = One(1, 1)

d = a + b + c

print(d.a)