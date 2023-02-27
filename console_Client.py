import clients.asm2204.st08.main


MENU = [
    ["[2204-08] Довиденков 2204", clients.asm2204.st08.main.main],
]


def menu():
    print("------------------------------")
    for i, item in enumerate(sorted(MENU)):
        print("{0:2}. {1}".format(i, item[0]))
    print("------------------------------")
    return int(input())


try:
    while True:
        sorted(MENU)[menu()][1]()
except Exception as ex:
    print(ex, "\nbye")
