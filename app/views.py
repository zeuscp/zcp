from flask import render_template, flash, redirect, session, url_for, jsonify, request, abort, make_response
from flask.ext.restful import Resource, reqparse, fields, marshal
from app import app, api, db, modules
from flask.views import MethodView
#from models import User

from app.modules.core.system import System
from app.modules.core import core_api #system_api, packages_api, resources_api


#from app.modules.domain.view import mod as domain
#from app.modules.database.view import mod as database
#from app.modules.user.view import mod as user
#from app.modules.system.main import System
#from app.modules.overview.view import mod as overview
#from app.modules.install.view import mod as install
from app.modules.install import view
from app.modules.overview import view

#app.register_blueprint(overview)
#app.register_blueprint(user)
#app.register_blueprint(database)
#app.register_blueprint(install)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("sb-admin/404.html"), 404
