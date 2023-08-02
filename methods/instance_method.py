class Mobile:
    def __init__(self):
        self.brand="iphone"     #instance variable
    #instance method
    def show(self,p):
        self.price=p
        print("price:",p)
mobj=Mobile()
print(mobj.brand)
mobj.show(900)

