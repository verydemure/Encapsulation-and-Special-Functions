class point:


    def __init__(self,x,y):
        self.x = x
        self.y = y


    def __str__(self):
        return f"({self.x},{self.y})"
    

p1 = point(2,3)
p2 = point(87,45)

print(p1)
print(p2)