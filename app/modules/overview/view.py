from flask import render_template, flash, redirect, session, url_for, Blueprint
from app import app, db, modules
from app.modules.overview.main import Overview
from app.modules.core.api import GlobalApi


mod = Blueprint('overview', __name__)
@mod.route('/', methods = ['GET', 'POST'])
@mod.route('/index', methods = ['GET', 'POST'])
def index():
    api = GlobalApi()
    services = {'Web Service': 'httpd',
                'Database Service': 'MySQL',
               }
    view_more = {'Domains': {'number': 0,
                             'url': '/domains',
                            },
                 'Databases': {'number': 0,
                               'url': '/databases',
                              },
                 'Users': {'number': 0,
                           'url': '/users',
                          },
        }

    systems = api.get_all("systems")
    disk = api.get_all("resources")
    resources = api.get_all("resources")
    #print disk['value']
    #print type(disk)
    #for x in disk:
    #    print type(disk[x])
    #    for y in disk[x]:
    #        print y
    #        print type(y['name'])
    #        print type(y['value'])
    return render_template("overview/template/index.html",
        title = 'Overview',
        systems = systems,
        resources = resources,
        disk = disk,
        view_more = view_more,
        )

app.register_blueprint(mod)
