from .user import User


class Writer(User):
    type = "Писатель"

    def __init__(self, name, surname, experience):
        self.name = name
        self.surname = surname
        self.experience = experience
        self.salary = int(experience) * 1000

    def get_dict(self):
        return {"type": self.type,
                "Name": self.name,
                "Surname": self.surname,
                "Experience": self.experience,
                "Salary": self.salary}

    def __str__(self):
        return f"<Writer> {self.name}| {self.surname}| {self.type}| {self.salary}"

    def get_user_info(self):
        print(f"~Писатель~\nИмя: {self.name} \nФамилия: {self.surname} "
              f"\nСтаж:{self.experience}\nЗарплата:{self.salary}Р\n")

