def vvod(mas):
	n=int(input("Введите количество строк: "))
	for i in range(n):
		mas.append([])
		m=int(input("Введите количество чисел в {} строке".format(i+1)))
		for j in range(m):
			mas[i].append(int(input("Введите элемент {} {}".format(i+1, j+1))))
			
def vvod_file(mas, n, m, i):
	with open('file{}.txt'.format(i)) as f:
		for row in f:
			mas.append([int(i) for i in row.split()])
