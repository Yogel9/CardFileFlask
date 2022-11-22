import os

from flask import render_template, request, redirect, url_for, Blueprint

from app.asm2204.st08.input_output.File import File
from app.asm2204.st08.input_output.shelve.NotWorkingShelve import FileShelve
from app.asm2204.st08.input_output.FlaskForm import FlaskForm
from app.asm2204.st08.input_output.MyDatabase import SQLite
from app.asm2204.st08.model.group import Group
from app.asm2204.st08.model.reader import Reader, get_age_limit
from app.asm2204.st08.model.writer import Writer


bp = Blueprint('st08',
               __name__,
               template_folder=os.getcwd()+'\\app\\templates\\asm2204\\st08\\templates\\',
               static_folder=os.getcwd()+'\\app\\static\\asm2204\\st08\\static\\')

# global g
# g = Group("Test_group")
s = SQLite()


@bp.route('/', methods=['POST', 'GET'])
def index():
    s.db_request("create_table")
    return redirect(url_for(".card_person"))


@bp.route('/table_person', methods=['POST', 'GET'])
def table_person():
    context = {"title": "Табличное представление",
               "person_list": bd_to_group(s.db_request("get_all")).person_list, }
    return render_template('table.html', context=context)


@bp.route('/card_person', methods=['POST', 'GET'])
def card_person():
    f = FlaskForm()
    f.clear_for_output()

    all_items = s.db_request("get_all")

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
    return render_template('card.html', context=context)


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
            s.db_request("add_items", new_data)
            # g.add_person(Writer(new_data["Name"], new_data["Surname"], new_data["Experience"]))
        if new_data["type"] == "Читатель":
            new_data["Age_limit"] = get_age_limit(new_data["Age"])
            s.db_request("add_items", new_data)
            # g.add_person(Reader(new_data["Name"], new_data["Surname"], new_data["Age"]))

    return render_template('add_person.html', context=context)


@bp.route('/edite_person/<type>/<pers_number>/', methods=['POST', 'GET'])  # это главная страница
def edite_person(pers_number=None, type=None):
    object_type = ["Писатель", "Читатель"]
    context = {"pers_number": pers_number,
               "obj_type": object_type}

    data = {"type": type,
            "id": pers_number, }

    if request.method == 'GET':
        context["info"] = s.db_request("get_one", data)
        context["person_type"] = type

    if request.method == 'POST':

        f = FlaskForm()
        f.input(request.form.to_dict())

        new_data = f.get_input_data()
        new_data["id"] = data["id"]
        new_data["type"] = data["type"]
        if new_data["type"] == "Писатель":
            new_data["Salary"] = float(new_data["Experience"]) * 1000
            s.db_request("update_item", new_data)
            # g.edit_person(pers_number, Writer(request.form.get("Name"), request.form.get("Surname"),
            #                                   request.form.get("Experience")))
        if new_data["type"] == "Читатель":
            new_data["Age_limit"] = get_age_limit(new_data["Age"])
            s.db_request("update_item", new_data)
            # g.edit_person(pers_number, Reader(request.form.get("Name"), request.form.get("Surname"),
            #                                   request.form.get("Age")))
        return redirect(url_for(".card_person"))

    return render_template('edite_person.html', context=context)


@bp.route('/del_person/<type>/<pers_number>/', methods=['POST', 'GET'])  # это главная страница
def del_person(pers_number=None, type=None):
    data = {"type": type,
            "id": pers_number, }
    s.db_request("delete_item", data)
    return redirect(url_for("st08.index"))


def bd_to_group(all_items):
    g = Group("Test_group")

    for reader in all_items["Reader"]:
        g.add_person(Reader(reader[1], reader[2], reader[3]))

    for w in all_items["Writer"]:
        g.add_person(Writer(w[1], w[2], w[3]))

    return g


@bp.route('/save_file')  # это главная страница
def save_file():
    f = File()
    f.output(bd_to_group(s.db_request("get_all")))

    return redirect(url_for("st08.index"))


@bp.route('/upload_file')  # это главная страница
def upload_file():
    f = File()
    g = Group("Test_group")
    g = f.input()

    for person in g.person_list:
        new_data = person.get_dict()

        if new_data["type"] == "Писатель":
            s.db_request("add_items", new_data)
        else:
            s.db_request("add_items", new_data)

    return redirect(url_for("st08.index"))


# if __name__ == "__main__":
#     app.run(debug=True)
