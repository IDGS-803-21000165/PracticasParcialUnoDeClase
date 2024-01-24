from flask import Flask, render_template, request

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


if __name__ == '__main__':
    app.run(debug=True)
