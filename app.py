from flask import Flask, render_template
from forms import ConversionForm, ShiftForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"

@app.route("/shift", methods=["GET", "POST"])
def shift():
    form = ShiftForm()
    
    ciphertext = ""
    if form.validate_on_submit():
        plaintext = form.plaintext.data
        shift = form.shift.data

        for char in plaintext:
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                ciphertext += char

    form.ciphertext.data = ciphertext
    return render_template("shift_form.html", title="Caesar shift cipher", form=form)

@app.route("/conversion", methods=["GET", "POST"])
def conversion():
    form = ConversionForm()
    if form.validate_on_submit():
        input= form.input.data
        output= form.output.data
        input_field= form.input_field.data

        if input == "Fahrenheit" and output == "Fahrenheit":
            outcome= input_field
        elif input == "Fahrenheit" and output == "Celsius":
            outcome = 5/9*(input_field-32)
        elif input == "Fahrenheit" and output == "Kelvin":
            outcome = 5/9*(input_field-32)+273
        elif input == "Celsius" and output == "Celsius":
            outcome= input_field
        elif input == "Celsius" and output == "Fahrenheit":
            outcome = 9/5*input_field+32
        elif input == "Celsius" and output == "Kelvin":
            outcome = input_field+273
        elif input == "Kelvin" and output == "Kelvin":
            outcome= input_field
        elif input == "Kelvin" and output == "Fahrenheit":
            outcome = 5/9*(input_field-273)+32
        elif input == "Kelvin" and output == "Celsius":
            outcome = input_field-273

        form.outcome.data = outcome
    return render_template("conversion_form.html",title="How Cool is Flask?", form=form)