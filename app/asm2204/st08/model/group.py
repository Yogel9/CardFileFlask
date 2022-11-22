

class Group:

	def __init__(self, name, *args):
		self.name = name
		self.person_list = [*args]

	def add_person(self, person):
		self.person_list.append(person)

	def edit_person(self, person_id, person):
		self.person_list[int(person_id)] = person

	def get_person(self, person_id):
		return self.person_list[int(person_id)]

	def del_person(self, person_id):
		self.person_list.pop(int(person_id))

	def display_info(self):
		print("<------------------------------------>")
		if len(self.person_list) == 0:
			print("Список пуст")
		else:
			print("№ Имя|Фамилия|Категория")
			for i, person in enumerate(self.person_list):
				print(i, str(person))
		print("<------------------------------------>\n")

			# if isinstance(person, Reader):
			# 	person.study()
			# elif isinstance(person, Writer):
			# 	person.work()
			# elif isinstance(person, Admin):
			# 	person.do_nothing()
			# else:
			# 	print(person)


