import pickle

from input_output.AbClass import MyAbstract


class File(MyAbstract):

    def __init__(self):
        pass

    def input(self, g):
        with open('data.pickle', 'rb') as f:
            return pickle.load(f)

    def output(self, g):
        with open('data.pickle', 'wb') as f:
            pickle.dump(g, f)