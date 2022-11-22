from .user import User


class Writer(User):
    type = "Писатель"

    def __init__(self, name, surname, experience):
        self.name = name
        self.surname = surname
        self.experience = experience
        self.salary = int(experience) * 1000

    def __str__(self):
        return f"{self.name}| {self.surname}| {self.type}"

    def get_user_info(self):
        print(f"~Писатель~\nИмя: {self.name} \nФамилия: {self.surname} "
              f"\nСтаж:{self.experience}\nЗарплата:{self.salary}Р\n")

