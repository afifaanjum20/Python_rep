def decor(num):
    def inner():
        b=num()
        sub=b-5
        return sub
    return inner

def dec(num):
    def inner():
        a=num()
        mul=a*2
        return mul
    return inner

@decor
@dec
def num():
    return 10

print(num())
