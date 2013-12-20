from flask import render_template, flash, redirect, session, url_for, Blueprint
from app import app, db, modules
from app.modules.overview.main import Overview


mod = Blueprint('overview', __name__)
@mod.route('/', methods = ['GET', 'POST'])
@mod.route('/index', methods = ['GET', 'POST'])
def index():
    o = Overview()
    system = {'Hostname': o.getHostname(),
              'IP Address(es)': o.getIps(),
              'Operating System': o.getOs(),
              'Kernel Version': o.getKernel(),
            }
    graph = {'Disk Usage - Used | Total': {'used': o.getDiskUsed(),
                                           'free': o.getDiskFree(),
                                           'total': o.getDiskTotal(),
                                           'percent': o.getDiskPercent(),
                                          },
             'RAM Usage - Used | Total': {'used': o.getRamUsed(),
                                          'free': o.getRamFree(),
                                          'total': o.getRamTotal(),
                                          'percent': o.getRamPercent(),
                                         },
            },
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

    return render_template("overview/template/index.html",
        title = 'Overview',
        system = system,
        services = services,
        graph = graph,
        view_more = view_more,
        )

