import numpy as np

#This program is to provide 10% discount on available products.
#In this program we have done broadcasting to calculate discount value product_porices*(discount/100)
#This is an example broadcasting of single element over an array  of length n.
product_prices = np.array([400,240, 315])
dscount=10;

def discountedprice(product_prices, discount):
    d=np.array(discount/100)
    product_discount = product_prices*d
    print(f"Discount amount on respective products are{product_discount}")
    return product_prices-product_discount
    
print(f" Original product prices are {product_prices} , \n respective prices after {dscount}% discount are => ",discountedprice(product_prices,dscount) )



