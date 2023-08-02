class Cal:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a*b
        else:
            print("pass 2 or more arguments")
        return s
obj=Cal()
print(obj.sum(2,4,2))
print(obj.sum(4,4))