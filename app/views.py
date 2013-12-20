from flask import render_template, flash, redirect, session, url_for
from app import app, db, modules
from models import User
#from app.modules.domain.view import mod as domain
#from app.modules.database.view import mod as database
from app.modules.user.view import mod as user
#from app.modules.system.main import System
from app.modules.overview.view import mod as overview

app.register_blueprint(overview)
app.register_blueprint(user)
#app.register_blueprint(database)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("sb-admin/404.html"), 404
