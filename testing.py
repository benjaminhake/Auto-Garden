class A:
    def __init__(self) -> None:
        self.a = 1
    
    def mod(self):
        self.a += 1

class B:
    def __init__(self, ca):
        self.a = ca
    
    def mod(self):
        self.a.a += 1

a = A()
b = B(a)
b.mod()
print(a.a)
a.mod()
print(b.a.a)