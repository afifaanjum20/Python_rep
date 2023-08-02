class Father:
    def __init__(self):
        print("father class constructor")
    def showF(self):
        print("father class method")
class Son(Father):
    def __init__(self):
        print("son class constructor")
    def showS(self):
        print("son class methods")
class GrandSon(Son):
    def __init__(self):
        super().__init__()
        print("Gson class constructor")
    def showG(self):
        print("gson method")
gson=GrandSon()
gson.showF()
gson.showS()
gson.showG()