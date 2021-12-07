products = []
while True:  #用while 因為不確定次數
    name = input('請輸入商品名稱:')
    if name == 'q':
    	break
    price = input('請輸入商品價格:')	
    #p = []
    #p.append(name)
    #p.append(price)
    #p = [name, price]
    products.append([name, price])
print(products)

#products[0][0]