import pickle
import os

array = []
barray = []
errors = (ValueError,KeyboardInterrupt)
os.system('color f0')


def cls():
	os.system('cls')


class Data:
	print()

class members:

	def __init__(self,name='',mesto ='',zarplata='',adress='',phone='',statys=''):
		self.name = name
		self.mesto = mesto
		self.zarplata = zarplata
		self.adress = adress
		self.phone = phone
		self.statys = statys

	#Getters

	def getName(self):
		return self.name

	#Setters

	def setName(self, name): self.name = name
	def setMesto(self, mesto): self.mesto = mesto
	def setZarplata(self, zarplata): self.zarplata = zarplata
	def setAdress(self, adress): self.adress = adress
	def setPhone(self, phone): self.phone = phone
	def setStatys(self, statys): self.statys = statys

	def printInfo(self):
		cls()
		print('ФИО сотрудника: ', self.name)
		print('Должность сотрудника: ', self.mesto)
		print('Зарплата сотрудника: ', self.zarplata)
		print('Адрес сотрудника: ', self.adress)
		print('Телефон сотрудника: ', self.phone)
		print('Статус сотрудника: ', self.statys)
		input('')

def creatContact():
	cls()
	contact = members()
	contact.setName(input('Введите ФИО сотрудника: '))
	contact.setMesto(input('Укажите должность сотрудника: '))
	contact.setZarplata(input('Укажите зарплату сотрудника: '))
	contact.setAdress(input('Укажите адрес сотрудника: '))
	contact.setPhone(input('Укажите телефон сотрудника: '))
	contact.setStatys(input('Укажите статус сотрудника: '))
	array.append(contact)
	saveContact()

def deleteContact():
	cls()
	showName()
	try:
		idContact = int(input('Введите номер сотрудника которого хотите удалить: '))
		print('Соотрудник: ',array[idContact-1].name,':удален.')
		del array[idContact-1]
		saveContact()

		input()
	except IndexError:
		print('\nВы ввели неправильно ФИО сотрудника.')
		input('Enter для продолжения')
	saveContact()


def editContact():
	cls()
	showName()
	try:
		idContact = int(input('Введите номер сотрудника которого хотите редактировать: '))
		if array[idContact - 1]:
			runEdit = True
		else:
			runEdit = False
		while runEdit:
			cls()
			print('Меню редактирования \n')
			print('1) - ФИО\n2) - Должность\n3) - Зарплата\n4) - Адрес\n5) - Телефон\n6) - Статус\n7 - Выйти')
			action = int(input(' --> '))
			if action == 1:
				array[idContact-1].setName(input('Новое ФИО: '))
			elif action == 2:
				array[idContact-1].setMesto(input('Новая должность: '))
			elif action == 3:
				array[idContact-1].setZarplata(input('Новая зарплата: '))
			elif action == 4:
				array[idContact-1].setAdress(input('Новый адрес: '))
			elif action == 5:
				array[idContact-1].setPhone(input('Новый телефон: '))
			elif action == 6:
				array[idContact-1].setStatys(input('Новый статус: '))
			elif action == 7:
				runEdit = False
	except IndexError:
		print('\nВы ввели неправилиное ФИО сотрудника.')
		input('Enter для продолжения: ')

	saveContact()


def peredVyvol():
	cls()
	showName()
	idContact = int(input('Введите номер сотрудника которого хотите удалить: '))

	with open('RvM.dat', 'rb') as RvMfile, open('DelRvM.dat', 'ab') as DelRvMfile:
		for idContact in RvMfile:
			DelRvMfile.write(idContact)
			initSaveContact()
			delrob()

def peredVrob():
	cls()

	idContact = int(input('Введите номер сотрудника которого хотите удалить: '))

	with open('DelRvM.dat', 'rb') as DelRvMfile, open('RvM.dat', 'ab') as RvMfile:
		for idContact in DelRvMfile:
			RvMfile.write(idContact)
			prosdelrob()
			saveContact()

def showContact():
	showName()
	try:
		idContact = int(input('Введите 0 для выхода: '))
		if idContact == 0:
			pass
		else:
			array[idContact - 1].printInfo()
	except IndexError:
		print('\nВы ввели неправильное ФИО сотрудника')
		input('Enter для продолжения: ')

def saveContact():
	global array

	with open('RvM.dat','wb') as f:
		pickle.dump(array,f)

def delrob():
	global barray

	with open('DelRvM.dat', 'wb') as f:
		pickle.dump(barray, f)

def prosdelrob():
	global barray

	try:
		with open('DelRvm.dat', 'rb') as f:
			barray = pickle.load(f)
	except:
		barray = []


def initSaveContact():
	global array

	try:
		with open('RvM.dat','rb') as f:
			array = pickle.load(f)
	except:
		array = []

def showName():
	cls()
	j = 1
	for i in array:
		print(str(j),')',i.getName())
		j+=1

def menuContact():
	if len(array) > 0:
		print('Всего сотрудников: ', len(array),'\n')
	else:
		print('Сотрудников нету!\n')

	if len(array) != 0:
		if len(array) == 1:
			showMenuName()
			print('\n\n')
		else:
			showMenuName()
			print('\n')

def showMenuName():
	if len(array) <= 4:
		for i in array:
			print(i.getName())
	else:
		i = 0
		while i <= 3:
			print(array[i].getName())
			i+=1

while True:
	cls()
	initSaveContact()
	menuContact()
	try:
		action = int(input('1 - Добавить нового сотрудника.\n2 - Показать весь список сотрудников.\n3 - Редактировать данные сотрудника.'
'\n4 - Удалить сотрудника.\n5 - Перенести сотрудника в раздел увольненных.\n6 - Перенести сотрудника в раздел робочих.\n------------------>  '))
		if action == 1:
			creatContact()
		elif action == 2:
			showContact()
		elif action == 3:
			editContact()
		elif action == 4:
			deleteContact()
		elif action == 5:
			peredVyvol()
		elif action == 6:
			peredVrob()
		elif action == 9:
			exit()
	except errors:
		print('\nВы ввели неверное значение')
		input('Enter для продолжения: ')