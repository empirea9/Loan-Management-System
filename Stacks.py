L = [("Laptop", 90000), ("Mobile", 30000), ("Pen", 50), ("Headphones", 1500)]  
product = []  
def Push_element(L):  
	for i in L: if i[1] > 50:  
	product.append(i)  
	print(product)  
def Pop_element(product):  
	while product:  
		print(product.pop())  
	else: 
		print("Stack Emply")