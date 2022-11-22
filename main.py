from function import init_group, data_input, edite_object, data_output, del_object
from input_output.Console import Console
# from input_output.File import File
from input_output.FileShelve import FileShelve

f = FileShelve()
c = Console()


def text_for_menu():
    """ Текст для меню """
    print("         Меню          \n"
          "[1] Добавить объект    \n"
          "[2] Редактировать      \n"
          "[3] Удалить объект     \n"
          "[4] Вывести все объекты\n"
          "[5] Сохранить в файл   \n"
          "[6] Загрузить с файла  \n"
          "[0] Выход              \n"
          )


def context_menu():
    """ Меню для вызова функций """
    init_group()
    stop = False
    while not stop:
        text_for_menu()
        match input():
            case "1":
                data_input(c)
            case "2":
                edite_object()
            case "3":
                del_object()
            case "4":
                data_output(c)
            case "5":
                data_output(f)
            case "6":
                data_input(f)
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


