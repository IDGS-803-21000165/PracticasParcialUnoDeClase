from flask import Flask, render_template, request
import FormulaDistancia as fm
from math import sqrt

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
