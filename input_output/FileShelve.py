import os
import shelve

from input_output.AbClass import MyAbstract
from model import Group, Writer, Reader

file_path = os.getcwd()+'\\data'


class FileShelve(MyAbstract):

    def __init__(self):
        pass

    def input(self, g =None):
        g = Group("Test_group")
        with shelve.open(file_path) as shelveFile:
            for i in range(shelveFile["count"]):
                if shelveFile[str(i)]["type"] == "Писатель":
                    person = Writer(shelveFile[str(i)]["name"], shelveFile[str(i)]["surname"], shelveFile[str(i)]["experience"])

                if shelveFile[str(i)]["type"] == "Читатель":
                    person = Reader(shelveFile[str(i)]["name"], shelveFile[str(i)]["surname"], shelveFile[str(i)]["age"])

                g.add_person(person)
            return g

    def output(self, g):
        shelveFile = shelve.open(file_path)
        for i, person in enumerate(g.person_list):
            shelveFile[str(i)] = person.get_dict()
        shelveFile["count"] = len(g.person_list)
        shelveFile.close()



