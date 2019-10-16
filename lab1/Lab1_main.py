import os

clear = lambda: os.system('cls')	

fl=True
while fl:
	clear()
	temp=input('Введите действие:\n\t1-Запуск подпункта один лабораторной работы номер один\n\t2-Запуск подпункта два лабораторной работы номер один\n\t3-Запуск подпункта два лабораторной работы номер один\n\t4-Выход из программы\n')
	if temp=='1':
		clear()
		os.system("lab1.1.py")
	elif temp=='2':
		clear()
		os.system("lab1.2.py")
	elif temp=='3':
		clear()
		os.system("lab1.3.py")
	elif temp=='4':
		fl=False
	else:
		efw2ig=input('Ошибка нажмите enter и повторите ввод')
		clear()
		
		
			
