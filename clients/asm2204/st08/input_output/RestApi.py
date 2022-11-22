import requests


class RestConsole:
    url = 'http://localhost:5000/'
    # url = 'http://localhost:5000/st2/api/'
    st = False

    def __init__(self):
        self.url = self.get_url()
        self.st = True

    # --- Добавление объектов через консоль ---
    def add_writer(self):
        """Добавить писателя"""
        print("[Писатель]")
        return {"Surname": input("Фамилия>>"),
                "Name": input("Имя>>"),
                "type": "Писатель",
                "Experience": int(input("Опыт>>")), }

    def add_reader(self):
        """Добавить читателя"""
        print("[Читатель]")
        return {"Surname": input("Фамилия>>"),
                "Name": input("Имя>>"),
                "type": "Читатель",
                "Age": int(input("Возраст>>")),
                }

    class_type = [
        ["Писатель", add_writer, "Writer"],
        ["Читатель", add_reader, "Reader"],
    ]

    def available_class(self):
        """Пишет доступные для выбора классы и возвращает номер выбранного"""
        print("Выбор типа объекта:")
        for i, item in enumerate(self.class_type):
            print(f"[{i}] {item[0]}")
        number = -2
        while not 0 <= number <= (len(self.class_type) - 1):
            print(f"Введите число от 0 до {len(self.class_type) - 1}")
            number = int(input(">>"))
        return number
    # --- Конец ---

    def one_item_choose(self):
        """Выбрать одну конкретную запись из всех"""
        r = requests.get(self.url + "show")
        num = self.available_class()
        c_type = self.class_type[num][2]
        for key_type, value_list in r.json().items():
            if key_type == c_type:
                for e_list in value_list:
                    print("")
                    for i, element in enumerate(e_list):
                        if i == 0:
                            print(f"ID:{element}")
                        else:
                            print(element)
        print("Выбор объекта")
        return {"type": self.class_type[num][0],
                "id": input("ID>>"),
                }

    def add(self):
        """Добавление объекта"""
        print("[Добавляем объект]")

        # print(self.url)
        r = requests.post(self.url + "add_person",
                          data=self.class_type[self.available_class()][1](self))
        if r.text == "True":
            print("Успешно добавили!")

    def delete(self):
        """Удаление объекта"""
        print("[Удаляем объект]")
        r = requests.get(self.url + "del_person",
                         self.one_item_choose())

    def edit(self):
        print("[Изменяем объект]")
        person_info = self.one_item_choose()
        r = requests.get(self.url + "edite_person",
                         person_info)
        # print(r.json())
        print("Изменяем:")
        for element in r.json()[0]:
            print(element)

        if person_info["type"] == "Писатель":
            person_info["Surname"] = input("Фамилия>>")
            person_info["Name"] = input("Имя>>")
            person_info["Experience"] = int(input("Опыт>>"))

        if person_info["type"] == "Читатель":
            person_info["Surname"] = input("Фамилия>>")
            person_info["Name"] = input("Имя>>")
            person_info["Age"] = int(input("Возраст>>"))

        print(person_info)
        r = requests.post(self.url + "edite_person",
                          person_info)

    def show(self):
        """Вывод объектов"""
        print("[Вывод объектов]")
        r = requests.get(self.url + "show")
        # print(r.json())
        for key_type, value_list in r.json().items():
            print(f"!!! Тип {key_type} !!!")
            for e_list in value_list:
                print("")
                for i, element in enumerate(e_list):
                    if i == 0:
                        print(f"ID:{element}")
                    else:
                        print(element)

    def get_url(self):
        """Поиск st"""
        url = 'http://localhost:5000/'
        response = requests.get(url + 'api/')
        # print(response.json())
        for item in response.json()['sts']:
            if item[1] == '[2204-08] Довиденков 2204':
                print(f"наш st{item[0]}")
                return self.url + 'st' + str(item[0]) + '/api/'
        print("Не нашли наш st")

    # старый вариант поиска st
    # def get_url(self):
    #     """Поиск st"""
    #     if self.st is False:
    #         print("Стартовые настройки. Ожидайте.")
    #         for i in range(90):
    #             response = requests.get(self.url + f'st{i}/Dovidenkov')
    #             if response.status_code == 200:
    #                 # print("Нашли подходящий ресурс")
    #                 if response.text == "Yes":
    #                     # print(f"Пройдена проверка подлиности| наш {self.url}st{i}")
    #                     print("Завершение стартовых настроек.")
    #                     return self.url + 'st' + str(i) + '/api/'
    #             else:
    #                 # print(response.raise_for_status())
    #                 pass
    #     else:
    #         print(f'Искомый адресс уже найден {self.url}')
    #         return self.url

    # идут функции под стратегию
    def input(self, *args):
        self.add()

    def output(self, *args):
        self.show()

    def delete(self, *args):
        self.delete()

    def edite(self, *args):
        self.edit()

    # функции под стратегию кончились

    # menu = [
    #     ["Добавить объект", add],
    #     ["Редактировать", edit],
    #     ["Удалить объект", delete],
    #     ["Вывести все объекты", show],
    #     ["Выход"],
    # ]
    #
    # def working_menu(self):
    #     """ Текст для меню """
    #     while True:
    #         for i, value in enumerate(self.menu):
    #             print(f"[{i}] {value[0]}")
    #
    #         choose = int(input(">>"))
    #         if self.menu[choose][0] == "Выход":
    #             break
    #         else:
    #             self.menu[choose][1](self)