from flask import Flask, render_template, request
import FormulaDistancia as fm
import Resistencias as rs
from math import sqrt

app = Flask(__name__)


@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        if request.form.get("operacion") == "suma":
            num1 = request.form.get("n1")
            num2 = request.form.get("n2")
            return f'<h1>La suma es: {str(int(num1) + int(num2))} </h1>'
        elif request.form.get("operacion") == "resta":
            num1 = request.form.get("n1")
            num2 = request.form.get("n2")
            return f'<h1>La resta es: {str(int(num1) - int(num2))} </h1>'
        elif request.form.get("operacion") == "multiplicacion":
            num1 = request.form.get("n1")
            num2 = request.form.get("n2")
            return f'<h1>La multiplicacion es: {str(int(num1) * int(num2))} </h1>'
        elif request.form.get("operacion") == "division":
            num1 = request.form.get("n1")
            num2 = request.form.get("n2")
            return f'<h1>La division es: {str(int(num1) / int(num2))} </h1>'


@app.route("/formulario")
def formulario():
    return render_template("formulario.html")


@app.route("/cinepolis")
def cinepolis():
    return render_template("formulario_cinepolis.html")


@app.route("/entradas", methods=["GET", "POST"])
def entradas():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        cantidadCompradores = int(request.form.get("cantidadDeCompradores"))
        tarjeta = request.form.get("tarjeta")
        cantidadBoletas = int(request.form.get("cantidadDeBeletas"))

        cantidadBPermitida = cantidadCompradores * 7
        precioTotal = cantidadBoletas*12
        resultadoFinal = 0

        if cantidadBoletas > cantidadBPermitida:
            return render_template("formulario_cinepolis.html", alerta='Número de boletos por persona excedido')
        else:
            if cantidadBoletas > 5:
                resultadoFinal = precioTotal - (precioTotal * .15)
            elif 3 <= cantidadBoletas <= 5:
                resultadoFinal = precioTotal - (precioTotal * .10)
            else:
                resultadoFinal = precioTotal

        if tarjeta == 'si':
            resultadoFinal = resultadoFinal - (resultadoFinal*.10)
            return render_template("formulario_cinepolis.html", nombre=nombre, resultado=resultadoFinal)
        else:
            return render_template("formulario_cinepolis.html", nombre=nombre, resultado=resultadoFinal)


@app.route("/formularioDistancia", methods=["GET", "POST"])
def alumnos():
    dist_form = fm.FormulaDistancia(request.form)
    suma = 0
    raiz = 0
    result = 0

    if request.method == 'POST':
        xU = dist_form.xUno.data
        xD = dist_form.xDos.data
        yU = dist_form.yUno.data
        yD = dist_form.yDos.data

        print(xU, xD, yU, yD)
        suma = ((xU-xD)**2 + (yU-yD)**2)
        raiz = sqrt(suma)
        result = raiz

    return render_template("formularioDistancia.html", form=dist_form, rest=result)


@app.route("/resistencias", methods=["GET", "POST"])
def resistencias():
    resi_form = rs.Resistencias(request.form)
    colU = 0
    colD = 0
    colT = 0
    tol = 0
    val = 0
    valMax = 0.0
    valMin = 0.0
    colTol = ""

    if request.method == 'POST':
        if (resi_form.colorUno.data is None):
            colU = 0
        else:
            colU = resi_form.colorUno.data

        if (resi_form.colorDos.data is None):
            colD = 0
        else:
            colD = resi_form.colorDos.data

        if (resi_form.colorTres.data is None):
            colT = 0
        else:
            colT = resi_form.colorTres.data

        if (resi_form.tolerancia.data is None):
            tol = 0
        else:
            tol = resi_form.tolerancia.data

    print(colU, colD, colT, tol)

    val = int(colU+colD) * (10 ** int(colT))
    valMax = val + val*float(tol)
    valMin = val - val*float(tol)

    if int(colU) == 0:
        colU = "negro"
    elif int(colU) == 1:
        colU = "cafe"
    elif int(colU) == 2:
        colU = "rojo"
    elif int(colU) == 3:
        colU = "naranja"
    elif int(colU) == 4:
        colU = "amarillo"
    elif int(colU) == 5:
        colU = "verde"
    elif int(colU) == 6:
        colU = "azul"
    elif int(colU) == 7:
        colU = "violeta"
    elif int(colU) == 8:
        colU = "gris"
    elif int(colU) == 9:
        colU = "blanco"

    if int(colD) == 0:
        colD = "negro"
    elif int(colD) == 1:
        colD = "cafe"
    elif int(colD) == 2:
        colD = "rojo"
    elif int(colD) == 3:
        colD = "naranja"
    elif int(colD) == 4:
        colD = "amarillo"
    elif int(colD) == 5:
        colD = "verde"
    elif int(colD) == 6:
        colD = "azul"
    elif int(colD) == 7:
        colD = "violeta"
    elif int(colD) == 8:
        colD = "gris"
    elif int(colD) == 9:
        colD = "blanco"

    if int(colT) == 0:
        colT = "negro"
    elif int(colT) == 1:
        colT = "cafe"
    elif int(colT) == 2:
        colT = "rojo"
    elif int(colT) == 3:
        colT = "naranja"
    elif int(colT) == 4:
        colT = "amarillo"
    elif int(colT) == 5:
        colT = "verde"
    elif int(colT) == 6:
        colT = "azul"
    elif int(colT) == 7:
        colT = "violeta"
    elif int(colT) == 8:
        colT = "gris"
    elif int(colT) == 9:
        colT = "blanco"

    if float(tol) == 0.05:
        tol = '5%'
        colTol = 'dorado'
    elif float(tol) == 0.10:
        tol = '10%'
        colTol = 'plata'

    return render_template("resistenciaFormulario.html", form=resi_form, colU=colU, colD=colD, colT=colT, colTol=colTol, tol=tol, val=val, valMax=valMax, valMin=valMin)


if __name__ == '__main__':
    app.run(debug=True)
