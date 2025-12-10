import json
import os
from datetime import datetime

class TodoList:
	def __init__(self, filename='tasks.txt'):
		self.filename = filename  # имя файла для хранения задач
		self.tasks = self.load_tasks()  # загружаем задачи при создании объекта

	def load_tasks(self):
		if os.path.exists(self.filename):  # проверяем, существует ли файл
			with open(self.filename, 'r') as f:  # открываем файл для чтения
				try:
					return json.load(f)  # загружаем данные из JSON файла
				except json.JSONDecodeError:  # если файл поврежден или пуст
					return []  # возвращаем пустой список
		return []  # если файла нет - пустой список
