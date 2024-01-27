from flask import Flask, render_template, request

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
