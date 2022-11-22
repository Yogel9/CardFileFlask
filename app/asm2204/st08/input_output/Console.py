from app.asm2204.st08 import Writer, Reader


class Console:
    object_type = ["Писатель", "Читатель"]

    def __init__(self):
        pass

    def get_info_from_console(self, type=None):
        print("Имя:")
        name = input()
        print("Фамилия:")
        surname = input()

        match str(type):
            case "Writer":
                print("Стаж:")
                experience = input()
                return Writer(name, surname, experience)
            case "Reader":
                print("Возраст:")
                age = input()
                return Reader(name, surname, age)
            case None:
                pass

    def new_person(self):
        print("Тип объекта:")
        for i, obj in enumerate(self.object_type):
            print(f"[{i}] {obj}")
        print(f"[other] Возвращение к меню")

        match input():
            case "0":
                return self.get_info_from_console(type="Writer")
            case "1":
                return self.get_info_from_console(type="Reader")
            case _:
                pass

    def input(self, g):
        p = self.new_person()
        print(p)
        g.add_person(p)
        return g

    def output(self, g):
        print("<------------------------------------>\n")
        if len(g.person_list) == 0:
            print("Список пуст")
        else:
            print("№ Имя|Фамилия|Категория")
            for i, person in enumerate(g.person_list):
                print(i, str(person))
        print("<------------------------------------>\n")


