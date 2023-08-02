class Father:
    def __init__(self):
        self.money= 1000
        print("father class constructor")
    def show(self):
        print("money",self.money)

class Son(Father):
    def display(self):
        print("child class method:",self.money)
    def change_amount(self):
        print("changed amount:",self.money+200)

s=Son()
s.money
s.show()
s.display()
s.change_amount()