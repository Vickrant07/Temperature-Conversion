from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField, FloatField
from wtforms.validators import InputRequired, NumberRange

class ShiftForm(FlaskForm):
    plaintext = StringField("Plaintext", validators=[InputRequired()])

    shift = IntegerField("Shift", validators=[InputRequired(), NumberRange(1, 25)])
    
    ciphertext = StringField("Ciphertext")
    submit = SubmitField("Submit")

class ConversionForm(FlaskForm):
    input = RadioField("From:", choices = ["Fahrenheit", "Celsius", "Kelvin"], default = "Fahrenheit")
    input_field= IntegerField(validators=[InputRequired()])

    output = RadioField("To:", choices= ["Fahrenheit","Celsius","Kelvin"], default= "Celsius")
    outcome= FloatField("Outcome:")
    submit = SubmitField("Submit")