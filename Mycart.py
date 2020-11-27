"""
Author: Karishma Shinde
Title: This code is for View the products,Adding the products and Billing
Date Created: 27-11-2020
"""

import mysql.connector

con = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database = "MyCart"
)

db_cursor = con.cursor() 

'''Steps to Create Database and Table we required'''

# db_cursor.execute("CREATE DATABASE MyCart")
# print(db_cursor)

# db_cursor.execute('SHOW DATABASES')
# print(db_cursor)
# for db in db_cursor:
#     print(db)
    
# db_cursor.execute('SHOW TABLES')
# print(db_cursor)
# for db in db_cursor:
#     print(db)


# db_cursor.execute("CREATE TABLE bill_script (billid INT AUTO_INCREMENT PRIMARY KEY ,product_count INT(5),actual_amt INT(5),discount INT(5),final_amt INT(5))")
# print(db_cursor)

#db_cursor.execute("CREATE TABLE  product ( productid INT AUTO_INCREMENT PRIMARY KEY,categoryid INT(5), productName VARCHAR(255), productPrice INT(5),FOREIGN KEY(categoryid) REFERENCES category (categoryid))")

'''Operations to perform by Admin side'''

print("---------------------ADMIN PART------------------------")

add_category = input("you want to add category? [y/n] : ")
print()
if add_category == 'y' or add_category =='Y': 
    name = input("Enter the categoryName:")
    print()    
    insert_query = "INSERT INTO category (categoryName) VALUES (%s)"
    db_cursor.execute(insert_query,(name,))
    print("Your category {} is sucessfully added".format(name))
con.commit()   

def showCategory():
    db_cursor.execute("SELECT * FROM category")
    category = db_cursor.fetchall()
    print("These are available Categories with (categoryid,categoryName)  :\n{}".format(category))
    print()

add_product = input("you want to add product? [y/n] : ")
print()
if add_product == 'y' or add_product =='Y': 
    showCategory()
    categoryid = int(input("Enter the categoryid:")) 
    productName = input("Enter the productName:")
    productPrice = int(input("Enter the productPrice:"))
    print() 
    insert_query = 'INSERT INTO product (categoryid,productName,productPrice) VALUES (%s,%s,%s)'
    db_cursor.execute(insert_query,(categoryid,productName,productPrice))
    print("Your product {} is sucessfully added".format(productName))
con.commit()  

show_bill = input("Do you want to see User bills? [y/n] : ")
print()
if show_bill == 'y' or show_bill =='Y':    
    db_cursor.execute("SELECT * FROM bill_script")
    bills = db_cursor.fetchall()
    print("[(bill_id, product_count, actual_amt, dis, final_amt)]")
    print(bills)
    print()
    
elif show_bill == 'n' or show_bill =='N': 
    pass

'''Operations to perform by User side'''

print("---------------------User PART------------------------")

show_category = input("you want to see list of category? [y/n] : ")
print()
if show_category == 'y' or show_category =='Y':
    showCategory()
elif show_category == 'n' or show_category =='N': 
    pass

show_product = input("Do you want to see list of product? [y/n] : ")
print()
if show_product == 'y' or show_product =='Y':    
    choice = int(input("Enter the category id to get products:"))    
    db_cursor.execute("SELECT productid,productName FROM product WHERE categoryid={}".format(choice))
    product = db_cursor.fetchall()
    print("These are available Products with (productid,productName) :\n{}".format(product))
    print()
elif show_product == 'n' or show_product =='N': 
    pass
    
show_productDetails = input(" Do you want to see details of product? [y/n] : ")
print()
if show_productDetails == 'y' or show_productDetails =='Y':    
    choice = int(input("Enter the product id to get details:")) 
    print()
    db_cursor.execute("SELECT productid,productName,productPrice FROM product WHERE productid={}".format(choice))
    product = db_cursor.fetchall()
    print("These are  Products details with (productid,productName,productPrice) :\n{}".format(product))
    print()
    
    
product_list = []
cart_items=[]
price = []
while 1:
    checkout = input("Do you want to add product in shopping cart? [y/n] : ")
    print()
    if checkout == 'y' or checkout =='Y':    
        order = input("Enter the product you want to add in cart:")
        cart_items.append(order) 
        print("you have {} products in yor cart {}".format(len(cart_items),cart_items))
        print()

        
    elif checkout == 'n' or checkout =='N':
        bill = input("You want to checkout?[y/n] : ")
        if bill == 'y' or bill =='Y':
            remove_product = input(" Do you want to remove product from cart? [y/n] : ")
            print()
            if remove_product == 'y' or remove_product =='Y': 
                print("Enter the product you want to remove from cart:")
                removeit = input()
                cart_items.remove(removeit)
                print()
            elif remove_product == 'n' or remove_product =='N': 
                pass
            
            for items in cart_items:
                sql = "SELECT productName,productPrice FROM product WHERE productName = %s"
                adr = (items, )
                db_cursor.execute(sql,adr)
                product = db_cursor.fetchall()
                product_list.append(product)                
                
            print('Products in cart with (productName,productPrice) :')
            for x in product_list:
                print(x)
                
            for y in product_list:
                for i in y:
                    price.append(i[1])
            amt = sum(price)
            if(amt>0):
                if amt >= 10000:
                    disc = 500
                else:
                    disc=0
                print()  
                print() 
                print("Actual Amount : ",amt)
                print("Discount      : ",disc)
                print("Final Amount  : ",amt-disc)
                
                product_count = len(cart_items)
                insert_query = 'INSERT INTO bill_script (product_count,actual_amt,discount,final_amt) VALUES (%s,%s,%s,%s)'
                db_cursor.execute(insert_query,(product_count,amt,disc,amt-disc))
                con.commit() 
                print("Thank You,Keep Shopping!!!!")
                exit()
            else:
                print("Invalid Amount")
                exit()
        elif bill == 'n' or bill =='N':
            print("Thank You for visiting our website!!!!")
            exit()
    else:
        print("Invalid answer")
con.commit()   
db_cursor.close()

