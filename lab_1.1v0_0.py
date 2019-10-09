def mx(mas):
	a = max(i for i in mas)
	print("\nМаксимум= {0}, индекс маскимума={1}".format(a, mas.index(a)))

def vivod(mas):
	print("\nВведенный массив: \n")
	print(' '.join([str(i) for i in mas]))


def mn(mas):
	a = min(i for i in mas)
	print("\nМинимум= {0}, индекс минимума={1}".format(a, mas.index(a)))
def sortirovka(mas):
	mas.sort()
	print("\nСортированный массив: \n")
	print(' '.join([str(i) for i in mas]))
def rsortirovka(mas):
	mas.sort(reverse=True)
	print("\nСортированный массив: \n")
	print(' '.join([str(i) for i in mas]))
def chetmas(mas, mas_chet):
	if len(mas_chet)==0:
		for i in mas:
			if i%2==0:
				mas_chet.append(i)
	print("\nМассив из четных элементов: \n")
	print(' '.join([str(i) for i in mas_chet]))
	
mas = list()
mas_chet = list()
fl=True
while fl:
	temp=input("Введите способ ввода: 1 - файл, 2 - консоль: ")
	if temp=="1":
		with open('file.txt') as f:
			mas = [int(i) for i in f.read().splitlines()]
		fl=False
	elif temp=="2":
		n = int(input("Введите размер массива: "))
		for i in range(n):
			mas.append(int(input("Введите {} число массива: ".format(i+1))))
		fl=False



while True:
	d=input("\nВведите действие:\n \t1-вывод элементов массива\n \t2-найти минимум и вывести его\n \t3-найти максимум и вывести его\n \t4-сортировка массива\n \t5-обратная сортировка массива\n \t6-новый массив из четных элементов\n \tЛюбая другая клавиша-выход из программы\n")
	if d=="1":
		vivod(mas)
	elif d=="2":
		mn(mas)
	elif d=="3":
		mx(mas)
	elif d=="4":
		sortirovka(mas)
	elif d=="5":
		rsortirovka(mas)
	elif d=="6":
		chetmas(mas, mas_chet)
	else:
		break
		
