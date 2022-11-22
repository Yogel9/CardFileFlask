from abc import ABC, abstractmethod


class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name}| {self.surname}"

    def get_user_info(self):
        print(f"Имя: {self.name} \nФамилия: {self.surname}")

