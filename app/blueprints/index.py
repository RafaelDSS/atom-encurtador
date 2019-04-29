from flask import Blueprint, redirect, render_template, request, flash, url_for
from app.models.forms import EntryEncurt
from app.models.tables import Url
from app.ext.db import db

app_encurtador = Blueprint('encurtador', __name__)

# View de registro da url.


@app_encurtador.route('/', methods=['GET', 'POST'])
def home():
    url_origem = None
    form = EntryEncurt(request.form)
    if form.validate_on_submit():
        url = Url.query.filter(Url.url_origem == form.url_origem.data).first()
        if not url:
            url_origem = form.url_origem.data
            url_destino = form.url_destino.data
            url = Url(url_destino, url_origem)
            db.session.add(url)
            db.session.commit()
            url_origem = url_for('encurtador.url_redirect',
                                 slogan=url_origem, _external=True)
    return render_template('index.html', form=form, link=url_origem)

# View de redirecionamento.


@app_encurtador.route('/d/<slogan>')
def url_redirect(slogan=None):
    if slogan:
        url = Url.query.filter_by(url_origem=slogan).first()
        if url:
            return redirect(url.url_destino)
        else:
            flash("Essa url não existe.")
    return redirect('/')


def configure(app):
    app.register_blueprint(app_encurtador)
