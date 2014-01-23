from flask import render_template, flash, redirect, session, url_for, Blueprint
from app import app, db, modules
from app.modules.sample_tempalte.main import SampleTemplate


mod = Blueprint('template', __name__)
@mod.route('/template', methods = ['GET', 'POST'])
def template():
    sp = SampleTemplate('booming')
    return render_template("sample_template/template/index.html",
        title = 'Sample Template',
        message=sp.yell("Git some sucka!"),
        alert='This is a sampled alert',
        )

app.register_blueprint(mod)
