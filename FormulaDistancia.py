from wtforms import Form
from wtforms import IntegerField


class FormulaDistancia(Form):
    xUno = IntegerField("Esquis Uno")
    xDos = IntegerField("Equis Dos")
    yUno = IntegerField("Y Uno")
    yDos = IntegerField("Y Dos")
