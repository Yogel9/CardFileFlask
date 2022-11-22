import os
import pickle

file_path = os.getcwd()+'\\data\\asm2204\\st08\\data.pickle'


class File:

    def __init__(self):
        pass

    def input(self):
        with open(file_path, 'rb') as f:
            return pickle.load(f)

    def output(self, g):
        with open(file_path, 'wb') as f:
            pickle.dump(g, f)
