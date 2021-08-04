from product_crud_ops.ProductInfo import Product
from product_crud_ops.DBConfig import DatabaseUtil

class ProductService:
    conn = None
    def __init__(self):
        ProductService.conn = DatabaseUtil.get_mysql_connection()

    def create_product_table(self):
        CREATE_TABLE_SQL='''CREATE TABLE Product (  
            PID INT NOT NULL,  
            PNAME VARCHAR (20) NOT NULL,  
            PPRICE FLOAT  NOT NULL,  
            PQTY INT  NOT NULL,  
            PVENDOR CHAR (25),  
            PCAT CHAR (25),  
            PRIMARY KEY (PID)  
        )'''
        cursor = ProductService.conn.cursor() # platform-- communication channel
        cursor.execute(CREATE_TABLE_SQL)
        ProductService.conn.commit()

    def insert_product(self,prod):
        print(type(prod))
        if type(prod)==Product:
            if prod.productId>=101:
                if prod.productQuantity>=1:
                    if prod.productPrice>500:
                        if self.get_product(prod.productId):
                            print('Duplicate Product...Cannot insert it again')
                            return
                        PRODUCT_INSERT_SQL = "insert into Product values("
                        PRODUCT_INSERT_SQL += str(prod.productId) + ",'" + prod.productName + "'," + str(
                            prod.productPrice) + "," + str(
                            prod.productQuantity) + ",'" + prod.productVendor + "','" + prod.productCategory + "')"
                        print(PRODUCT_INSERT_SQL)


                        cursor = ProductService.conn.cursor()
                        cursor.execute(PRODUCT_INSERT_SQL)
                        ProductService.conn.commit()
                        print('Product Saved successfully..!')
                    else:
                        print("INvalid Product Price")
                else:
                    print('Invalid Product Qty..!')
            else:
                print('INvalid Product Id')
        else:
            print('Invalid Product..Cannot insert..!')

    def delete_product(self,pid):
        if self.get_product(pid):
            DELETE_PRODUCT_QUERY = "DELETE FROM PRODUCT WHERE PID="+str(pid)
            cursor = ProductService.conn.cursor()
            cursor.execute(DELETE_PRODUCT_QUERY)
            ProductService.conn.commit()
            print("Product Deleted Successfully...!")
        else:
            print("Given Product Not Avaiable so cannot delete")

    def get_product(self,pid):
        if pid>=101:
            FETCH_PRODUCT_QUERY = "SELECT * FROM PRODUCT WHERE PID="+str(pid)
            cursor = ProductService.conn.cursor()
            cursor.execute(FETCH_PRODUCT_QUERY)
            result = cursor.fetchone()
            if result==None:
                print('No record exist')
            else:
                print(result)
                return result
        else:
            print("invalid product id...cannot fetch..")
    def get_all_products(self):
        FETCH_PRODUCTS_QUERY = "SELECT * FROM PRODUCT"
        cursor = ProductService.conn.cursor()
        cursor.execute(FETCH_PRODUCTS_QUERY)
        result = cursor.fetchall()

        if result == None:
            print('No record exist')
        else:
            print(result)
            return result

    def update_product(self,prod):
        if type(prod)==Product:
            if prod.productQuantity >= 1:
                if prod.productPrice > 500:
                    if self.get_product(prod.productId):
                        UPDATE_PRODUCT_QUERY = 'update product set '
                        UPDATE_PRODUCT_QUERY += "pname='" + prod.productName + "',pprice=" + str(
                            prod.productPrice) + ",pcat='" + prod.productCategory + "',pqty=" + str(
                            prod.productQuantity) + ",pvendor='" + prod.productVendor + "'";
                        UPDATE_PRODUCT_QUERY += " WHERE PID=" + str(prod.productId)
                        ProductService.conn.cursor().execute(UPDATE_PRODUCT_QUERY)
                        ProductService.conn.commit()
                        print("product updated successfully....")
                    else:
                        print('Not avbl so cannt update..')
                else:

                    print("invalid price")
            else:
                print("invalid Qty")
        else:
            print('invalid product...!')
