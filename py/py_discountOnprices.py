#This program is to provide 10% discount on available products.

product_prices =[400,240, 315]
discount=10;

def discountedprice(product_prices, discount):
    discounted_prices=[]
    for n in product_prices:
        product_discount= n*(discount/100)
        discounted_prices.append( (n-product_discount))
    return discounted_prices

print(f" Original product prices are {product_prices} , \n respective prices after {discount}% discount are =>",discountedprice(product_prices, discount) )
        

