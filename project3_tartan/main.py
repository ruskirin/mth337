import constants
from objects import tartan


def main():
    print(constants.COLORS)
    print(constants.TARTANS)

    while True:
        a = input("Enter tartan name: ")
        tartan.Tartan(a)

if __name__ == '__main__':
    constants.init_data()

    main()