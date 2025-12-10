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
  

	def save_tasks(self):
		with open(self.filename, 'w') as f:   # открываем файл для записи ('w')
			json.dump(self.tasks, f, indent=2)  # сохраняем с отступами для читаемости
		

	def add_ask(self, title):
		task = {
			'id': len(self.tasks) + 1,  # уникальный ID = текущее кол-во задач + 1
			'title': title,  # уникальный ID = текущее кол-во задач + 1
			'completed': False,  # статус выполнения
			'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  # текущее время
					# %Y - год (4 цифры) - %Y - year (4 digits)
					# %m - месяц (01-12) - %m - month (01-12)
					# %H - час (00-23) - %H - hour (00-23)
					# %M - минуты (00-59) - %M - minutes (00-59)
					# %S - секунды (00-59) - %S - seconds (00-59)

		self.tasks.append(task)  # добавляем задачу в список
		self.save_taks()  # сохраняем изменения в файл
		print(f"Задача добавлена (ID: {task['id']})")


	def show_tasks(self):
		if not self.tasks:  # проверка на пустой список
			print("Список дел пуст!")
			return  # выход из метода
		
		for task in self.tasks:  # перебираем все задачи
			status = "✓" if task['completed'] else "✗"  # галочка или крестик
			print(f"{task['id']}. [{status}] {task['title']} - {task['created_at']}")

	def complete_task(self, task_id):
		for task in self.tasks:  # ищем задачу по ID
			if task['id'] == task_id:  # если нашли
				task['completed'] = True  # меняем статус
				self.save_tasks()  # сохраняем
				print(f"Задача {task_id} отмечена как выполненная")
				return  # выходим из метода
		print("Задача не найдена")  # если не нашли