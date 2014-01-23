from flask.ext.restful import Resource, reqparse, fields, marshal
from app import app, api, db, modules
from flask.views import MethodView
from app.modules.core.system import System
from app.models import System as sys

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
system_fields = {
    'name': fields.String,
    'value': fields.String,
    'uri': fields.Url('system')
}

class SystemAPI(Resource):
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
        super(SystemAPI, self).__init__()

    def get(self, name):
        s = sys.query.filter_by(name=name).first()
        return { 'system': marshal(s, system_fields) }

    def put(self, name):
        args = self.reqparse.parse_args()
        data = {
            'name' : name,
            'value' : args['value'],
        }
        print data
        s = sys.query.filter_by(name=name).first()
        s.value = args['value']
        db.session.commit()
        return {'system': marshal(data, system_fields)}, 201

    def delete(self):
        pass

class SystemListAPI(Resource):
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
                                   required=True,
                                   help="data of system variable required",
                                   location='json',
                                   )
        super(SystemListAPI, self).__init__()

    def get(self):
        s = sys.query.all()
        return { 'system': map(lambda t: marshal(t, system_fields), s) }

    def post(self):
        args = self.reqparse.parse_args()
        data = {
            'name' : args['name'],
            'value' : args['value'],
        }
        insert = sys(name=args['name'],
                     value=args['value'])
        db.session.add(insert)
        db.session.commit()
        return {'system': marshal(data, system_fields)}, 201

api.add_resource(SystemAPI, '/api/v1.0/systems/<name>', endpoint='system')
api.add_resource(SystemListAPI, '/api/v1.0/systems', endpoint='systems')
