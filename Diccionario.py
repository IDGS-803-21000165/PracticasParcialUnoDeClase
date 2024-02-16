from wtforms import Form
from wtforms import StringField, RadioField
from wtforms import validators


class Diccionario(Form):
    inglesTxt = StringField("Palabra en Ingles", [
        validators.DataRequired(message="Palabra en ingles requerida"),
        validators.Length(min=2, max=15, message='Ingrese una palabra valida')
    ])

    espaniolTxt = StringField("Palabra en español", [
        validators.DataRequired(message="Palabra en español requerida"),
        validators.Length(min=2, max=15, message='Ingrese una palabra valida')
    ])


class Traductor(Form):
    OPCIONES_IDIOMA = [
        ('Es', 'Español'),
        ('En', 'Inglés'),
    ]

    palabraBus = StringField("Palabra para traducir", [
        validators.DataRequired(message="Palabra en español requerida"),
        validators.Length(min=2, max=15, message='Ingrese una palabra valida')
    ])

    idiomaOpcion = RadioField(
        "Seleccione el idioma a traducir", choices=OPCIONES_IDIOMA)
