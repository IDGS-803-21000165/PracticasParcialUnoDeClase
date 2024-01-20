class Piramide:
    def __init__(self):
        self.numero = int(input("Igrese el número para generar la piramide: "))

    def crearPiramide(self):
        for i in range(1, self.numero + 1):
            for j in range(1, i + 1):
                print("*", end="")
            print()


def main():
    obj = Piramide()
    obj.crearPiramide()


if __name__ == '__main__':
    main()
