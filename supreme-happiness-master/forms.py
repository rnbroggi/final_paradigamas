from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, ValidationError
from wtforms.validators import Required


class LoginForm(FlaskForm):
    usuario = StringField('Nombre de usuario', validators=[Required()])
    password = PasswordField('Contraseña', validators=[Required()])
    enviar = SubmitField('Ingresar')


class SaludarForm(FlaskForm):
    usuario = StringField('Nombre: ', validators=[Required()])
    enviar = SubmitField('Saludar')


class RegistrarForm(LoginForm):
    password_check = PasswordField('Verificar Contraseña', validators=[Required()])
    enviar = SubmitField('Registrarse')

class BuscarForm(FlaskForm):
    nombre = StringField('Buscar: ', [validators.Length(min=3)])
    enviar = SubmitField('Buscar')

def validate_codigo(form, field):
    parte_alfabetica = field.data[slice(0,3)].upper()
    chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    primera_validacion = True
    segunda_validacion = True

    for letra in parte_alfabetica:
        if letra not in chars:
            primera_validacion = False

    try:
        parte_numerica = int(field.data[slice(3,6)])

        if parte_numerica < 100:
            parte_numerica += 100

        if len(str(parte_numerica)) != 3:
            segunda_validacion = False

    except:
        segunda_validacion = False

    if len(field.data) != 6 or not primera_validacion  or not segunda_validacion:
        raise ValidationError('El codigo debe ser de 6 caracteres: Tres letras y luego tres digitos')

def validate_cantidad(form, field):
    try:
        field.data = int(field.data)
    except ValueError:
        raise ValidationError('Este campo solo puede tener un numero entero')

def validate_precio(form, field):
    try:
        if '.' not in field.data :
            raise ValidationError('Este campo solo puede tener un numero decimal')
        field.data  = float(field.data)
    except ValueError:
        raise ValidationError('Este campo solo puede tener un numero decimal')


class AgregarForm(FlaskForm):
    codigo = StringField('Codigo: ', [validators.Required(), validate_codigo])
    producto = StringField('Producto: ', validators=[Required()])
    cliente = StringField('Cliente: ', validators=[Required()])
    cantidad = StringField('Cantidad: ', validators=[Required(), validate_cantidad])
    precio = StringField('Precio: ', validators=[Required(), validate_precio])
    enviar = SubmitField('Agregar')
