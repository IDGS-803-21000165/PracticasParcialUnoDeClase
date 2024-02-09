from wtforms import Form
from wtforms import SelectField, RadioField


class Resistencias(Form):
    OPCIONES_COLORES = [
        (0, 'Negro'),
        (1, 'Cafe'),
        (2, 'Rojo'),
        (3, 'Naranja'),
        (4, 'Amarillo'),
        (5, 'Verde'),
        (6, 'Azul'),
        (7, 'Violeta'),
        (8, 'Gris'),
        (9, 'Blanco')
    ]

    OPCIONES_TOLERANCIA = [
        ('0.05', 'Dorado'),
        ('0.10', 'Plata'),
    ]

    colorUno = SelectField("Color 1", choices=OPCIONES_COLORES)
    colorDos = SelectField("Color 2", choices=OPCIONES_COLORES)
    colorTres = SelectField("Color 3", choices=OPCIONES_COLORES)
    tolerancia = RadioField("Tolerancia", choices=OPCIONES_TOLERANCIA)
