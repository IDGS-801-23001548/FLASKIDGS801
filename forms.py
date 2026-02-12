from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField
from wtforms import validators
from wtforms.validators import ValidationError


class UserForm(FlaskForm):
    id = IntegerField("id", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=20, message="Ingrese valor valido")
    ])

    nombre = StringField("nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=3, max=10, message="Ingrese un nombre valido")
    ])

    apaterno = StringField("apaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])

    amaterno = StringField("amaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])

    correo = EmailField("correo", [
        validators.Email(message="Ingresa un correo valido")
    ])