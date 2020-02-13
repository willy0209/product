#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品名稱,商品價格' in line:
			continue # 遇到商品跟價格就跳過那一行
		name, price = line.strip().split(',') #strip是去除\n的功能
		products.append([name, price])
print(products)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	#p = [name, price] #等於下面三行
	#p = []
	#p.append(name)
	#p.append(price)
	products.append([name, price])#等於上面幾行
print(products)

#印出所有購買紀錄
for p in products: #把一個一個清單的東西拿出來
	print(p[0], '的價格是', p[1])

#寫入檔案
with open ('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品名稱,商品價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #\n 換行符號