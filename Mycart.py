"""
Author: Karishma Shinde
Title: This code is for View the products,Adding the products and Billing
Date Created: 26-11-2020
"""

lst_category=[]
lst_items=[]   
category={'Mens Clothing':[{'Shirts':{'color':['Red','Black'],'size':['S','M','L'],'price':[5555,990,1000]}},],
          'Ladies Clothing':[{'Tops':{'color':['Red','Black'],'size':['S','M','L'],'price':[9999,3333,1000]}},],
          'Kids Clothing':[{'Sweater':{'color':['Red','Black'],'size':['S','M','L'],'price':[999,4444,1000]}},]}

'''To Display Avalilable Category'''

show_category = input("You want to see available Category? [y/n] : ")
if show_category =='y':
    for key, value in category.items() :
        lst_category.append(key)
    print("These are available Categories  : {}".format(list(enumerate(lst_category))))
    print()
else:
    print("Please enter y to see Categories of product")
    exit()
    
size=[]
cart_items = []  
cost_items = []   
def details():
    
    '''To Display Avalilable Products'''   
    choice = int(input("Enter the Category id to get more product :"))

    if choice < len(lst_category):
        product_length=len(category[lst_category[choice]])

        for length in range(product_length):   
            product=category[lst_category[choice]][length]

            for key, value in product.items() :
                lst_items.append(key)
        print("These are available Products : {}".format(list(enumerate(lst_items))))
        print()
        
        '''To Display Avalilable Product DEtails'''
        
        details = int(input("Enter the Product id to get more product details :"))
        if details<= len(lst_items):    
            product_details=category[lst_category[choice]][details]
            print(product_details)
        else:
            print("Please enter correct Product id") 
            exit()
details ()

def checkout():
    while 1:
        print()
        cart = input("You want to add product in cart[y/n] :")
        
        if cart == 'y':
            order = input("Please select the product want to add in cart : ")
            cart_items.append(order)
            product_size =input("Please select the size of product(Enter 0 for S,1 for M,2 for L) :")
            size.append(product_size)
            x= zip(cart_items,size)
            cart_products=(list(x))
            print()
            print("you have {} products in yor cart {}".format(len(cart_products),cart_products))
            
            checkout = input("You want to checkout?[y/n] : ")
            if checkout == 'y':
                for x in range(len(cart_products)):
                    bill_list = (cart_products[x])
                    if bill_list[0] == 'Shirts':
                        cost = (category.get('Mens Clothing',{})[0].get(bill_list[0]).get('price')[int(bill_list[1])])
                        cost_items.append(cost)
                    elif bill_list[0] == 'Tops':
                        cost = (category.get('Ladies Clothing',{})[0].get(bill_list[0]).get('price')[int(bill_list[1])])
                        cost_items.append(cost)
                    elif bill_list[0] == 'Sweater':
                        cost = (category.get('Kids Clothing',{})[0].get(bill_list[0]).get('price')[int(bill_list[1])])
                        cost_items.append(cost)
                print()       
                amt = sum(cost_items)
                # checking conditions and calculating discount
                if(amt>0):
                    if amt >= 10000:
                        disc = 500
                    else:
                        disc=0
                        
                    print("Actual Amount : ",amt)
                    print("Discount      : ",disc)
                    print("Final Amount  : ",amt-disc)
                    exit()
                else:
                    print("Invalid Amount")
                    exit()
                    
checkout()

