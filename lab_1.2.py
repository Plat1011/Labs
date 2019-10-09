# -*- coding: utf8 -*-
import os

def vivod(mas):
	print("Массив: ")
	for row in mas:
		for elem in row:
			print(elem, end=' ')
		print()
	
def mx(mas):
	maximum=mas[0][0]
	jmax, imax = 1, 1
	b=list()
	i_list=list()
	i, j = 0, 0
	for row in mas:
		i+=1
		j=0
		for elem in row:
			j+=1
			if maximum<elem:
				
				maximum = elem
				
				imax=i
				jmax=j
			 
	print("Максимум: {0}, индекс максимума: {1}, {2}".format(maximum, imax, jmax))


def mn(mas):
	minimum=mas[0][0]
	jmax, imax = 1, 1
	b=list()
	i_list=list()
	i, j = 0, 0
	for row in mas:
		i+=1
		j=0
		for elem in row:
			j+=1
			if minimum>elem:
				minimum = elem
				imax=i
				jmax=j
			 
	print("Минимум: {0}, индекс минимума: {1}, {2}".format(minimum, imax, jmax))

def vvod(n, m):
	
	mas = [[0] * m for i in range(n)]
	for i in range(n):
		for j in range(m):
			mas[i][j]=int(input("Введите элемент из строки №{0} и стобца №{1}: ".format(i,j)))
	return mas

def proizved(mas_1, mas_2, n, m):
	for i in range(n):
		for j in range(m):
			mas_3[i][j]=mas_1[i][j]*mas_2[i][j]
	return mas_3
	
def summa(mas_1, mas_2, n, m):
	for i in range(n):
		for j in range(m):
			mas_3[i][j]=mas_1[i][j]+mas_2[i][j]
	return mas_3
	
def raznost(mas_1, mas_2, n, m):
	mas_3 = [[0] * m for i in range(n)]
	for i in range(n):
		for j in range(m):
			mas_3[i][j]=mas_1[i][j]-mas_2[i][j]
			
	return mas_3

def vvod_file(mas, n, m, i):
	with open('file{}.txt'.format(i)) as f:
		for row in f:
			mas.append([int(i) for i in row.split()])
	n=len(mas)
	m=len(mas[0])
	return n, m
			
while True:
	hol=input("Введите способ ввода матриц:\n \t 1-через файл \n\t 2-с консоли\n")
	if hol=="1":
		n1, m1=0, 0
		n2, m2=0, 0
	
		mas_1=list()
		n1, m1 =vvod_file(mas_1, n1, m1, 1)
		mas_2=list()
		n2, m2 =vvod_file(mas_2, n2, m2, 2)
		if n2==n1 and m1==m2:
			n=n1
			m=m1
			ewtfgerg=input("Успешный ввод, нажмите enter")
			break
		else:
			print("Ошибка:длины строк и столбцов не совпадают")
	elif hol=="2":
		
		n=int(input("Введите количество строк в массивах: "))
		m=int(input("Введите количество стобцов в массивах"))
		
		mas_1=vvod(n, m)
		mas_2=vvod(n, m)
		break

clear = lambda: os.system('cls')
l=0
while True:
	clear()
	d=input("\nВведите действие:\n \t1-вывод элементов массива №1 \n \t2-вывод элементов массива №2 \n \t3-найти максимум элементов массива №1 и вывести его\n \t4-найти максимум элементов массива №2 и вывести его\n \t5-найти минимум элементов массива №1 и вывести его\n \t6-найти минимум элементов массива №2 и вывести его\n \t7-Найти произведение двух массивов\n \t8-Найти сумму двух массивов\n \t9-Найти разность двух массивов\n \tЛюбая другая клавиша-выход из программы\n")
	if d=="1":
		clear()
		vivod(mas_1)
		tempcl=input("Нажмите клавищи space+enter для выхода из программы, или enter для продолжения")
		if tempcl==" ":
			break	
	elif d=="2":
		clear()
		vivod(mas_2)
		tempcl=input("Нажмите клавищи space+enter для выхода из программы, или enter для продолжения")
		if tempcl==" ":
			break	
	elif d=="3":
		clear()
		mx(mas_1)
		tempcl=input("Нажмите клавищи space+enter для выхода из программы, или enter для продолжения")
		if tempcl==" ":
			break	
	elif d=="4":
		clear()
		mx(mas_2)
		tempcl=input("Нажмите клавищи space+enter для выхода из программы, или enter для продолжения")
		if tempcl==" ":
			break	
	elif d=="5":
		clear()
		mn(mas_1)
		tempcl=input("Нажмите клавищи space+enter для выхода из программы, или enter для продолжения")
		if tempcl==" ":
			break	
	elif d=="6":
		clear()
		mn(mas_2)
		tempcl=input("Нажмите клавищи space+enter для выхода из программы, или enter для продолжения")
		if tempcl==" ":
			break	
	elif d=="7":
		mas_3 = [[0] * m for i in range(n)]
		mas_3=proizved(mas_1, mas_2, n, m)
		clear()	
		vivod(mas_3)
		tempcl=input("Нажмите клавищи space+enter для выхода из программы, или enter для продолжения")
		if tempcl==" ":
			break	
	elif d=="8":
		mas_3 = [[0] * m for i in range(n)]
		mas_3=summa(mas_1, mas_2, n, m)
		clear()	
		vivod(mas_3)
		tempcl=input("Нажмите клавищи space+enter для выхода из программы, или enter для продолжения")
		if tempcl==" ":
			break
	elif d=="9":
		mas_3 = [[0] * m for i in range(n)]
		mas_3=raznost(mas_1, mas_2, n, m)
		clear()
		vivod(mas_3)
		tempcl=input("Нажмите клавищи space+enter для выхода из программы, или enter для продолжения")
		if tempcl==" ":
			break		
	else:
		break




	
