import os

from flask import render_template, request, redirect, url_for, Blueprint, g, current_app

from app.asm2204.st08.input_output.File import File
from app.asm2204.st08.input_output.shelve.NotWorkingShelve import FileShelve
from app.asm2204.st08.input_output.FlaskForm import FlaskForm
from app.asm2204.st08.input_output.MyDatabase import SQLite
from app.asm2204.st08.model.group import Group
from app.asm2204.st08.model.reader import Reader, get_age_limit
from app.asm2204.st08.model.writer import Writer


bp = Blueprint('st08',
               __name__,
               template_folder=os.getcwd() + '\\app\\templates\\asm2204\\st08\\templates\\',
               static_folder=os.getcwd() + '\\app\\static\\asm2204\\st08\\static\\')


# global g
# g = Group("Test_group")


@bp.before_request
def bd_connection():
    g.bd = SQLite()


@bp.route('/Dovidenkov', methods=['GET'])
def find_me():
    return "Yes"


@bp.route('/', methods=['POST', 'GET'])
def index():
    g.bd.db_request("create_table")
    return redirect(url_for(".card_person"))


@bp.route('/table_person', methods=['POST', 'GET'])
def table_person():
    context = {"title": "Табличное представление",
               "person_list": bd_to_group(g.bd.db_request("get_all")).person_list, }
    return render_template('/asm2204/st08/templates/table.html', context=context)


@bp.route('/card_person', methods=['POST', 'GET'])
def card_person():
    f = FlaskForm()
    f.clear_for_output()
    print(g.bd)
    all_items = g.bd.db_request("get_all")

    for reader in all_items["Reader"]:
        # print(reader)
        f.add_for_output(["Тип", "ID", "Имя", "Фамилия", "Возраст", "РСВР"],
                         ["Читатель", reader[0], reader[1], reader[2], reader[3], reader[4]])

    for w in all_items["Writer"]:
        # print(w)
        f.add_for_output(["Тип", "ID", "Имя", "Фамилия", "Стаж", "Зарплата"],
                         ["Писатель", w[0], w[1], w[2], w[3], w[4]])

    context = {"title": "Карточки",
               "person_list": f.output()}
    return render_template('/asm2204/st08/templates/card.html', context=context)


@bp.route('/add_person', methods=['POST', 'GET'])
def add_person():
    object_type = ["Писатель", "Читатель"]
    context = {"title": "Добавление",
               "obj_type": object_type}

    if request.method == 'POST':
        f = FlaskForm()
        f.input(request.form.to_dict())

        new_data = f.get_input_data()

        if new_data["type"] == "Писатель":
            new_data["Salary"] = float(new_data["Experience"]) * 1000
            g.bd.db_request("add_items", new_data)
            # g.add_person(Writer(new_data["Name"], new_data["Surname"], new_data["Experience"]))
        if new_data["type"] == "Читатель":
            new_data["Age_limit"] = get_age_limit(new_data["Age"])
            g.bd.db_request("add_items", new_data)
            # g.add_person(Reader(new_data["Name"], new_data["Surname"], new_data["Age"]))

    return render_template('/asm2204/st08/templates/add_person.html', context=context)


@bp.route('/edite_person/<type>/<pers_number>/', methods=['POST', 'GET'])  # это главная страница
def edite_person(pers_number=None, type=None):
    object_type = ["Писатель", "Читатель"]
    context = {"pers_number": pers_number,
               "obj_type": object_type}

    data = {"type": type,
            "id": pers_number, }

    if request.method == 'GET':
        context["info"] = g.bd.db_request("get_one", data)
        context["person_type"] = type

    if request.method == 'POST':

        f = FlaskForm()
        f.input(request.form.to_dict())

        new_data = f.get_input_data()
        new_data["id"] = data["id"]
        new_data["type"] = data["type"]
        if new_data["type"] == "Писатель":
            new_data["Salary"] = float(new_data["Experience"]) * 1000
            g.bd.db_request("update_item", new_data)
            # g.edit_person(pers_number, Writer(request.form.get("Name"), request.form.get("Surname"),
            #                                   request.form.get("Experience")))
        if new_data["type"] == "Читатель":
            new_data["Age_limit"] = get_age_limit(new_data["Age"])
            g.bd.db_request("update_item", new_data)
            # g.edit_person(pers_number, Reader(request.form.get("Name"), request.form.get("Surname"),
            #                                   request.form.get("Age")))
        return redirect(url_for(".card_person"))

    return render_template('/asm2204/st08/templates/edite_person.html', context=context)


@bp.route('/del_person/<type>/<pers_number>/', methods=['POST', 'GET'])  # это главная страница
def del_person(pers_number=None, type=None):
    data = {"type": type,
            "id": pers_number, }
    g.bd.db_request("delete_item", data)
    return redirect(url_for("st08.index"))


def bd_to_group(all_items):
    group = Group("Test_group")

    for reader in all_items["Reader"]:
        group.add_person(Reader(reader[1], reader[2], reader[3]))

    for w in all_items["Writer"]:
        group.add_person(Writer(w[1], w[2], w[3]))

    return group


@bp.route('/save_file')  # это главная страница
def save_file():
    f = File()
    f.output(bd_to_group(g.bd.db_request("get_all")))

    return redirect(url_for("st08.index"))


@bp.route('/upload_file')  # это главная страница
def upload_file():
    f = File()
    # group = Group("Test_group")
    group = f.input()

    for person in group.person_list:
        new_data = person.get_dict()

        if new_data["type"] == "Писатель":
            g.bd.db_request("add_items", new_data)
        else:
            g.bd.db_request("add_items", new_data)

    return redirect(url_for("st08.index"))


# здесь функции с api
@bp.route('/api/add_person', methods=['POST', 'GET'])
def api_add_person():

    if request.get_json() is not None:
        json_data = request.json
        print(json_data)
        data_to_bd(json_data, "add_items")
        return "True"

    if request.method == 'POST':
        f = FlaskForm()
        f.input(request.form.to_dict())

        new_data = f.get_input_data()
        data_to_bd(new_data, "add_items")

    return "True"


def data_to_bd(data, type):
    """Добавляем высчитываемые поля перед отправкой в бд"""
    if data["type"] == "Писатель":
        data["Salary"] = float(data["Experience"]) * 1000
        g.bd.db_request(type, data)
    elif data["type"] == "Читатель":
        data["Age_limit"] = get_age_limit(data["Age"])
        g.bd.db_request(type, data)


@bp.route('/api/edite_person', methods=['POST', 'GET'])  # это главная страница
def api_edite_person():

    if request.get_json() is not None:
        json_data = request.json
        print(json_data)
        data_to_bd(json_data, "update_item")
        return "True"

    if request.method == 'GET':
        data = {"type": request.args.get('type'),
                "id": request.args.get('id'), }
        return g.bd.db_request("get_one", data)

    if request.method == 'POST':
        f = FlaskForm()
        f.input(request.form.to_dict())
        new_data = f.get_input_data()
        data_to_bd(new_data, "update_item")
        return "True"


@bp.route('/api/del_person', methods=['POST', 'GET'])  # это главная страница
def api_del_person():
    if request.get_json() is not None:
        json_data = request.json
        print(json_data)
        g.bd.db_request("delete_item", json_data)
        return "True"

    data = {"type": request.args.get('type'),
            "id": request.args.get('id'), }
    print(data)
    g.bd.db_request("delete_item", data)
    return "True"


@bp.route('/api/show')
def api_show():
    # словарь с листом
    for key_type, value_list in g.bd.db_request("get_all").items():
        print(value_list)
    return g.bd.db_request("get_all")
