from flask.ext.restful import Resource, reqparse, fields, marshal
from app import app, api, db, modules
from flask.views import MethodView
from app.modules.core.system import System
from app.models import Resources

resource_fields = {
    'name': fields.String,
    'value': fields.String,
    'uri': fields.Url('resource')
}

class ResourceAPI(Resource):
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
        super(ResourceAPI, self).__init__()

    def get(self, name):
        s = sys.query.filter_by(name=name).first()
        return { 'resource': marshal(s, resource_fields) }

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
        return {'resource': marshal(data, resource_fields)}, 201

    def delete(self):
        pass

class ResourceListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name',
                                   type=str,
                                   required=True,
                                   help="name of resource variable required",
                                   location='json',
                                   )
        self.reqparse.add_argument('value',
                                   type=str,
                                   required=True,
                                   help="data of resource variable required",
                                   location='json',
                                   )
        super(ResourceListAPI, self).__init__()

    def get(self):
        s = Resources.query.all()
        return { 'resource': map(lambda t: marshal(t, resource_fields), s) }

    def post(self):
        args = self.reqparse.parse_args()
        data = {
            'name' : args['name'],
            'value' : args['value'],
        }
        insert = Resources(name=args['name'],
                     value=args['value'])
        db.session.add(insert)
        db.session.commit()
        return {'resource': marshal(data, resource_fields)}, 201

api.add_resource(ResourceAPI, '/api/v1.0/resources/<name>', endpoint='resource')
api.add_resource(ResourceListAPI, '/api/v1.0/resources', endpoint='resources')
