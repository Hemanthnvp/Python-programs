class numbers:
    def __init__(self):
        self.x=100
    def display(self):
        y=40
        print("instance variable",self.x)
        print("normal variable",y)
n=numbers()
n.display()
print("outside the method the value is:",n.x)

