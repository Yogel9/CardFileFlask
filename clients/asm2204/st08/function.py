# from input_output.Console import Console
from app.asm2204.st08 import Group
from clients.asm2204.st08.input_output.Console import Console


global g


def init_group():
    global g
    g = Group("Test_group")


def input_check(value, type='int', min_value=0, max_value=100):
    if type == 'int':
        try:
            if int(value) >= min_value or int(value) <= max_value:
                return True
            print(f"{value} не входит в интервал от {min_value} до {max_value}")
            return False
        except:
            return False
    else:
        return True


def show_all_object(text="изменения"):
    print(f"[Объекты доступные для {text}:]")
    for i, person in enumerate(g.person_list):
        print(f"Объект № {i}")
        person.get_user_info()
    print(f"Выберите № объекта(от 0 до {len(g.person_list) - 1}):")


def edite_object(IOclass=None):
    """Изменение записи"""
    if IOclass is not None:
        IOclass.edite()
    else:
        c = Console()

        if len(g.person_list) == 0:
            return False

        print("[Вы хотите изменить объект в списоке]")
        show_all_object()

        while True:
            person_id = input()
            if input_check(person_id, "int", 0, len(g.person_list)-1):
                editable_person = g.get_person(person_id)
                print("[Изменяемы объект]\n")
                editable_person.get_user_info()
                g.edit_person(person_id, c.new_person())
                break
            else:
                show_all_object()


def del_object(IOclass=None):
    """Удаление записи"""
    if IOclass is not None:
        IOclass.delete()
    else:
        if len(g.person_list) == 0:
            return False
        show_all_object("удаления")
        while True:
            person_id = input()
            if input_check(person_id, "int", 0, len(g.person_list)-1):
                g.del_person(person_id)
                break
            else:
                show_all_object()


def data_input(input_class):
    """Добавить объект"""
    global g
    g = input_class.input(g)
    pass


def data_output(output_class):
    """Вывести объект(на консоль/файл)"""
    output_class.output(g)
    pass
