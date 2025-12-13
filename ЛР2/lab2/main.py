from lab2.rectangle import Rectangle
from lab2.circle import Circle
from lab2.square import Square
from termcolor import colored

def main():
    r = Rectangle("синего", 12, 13)
    c = Circle("зеленого", 0.5)
    s = Square("красного", 22)

    print(r)
    print(c)
    print(s)

    print(colored("Это строка из внешнего пакета termcolor!", "red"))
    print(colored("Демонстрация работы с внешним пакетом", "green", attrs=["bold"]))

if __name__ == "__main__":
    main()
