class Product:
    tab='Apple'
    def display(self):
        print("mon")
    @classmethod
    def show_details(cls,p):
        price=p
        cls.tab="doc"
        print("class variable:",cls.tab,p)
prod=Product()
print(prod.tab)
prod.show_details(500)
# prod.tab="samsung"
# print(prod.tab)
#
# print(Product.tab)