from flask import render_template, flash, redirect, session, url_for, Blueprint
from app import app, db, modules
from app.modules.core.api import GlobalApi
from app.modules.core.system import System
from app.modules.core.resources import Resources
from app.modules.install.forms.form import LAMP
import requests
import json

mod = Blueprint('install', __name__)
@mod.route('/install', methods = ['GET', 'POST'])
def index():
    s = System()
    r = Resources()
    api = GlobalApi()
    ip_addr = []
    system = {"title": [{'system': 
                            [{'name': 'hostname', 'value': s.getHostname()},
                             {'name': 'operating_system', 'value': s.getOperatingSystem()},
                             {'name': 'kernel_version', 'value': s.getKernelRelease()},
                             ]
                        }]
              }
    ip_addresses = {"title": [{"ip_addresses":
                                    ip_addr
                              }]
                    }
    disk = {"title": [{'disk_usage': 
                         [{'name': 'used', 'value': r.disk_usage.used / 1024 / 1024, 'path': r.path},
                          {'name': 'free', 'value': r.disk_usage.free / 1024 / 1024, 'path': r.path},
                          {'name': 'total', 'value': r.disk_usage.total / 1024 / 1024, 'path': r.path},
                          {'name': 'percent', 'value': r.disk_usage.percent, 'path': r.path},
                          ]
                      }]
           }

    memory = {"title": [{'ram_usage': 
                            [{'name': 'used', 'value': r.ram_usage.used / 1024 / 1024},
                             {'name': 'free', 'value': r.ram_usage.free / 1024 / 1024},
                             {'name': 'total', 'value': r.ram_usage.total / 1024 / 1024},
                             {'name': 'percent', 'value': r.ram_usage.percent},
                             ]
                        }]
             }
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
    lamp = LAMP()
    relist = []
    endlist = []
    packlist = []
    for ip in s.getIps():
        ip_addr.append({"name": "ip_address", "value":ip})
    api.post("resources", ip_addresses)
    api.post("systems", system)
    api.post("resources", disk)
    api.post("resources", memory)
    if lamp.validate_on_submit():
#        #for x in lamp:
#        #    if x.id != "csrf_token":
#        #        for name in x.data:
#        #            packlist.append({'name':name})
#
#        for name, value in system.iteritems():
#            endlist.append({'name':name, 'value':value})
#        
#        for name, value in disk.iteritems():
#            relist.append({'name':name, 'value':value})
#
#        for name, value in memory.iteritems():
#            relist.append({'name':name, 'value':value})
#
#        for item in endlist:
#            print item
#            api.post('systems', item)
#        for item in relist:
#            api.post('resources', item)
#        for item in packlist:
#            api.post('packages', item)

        return redirect("/index")

    return render_template("install/template/index.html",
        title = 'install',
        systems = api.get_all("systems"),
        disk = api.get_all("resources"),
        resources = api.get_all("resources"),
        view_more = view_more,
        lamp = lamp
        )

app.register_blueprint(mod)
