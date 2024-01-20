from Piramide import Piramide
from ComparadorListaNumeros import ComparadorListaNumeros

print("Piramide".center(50, '-'))
objP = Piramide()
objP.crearPiramide()

print("Comparador Lista Numeros".center(50, '-'))
comparador = ComparadorListaNumeros()
comparador.ingresar_numeros()
comparador.mostrar_resultados()
