from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    operations = request.form["operation"]
    if operations == "+":
        res = num1 + num2
    elif operations == "-":
        res = num1 - num2
    elif operations == "*":
        res = num1 * num2
    elif operations == "/":
        res = num1 / num2
    else:
        res = "Invalid Operation Chosen"
 
    return render_template("calculate.html", result=res)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
