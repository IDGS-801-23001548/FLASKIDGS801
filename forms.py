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

    apellidos = StringField("apaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])

    email = EmailField("correo", [
        validators.Email(message="Ingresa un correo valido")
    ])
    
    telefono = IntegerField("telefono", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=20, message="Ingrese valor valido")
    ])