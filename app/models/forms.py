import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from app.models.tables import Url


class EntryEncurt(FlaskForm):
    url_origem = StringField('Nome pra seu novo link:', validators=[InputRequired(
        'Campo requerido.'), Length(max=30, message='Digite no maximo 20 caracteres.')])
    url_destino = StringField('Link a ser encurtado:', validators=[
                              InputRequired('Campo requerido.')])
    submit = SubmitField('Encurtar')

    def validate_url_origem(form, field):
        url = Url.query.filter_by(url_origem=field.data).first()
        if url:
            raise ValidationError('Este nome já está em uso, digite outro.')

    def validate_url_destino(form, field):
        if not re.fullmatch(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', field.data):
            raise ValidationError('Digite uma url válida.')
