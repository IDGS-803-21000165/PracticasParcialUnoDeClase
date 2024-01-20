class ComparadorListaNumeros:
    def __init__(self):
        self.num_long = int(input("Ingrese el número de dígitos a escribir: "))
        self.num_list = []
        self.pares = []
        self.impares = []
        self.num_repetidos = {}

    def ingresar_numeros(self):
        for i in range(self.num_long):
            self.num_list.append(int(input("Ingrese el número: ")))

    def mostrar_resultados(self):
        print(f'Números ingresados: {self.num_list}')
        self.num_list.sort()
        print(f'Números ordenados: {self.num_list}')

        # Validar numeros repetidos
        for numero in self.num_list:
            if numero in self.num_repetidos:
                self.num_repetidos[numero] += 1
            else:
                self.num_repetidos[numero] = 1

        # Obtener numeros pares e impares
        set_nums = set(self.num_list)
        for numero in set_nums:
            if numero % 2 == 0:
                self.pares.append(numero)
            else:
                self.impares.append(numero)

        for numero, cantidad in self.num_repetidos.items():
            print(f"El número {numero} se repitió {cantidad} veces")

        print(
            f'Los números pares son: {len(self.pares)} y el listado es: {self.pares}')
        print(
            f'Los números impares son: {len(self.impares)} y el listado es: {self.impares}')


def main():
    comparador = ComparadorListaNumeros()
    comparador.ingresar_numeros()
    comparador.mostrar_resultados()


if __name__ == '__main__':
    main()
