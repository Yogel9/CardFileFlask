import os
import sqlite3


class SQLite:
    """Класс для работы с БД"""
    db_name = 'person_data.sqlite3'
    db_url = os.getcwd() + f'\\data\\asm2204\\st08\\{db_name}'

    def __init__(self, db_name=None, db_url=None):
        if db_url is not None:
            self.db_url = db_url
        if db_name is not None:
            self.db_name = db_name

    def __str__(self):
        return f"<Class SQLite> db_name: {self.db_name}"

    def set_url(self, db_url):
        self.db_url = db_url

    def set_name(self, db_name):
        self.db_name = db_name

    @staticmethod
    def get_all_request_name():
        return bd_request_dict

    def db_request(self, request_name, data=None):
        try:
            bd_connection = sqlite3.connect(self.db_url)
            # курсор - это специальный объект который делает запросы и получает их результаты
            cursor = bd_connection.cursor()
            print(f"<SQLite> Успешное подключение к {self.db_url}!")


            ############################Здесь будет лежать запрос###########################
            if data is None:
                result = bd_request_dict[request_name](bd_connection, cursor)
            else:
                result = bd_request_dict[request_name](bd_connection, cursor, data)
            ############################Здесь он кончается##################################

            cursor.close()

        except Exception as e:
            print(f"<Ошибка подключения к БД> Error: {e}")
        finally:
            if bd_connection:
                bd_connection.close()
                print(f"<SQLite> Соединение закрыто!")
        # если можем что-то вернуть вернём
        try:
            return result
        except: # иначе не судьба
            pass


def db_version(bd_connection, cursor):
    """Запрашиваем у ДБ версию"""
    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    print(f"<SQLite> Версия базы данных SQLite: {cursor.fetchall()[0][0]}")


def create_table(bd_connection, cursor):
    """Создаем таблицы"""
    # print("Создание таблиц 0/2")
    cursor.execute(r_create_table_writer)
    # print("Создание таблиц 1/2")
    cursor.execute(r_create_table_reader)
    # print("Создание таблиц 2/2")


def drop_table(bd_connection, cursor):
    """Удаляем таблицы из листа ниже"""
    table_name = ["Writer",
                  "Reader"]
    for i, name in enumerate(table_name):
        print(f"Удаление таблиц {i+1}/{len(table_name)}")
        cursor.execute(r_drop_table + name)


def add_items(bd_connection, cursor, data_dict):
    """"Добавляем нвоы объект"""
    if data_dict["type"] == 'Читатель':
        cursor.execute(reader_add, (data_dict["Name"],
                                    data_dict["Surname"],
                                    data_dict["Age"],
                                    data_dict["Age_limit"]))
    if data_dict['type'] == 'Писатель':
        cursor.execute(writer_add, (data_dict["Name"],
                                    data_dict["Surname"],
                                    data_dict["Experience"],
                                    data_dict["Salary"]))
    bd_connection.commit()


def get_all_items(bd_connection, cursor):
    """Получаем все объекты с бд"""
    cursor.execute(writer_get_all)
    writer_list = cursor.fetchall()
    cursor.execute(reader_get_all)
    reader_list = cursor.fetchall()
    return {"Writer": writer_list,
            "Reader": reader_list}


def get_one_item(bd_connection, cursor, data_dict):
    """Получаем один объект по id"""
    if data_dict["type"] == "Писатель":
        cursor.execute(writer_get, (data_dict["id"]))
        return cursor.fetchall()
    elif data_dict["type"] == "Читатель":
        cursor.execute(reader_get, (data_dict["id"]))
        return cursor.fetchall()
    else:
        return None


def edite_one_item(bd_connection, cursor, data_dict):
    """Изменяем один объект по id"""
    if data_dict["type"] == "Писатель":
        cursor.execute(writer_update, (data_dict["Name"],
                                       data_dict["Surname"],
                                       float(data_dict["Experience"]),
                                       float(data_dict["Salary"]),
                                       data_dict["id"],))

        print("ОБНОВИЛИ ПИСАТЕЛЯ")
    if data_dict["type"] == "Читатель":
        cursor.execute(reader_update, (data_dict["Name"],
                                       data_dict["Surname"],
                                       data_dict["Age"],
                                       data_dict["Age_limit"],
                                       data_dict["id"],))
        print("ОБНОВИЛИ ЧИТАТЕЛЯ")
    bd_connection.commit()


def delete_one_item(bd_connection, cursor, data_dict):
    """Удаляем один объект по id"""
    print(f"[Удаление] {data_dict}")
    if data_dict["type"] == "Писатель":
        cursor.execute(writer_delete, (data_dict["id"],))
    if data_dict["type"] == "Читатель":
        cursor.execute(reader_delete, (data_dict["id"],))

    bd_connection.commit()


# Удаление таблицы
r_drop_table = "DROP TABLE "

# Создание таблиц
r_create_table_writer = '''CREATE TABLE IF NOT EXISTS Reader
                        (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        surname text NOT NULL,
                        age INTEGER NOT NULL,
                        age_limit TEXT NOT NULL
                        ); '''


r_create_table_reader = '''CREATE TABLE IF NOT EXISTS Writer
                        (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        surname TEXT NOT NULL,
                        experience REAL NOT NULL,
                        salary REAL NOT NULL);'''


# добавление записей
writer_add = 'INSERT INTO Writer (name, surname,experience, salary)  VALUES (?, ?, ?, ?)'
reader_add = 'INSERT INTO Reader (name, surname,age, age_limit)  VALUES (?, ?, ?, ?)'

# считываем записи
writer_get_all = 'SELECT * FROM Writer'
reader_get_all = 'SELECT * FROM Reader'

# считываем записи
writer_get = 'SELECT * FROM Writer WHERE id=?'
reader_get = 'SELECT * FROM Reader WHERE id=?'


# Изменяем запись
writer_update = 'UPDATE Writer SET name = ?, surname = ?, experience = ?, salary = ? WHERE id = ?'
reader_update = 'UPDATE Reader SET name = ?, surname = ?, age = ?, age_limit = ? WHERE id = ?'

# Удаление
writer_delete = 'DELETE FROM Writer WHERE id=?'
reader_delete = 'DELETE FROM Reader WHERE id=?'


# словарь запросов
bd_request_dict = {
    "version": db_version,
    "create_table": create_table,
    "drop_table": drop_table,
    "add_items": add_items,
    "get_all": get_all_items,
    "get_one": get_one_item,
    "update_item": edite_one_item,
    "delete_item": delete_one_item,
}





# s = SQLite()

#
# def my_db_decorator(function):
#     """Вопрос, как  bd_connection и cursor передать в функцию из
#     обертки, а не из вызова функции
#     """
#     def wrapper(bd_connection=None, cursor=None):
#         try:
#             print(f"Вошли в обертку {bd_connection}")
#             bd_connection = sqlite3.connect(s.get_url())
#             cursor = bd_connection.cursor()
#             print(f"<SQLite> Соединение открыто!")
#             # ТУТ
#             function(bd_connection, cursor)
#             cursor.close()
#         except Exception as e:
#             print(f"<Ошибка подключения к БД> Error: {e}")
#         finally:
#             if bd_connection:
#                 bd_connection.close()
#                 print(f"<SQLite> Соединение закрыто!")
#
#     return wrapper()
#
#
# @my_db_decorator
# def init_db(connection=None, cursor=None):
#     sqlite_select_query = "select sqlite_version();"
#     cursor.execute(sqlite_select_query)
#     print(f"<SQLite> Версия базы данных SQLite: {cursor.fetchall()[0][0]}")



