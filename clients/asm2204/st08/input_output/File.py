import pickle




class File:

    def __init__(self):
        pass

    def input(self, g):
        with open('asm2204/st08/data.pickle', 'rb') as f:
            return pickle.load(f)

    def output(self, g):
        with open('asm2204/st08/data.pickle', 'wb') as f:
            pickle.dump(g, f)