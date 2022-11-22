from asm2204.st08.input_output.File import File
from asm2204.st08.input_output.FlaskForm import FlaskForm
from asm2204.st08.model.group import Group
from asm2204.st08.model.reader import Reader
from asm2204.st08.model.writer import Writer
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static')

global g
g = Group("Test_group")


@app.route('/', methods=['POST', 'GET'])
def index():
    return redirect(url_for("card_person"))
    # person_list = zip(list(range(len(g.person_list))), g.person_list)
    # context = {"title": "Главная",
    #            "person_list": person_list, }
    # return render_template('table.html', context=context)


@app.route('/table_person', methods=['POST', 'GET'])
def table_person():
    person_list = zip(list(range(len(g.person_list))), g.person_list)
    context = {"title": "Табличное представление",
               "person_list": person_list, }
    return render_template('table.html', context=context)


@app.route('/card_person', methods=['POST', 'GET'])
def card_person():
    f = FlaskForm()
    f.clear_for_output()
    for user_class in g.person_list:
        if user_class.type == "Писатель":
            f.add_for_output(["Имя", "Фамилия", "Стаж", "Зарплата"],
                             [user_class.name, user_class.surname, user_class.experience, user_class.salary])
        elif user_class.type == "Читатель":
            f.add_for_output(["Имя", "Фамилия", "Возраст", "РСВР"],
                             [user_class.name, user_class.surname, user_class.age, user_class.age_limit])
        else:
            pass

    context = {"title": "Карточки",
               "person_list": list(zip(range(len(g.person_list)-1), f.output()))}
    return render_template('card.html', context=context)


@app.route('/add_person', methods=['POST', 'GET'])
def add_person():
    object_type = ["Писатель", "Читатель"]
    context = {"title": "Добавление",
               "obj_type": object_type}

    if request.method == 'POST':
        f = FlaskForm()
        f.input(request.form.to_dict())

        if f.get_type() == "Писатель":
            g.add_person(Writer(f.get_name(), f.get_name(), f.get_experience()))
        else:
            g.add_person(Reader(f.get_name(), f.get_name(), f.get_age()))

    return render_template('add_person.html', context=context)


@app.route('/edite_person/<pers_number>', methods=['POST', 'GET'])  # это главная страница
def edite_person(pers_number=None):
    object_type = ["Писатель", "Читатель"]
    context = {"editable_person": g.get_person(pers_number),
               "pers_number": pers_number,
               "obj_type": object_type}

    if request.method == 'POST':
        if request.form.get("type") == "Писатель":
            g.edit_person(pers_number, Writer(request.form.get("Name"), request.form.get("Surname"),
                                              request.form.get("Experience")))
        else:
            g.edit_person(pers_number, Reader(request.form.get("Name"), request.form.get("Surname"),
                                              request.form.get("Age")))
        return redirect(url_for("index"))

    return render_template('edite_person.html', context=context)


@app.route('/del_person/<pers_number>', methods=['POST', 'GET'])  # это главная страница
def del_person(pers_number=None):
    g.del_person(pers_number)
    return redirect(url_for("index"))


@app.route('/save_file')  # это главная страница
def save_file():
    f = File()
    f.output(g)
    return redirect(url_for("index"))


@app.route('/upload_file')  # это главная страница
def upload_file():
    f = File()
    global g
    g = f.input()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
