from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    name = ''
    if request.method == 'POST' and 'username' in request.form and 'weight' in request.form:
        name = request.form.get('username')
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height)

    return render_template("bmi_calc.html",
                            name=name,
                            bmi=bmi)

def calc_bmi(weight, height):
    return round((weight / ((height/100) ** 2)), 2)


app.run()