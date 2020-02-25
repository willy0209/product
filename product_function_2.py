#先檢查檢查檔案在不在
#function的中心思想，只做一件事
import os #作業系統(operation system)

#讀取檔案
def read_file(filename):
	products = [] #不管有沒有找到檔案，都要產生空清單
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品名稱,商品價格' in line:
				continue # 遇到商品跟價格就跳過那一行
			name, price = line.strip().split(',') #strip是去除\n的功能
			products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
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
	return products

#印出所有購買紀錄
def print_products(products):
	for p in products: #把一個一個清單的東西拿出來
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open (filename, 'w', encoding = 'utf-8') as f:
		f.write('商品名稱,商品價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') #\n 換行符號

def  main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檢查檔案在不在
		print('yeah!找到檔案')
		products = read_file(filename)
	else:
		print('no!找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()