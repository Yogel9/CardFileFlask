from .user import User


def get_age_limit(age):
    if age > "18":
        return "18+"
    elif age > "16":
        return "16+"
    elif age > "12":
        return "12+"
    elif age > "6":
        return "6+"
    else:
        return "0+"
    return


class Reader(User):
    type = "Читатель"

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.age_limit = get_age_limit(age)

    def __str__(self):
        return f"{self.name}| {self.surname}| {self.type}"

    def get_user_info(self):
        print(f"~Читатель~\nИмя: {self.name} \nФамилия: {self.surname} \nВозраст:{self.age}\n"
              f"РСВР:{self.age_limit}\n")  # РСВР — «Российская Система Возрастных Рейтингов»
