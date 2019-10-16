# -*- coding: utf8 -*-
import sys  
import os
import pandas as pd

clear = lambda: os.system('cls')	

def maxdf():
	print(max(float(i.replace(',', '.')) for i in df.Средний_балл))

def mindf():
	print(min(float(i.replace(',', '.')) for i in df.Средний_балл))

def updatedf():
	print(df)
	number=int(input('Введите номер записи:'))
	pole=input('Введите название поля: ')
	znach=input('Введите значение ячейки(придерживайтесь формы):')
	df.at[(number-1), pole]=znach
	

def sumdf():
	print(sum(float(i.replace(',', '.')) for i in df.Средний_балл))

def sredn():
	print(sum(float(i.replace(',', '.')) for i in df.Средний_балл)/len(df.Средний_балл))

def savedf():
	moddf.to_csv(r'students.csv', encoding = "utf-8", index=False, sep=';')

def searchdf_name():
	clear()
	temp=input('Введите ФИО человека, которого вы пытаетесь найти: ')

	df_empty=df[df.ФИО_студента=='{}'.format(temp)]
	if df_empty.empty:
		rgwe=input('Такого человека в БД нет. Нажмите enter для продолжения...')
		clear()
	else:
		print(df_empty)

def searchdf_birthdate():
	temp=input('Введите дату рождения в формате гггг-мм-дд человека, которого вы пытаетесь найти: ')

	df_empty=df[df.Дата_рождения=='{}'.format(temp)]
	if df_empty.empty:
		rgwe=input('Человека с такой датой рождения в БД нет. Нажмите enter для продолжения...')
		clear()
	else:
		print(df_empty)

def tempcl():
	tempcl1=input("Нажмите клавищи space+enter для выхода из программы, или enter для продолжения")
	if tempcl1==" ":
		return False
	else:
		return True

def sort_by_date():
	clear()
	temp=input('Введите тип сортировки(1-обратная 2-прямая): ')
	while True:
		if temp=='1':
			df.sort_values(by=['Дата_рождения'], inplace=True, ascending=False)
			break
		elif temp=='2':
			df.sort_values(by=['Дата_рождения'], inplace=True)
			break
		else:
			gerj=input('Неверное значение. Нажмите enter для продолжения...')
			clear()
	temp=input('Вывести отсортированную БД? 1-Да: ')
	clear()
	if temp=='1':
		print(df)
		rg=input('Нажмите enter для продолжения...')
		clear()

def sort_by_name():
	clear()
	temp=input('Введите тип сортировки(1-обратная 2-прямая): ')
	while True:
		if temp=='1':
			df.sort_values(by=['ФИО_студента'], inplace=True, ascending=False)
			break
		elif temp=='2':
			df.sort_values(by=['ФИО_студента'], inplace=True)
			break
		else:
			gerj=input('Неверное значение. Нажмите enter для продолжения...')
			clear()
	temp=input('Вывести отсортированную БД? 1-Да: ')
	clear()
	if temp=='1':
		print(df)
		rg=input('Нажмите enter для продолжения...')
		clear()

def addnewrow():
	clear()
	number=len(df['Номер'])+1
	FIO=input('Введите ФИО студента: ')
	birth=input('Введите дату рождения в формате гггг-мм-дд: ')
	institut=input('Введите интитут: ')
	grupa=input('Введите группу: ')
	kurs=input('Введите курс: ')
	sr=input('Введите средний балл: ')
	moddf=df.append({'Номер': number , 'ФИО_студентв': FIO , 'Дата_рождения':birth , 'Институт':institut , 'Группа':grupa , 'Курс':kurs , 'Средний_балл':sr}, ignore_index=True)
		

	
	

df = pd.read_csv('students.csv', sep=(';'), encoding = "utf-8")
print(df)
rweg=input('Нажмите enter для продолжения...')
fl=True
while fl:
	clear()
	temp=input('Введите действие:\n\t1-Добавление записи в БД\n\t2-Изменение записи в БД\n\t3-Удаление записи в БД\n\t4-Сортировка по ФИО\n\t5-Сортировка по дате рождения\n\t6-Поиск элемента по имени\n\t7-Поиск элемента по дате рождения\n\t8-Минимум по среднему баллу\n\t9-Максимум по среднему баллу\n\t10-Среднее значение среднего балла\n\t11-Сумма средних баллов\n\t12-Вывести БД\n')
	if temp=='1':
		number=len(df['Номер'])+1
		FIO=input('Введите ФИО студента: ')
		birth=input('Введите дату рождения в формате гггг-мм-дд: ')
		institut=input('Введите интитут: ')
		grupa=input('Введите группу: ')
		kurs=input('Введите курс: ')
		sr=input('Введите средний балл: ')
		moddf=df.append({'Номер': number , 'ФИО_студента': FIO , 'Дата_рождения':birth , 'Институт':institut , 'Группа':grupa , 'Курс':kurs , 'Средний_балл':sr}, ignore_index=True)
		clear()
		print(moddf)
		while True:
			sa_ve=input('1-Чтобы сохранить изменение\n2-Не сохранять\n')
			if sa_ve=='1':
				savedf()
				df=moddf.copy()

				break
			elif sa_ve=='2':
				break
		fl=tempcl()
		
		
		
	elif temp=='2':
		updatedf()
		clear()
		print(df)
		fl=tempcl()
	elif temp=='3':
		clear()
		print(df)
		number=int(input('Введите номер строки которую вы хотите удалить'))
		moddf=df.drop(number-1)
		print(moddf)
		while True:
			sa_ve=input('1-Чтобы сохранить изменение\n2-Не сохранят\n')
			if sa_ve=='1':
				savedf()
				df=moddf.copy()

				break
			elif sa_ve=='2':
				break
		fl=tempcl()
	elif temp=='4':
		sort_by_name()
		fl=tempcl()
	elif temp=='5':
		sort_by_date()
		fl=tempcl()
	elif temp=='6':
		searchdf_name()
		fl=tempcl()
	elif temp=='7':
		searchdf_birthdate()
		fl=tempcl()
	elif temp=='8':
		mindf()
		fl=tempcl()
	elif temp=='9':
		maxdf()
		fl=tempcl()
	elif temp=='10':
		sredn()
		fl=tempcl()
	elif temp=='11':
		sumdf()
		fl=tempcl()
	elif temp=='12':
		print(df)
		fl=tempcl()

