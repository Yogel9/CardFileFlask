import requests

from app.asm2204.st08.input_output.Console import Console
from clients.asm2204.st08.function import init_group, data_input, edite_object, data_output, del_object
from clients.asm2204.st08.input_output.RestApi import RestConsole
# from .function import init_group, data_input, edite_object, data_output, del_object
# from input_output.Console import Console
# from input_output.File import File
# from input_output.FileShelve import FileShelve


def text_for_menu():
    """ Текст для меню """
    print("         Меню          \n"
          "[1] Добавить объект    \n"
          "[2] Редактировать      \n"
          "[3] Удалить объект     \n"
          "[4] Вывести все объекты\n"
          "[0] Выход              \n")


def context_menu():
    """ Меню для вызова функций """
    # f = FileShelve() итак есть вывод в flask
    c = RestConsole()

    if isinstance(c, Console):
        init_group()

    stop = False
    while not stop:
        text_for_menu()
        match input():
            case "1":
                data_input(c)
            case "2":
                edite_object(c)
            case "3":
                del_object(c)
            case "4":
                data_output(c)

            case "0":
                print("[Завершение работы]")
                stop = True
            case _:
                print("[Повторите ввод]")
                pass


def main():
    context_menu()


if __name__ == '__main__':
    main()
