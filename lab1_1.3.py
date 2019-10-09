# -*- coding: utf8 -*-
import os
import numpy as np


def vvod(mas):
	n=int(input("Введите количество строк: "))
	for i in range(n):
		mas.append([])
		m=int(input("Введите количество чисел в {} строке: ".format(i+1)))
		for j in range(m):
			mas[i].append(int(input("Введите элемент {} {}: ".format(i+1, j+1))))
			
def vvod_file(mas):
	with open('file3.txt') as f:
		for row in f:
			mas.append([int(i) for i in row.split()])

def tempcl():
	tempcl1=input("Нажмите клавищи space+enter для выхода из программы, или enter для продолжения")
	if tempcl1==' ':
		return False
	else:
		return True
			
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

clear = lambda: os.system('cls')

mas = list()
mas_chet = list()
fl=True
while fl:
	temp=input("Введите способ ввода: 1 - файл, 2 - консоль: ")
	if temp=="1":
		vvod_file(mas)
		fl=False
	elif temp=="2":
		vvod(mas)
		fl=False
fl=True
while fl:
	clear()
	d=input("\nВведите действие:\n \t1-вывод элементов массива\n \t2-найти минимум и вывести его\n \t3-найти максимум и вывести его\n \t4-Изменить элемент массива\n \tЛюбая другая клавиша-выход из программы\n")
	if d=="1":
		clear()
		vivod(mas)
		fl=tempcl()
	elif d=="2":
		clear()
		mn(mas)
		fl=tempcl()
	elif d=="3":
		clear()
		mx(mas)
		fl=tempcl()
	elif d=="4":
		fl_loc=True
		clear()
		vivod(mas)
		while fl_loc:
			i_ch=int(input("Введите номер строки для измениения: "))
			if i_ch>(len(mas)+1 or i_ch<=0):
				wrgjo=input("Такой строки не существует, нажмите enter для продолжения")
			else:
				j_ch=int(input("Введите номер элемента в строке {} для измениения: ".format(i_ch)))
				if j_ch>(len(mas[i_ch-1])+1) or j_ch<=0:
					wrgjo=input("Такого элемента не существует, нажмите enter для продолжения")
				else:
					mas[i_ch-1][j_ch-1]=int(input("Текущее значение = {} \n Введите новое: ".format(mas[i_ch-1][j_ch-1])))
					fl_loc=False
					open('file3.txt', 'w').close()
					with open('file3.txt', 'w') as f:
						for row in mas:
							for elem in mas:
								f.write(str(elem)+' ')
							
		fl=tempcl()
					
				
	else:
		fl=false
		







