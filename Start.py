from product_crud_ops.ProductInfo import Product
from product_crud_ops.ProductService import ProductService

if __name__ == '__main__':
    p1 = Product(pid=102, pnm="Mobile", pprice=542.3, pcat="A", pven="AMZ", pqty=10)
    service = ProductService()

    #print(UPDATE_PRODUCT_QUERY)
    #service.create_product_table()
    #service.insert_product(p1)
    service.get_all_products()
    #service.update_product(p1)
