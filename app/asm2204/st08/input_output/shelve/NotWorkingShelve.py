import os
import shelve

file_path = os.getcwd()+'\\data\\asm2204\\st08\\LR1_data\\data'


class FileShelve:

    def __init__(self):
        pass

    def input(self):
        with shelve.open(file_path) as f:
            return f["g_list"]

    def output(self, g):
        shelveFile = shelve.open(file_path)
        shelveFile["g_list"] = g
        shelveFile.close()

