
class Product: #complex structure created by Dev -- datatype
    def __init__(self,pid,pnm,pprice,pcat,pven,pqty):
        self.productId=pid #101
        self.productName=pnm
        self.productPrice=pprice #500
        self.productCategory=pcat
        self.productVendor=pven
        self.productQuantity=pqty #1

    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)


#p1 = Product(pid=101,pnm="Mobile",pprice=23833.3,pcat="A",pven="FLip",pqty=3)
#print(p1)