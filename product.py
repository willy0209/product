products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	#p = [name, price] #等於下面三行
	#p = []
	#p.append(name)
	#p.append(price)
	products.append([name, price])#等於上面幾行
print(products)

for p in products: #把一個一個清單的東西拿出來
	print(p[0], '的價格是', p[1])