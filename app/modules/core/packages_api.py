from flask.ext.restful import Resource, reqparse, fields, marshal
from app import app, api, db, modules
from flask.views import MethodView
from app.modules.core.system import System
from app.models import Packages

s = System()
system = [
    {
        'name': u'operating_system',
        'value': u'{0}'.format(s.getOperatingSystem()),
    },
    {
        'name': u'kernel',
        'value': u'{0}'.format(s.getKernelRelease()),
    }
]
package_fields = {
    'name': fields.String,
    'value': fields.String,
    'uri': fields.Url('package')
}

class PackageAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name',
                                   type=str,
                                   location='json',
                                   )
        self.reqparse.add_argument('value',
                                   type=str,
                                   location='json',
                                   )
        super(PackageAPI, self).__init__()

    def get(self, name):
        s = Packages.query.filter_by(name=name).first()
        return { 'package': marshal(s, package_fields) }

    def put(self, name):
        args = self.reqparse.parse_args()
        data = {
            'name' : name,
            'value' : args['value'],
        }
        print data
        s = Packages.query.filter_by(name=name).first()
        s.value = args['value']
        db.session.commit()
        return {'package': marshal(data, package_fields)}, 201

    def delete(self):
        pass

class PackageListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name',
                                   type=str,
                                   required=True,
                                   help="name of system variable required",
                                   location='json',
                                   )
        self.reqparse.add_argument('value',
                                   type=str,
                                   help="data of system variable required",
                                   location='json',
                                   )
        super(PackageListAPI, self).__init__()

    def get(self):
        s = Packages.query.all()
        return { 'package': map(lambda t: marshal(t, package_fields), s) }

    def post(self):
        args = self.reqparse.parse_args()
        data = {
            'name' : args['name'],
        }
        insert = Packages(name=args['name'])
        db.session.add(insert)
        db.session.commit()
        return {'package': marshal(data, package_fields)}, 201

api.add_resource(PackageAPI, '/api/v1.0/packages/<name>', endpoint='package')
api.add_resource(PackageListAPI, '/api/v1.0/packages', endpoint='packages')
