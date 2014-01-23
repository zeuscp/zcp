from flask import jsonify
from flask.ext.restful import Resource, reqparse, fields, marshal
from app import app, api, db, modules
from flask.views import MethodView
#from app.modules.core.system import System
#from app.models import System as sys
from app.models import Endpoint, EndpointData
import json
import ast

system_fields = {
    'name': fields.String,
    'value': fields.String,
    'uri': fields.Url('system')
}

#class SystemAPI(Resource):
#    def __init__(self):
#        self.reqparse = reqparse.RequestParser()
#        self.reqparse.add_argument('name',
#                                   type=str,
#                                   location='json',
#                                   )
#        self.reqparse.add_argument('value',
#                                   type=str,
#                                   location='json',
#                                   )
#        super(SystemAPI, self).__init__()
#
#    def get(self, name):
#        s = sys.query.filter_by(name=name).first()
#        return { 'system': marshal(s, system_fields) }
#
#    def put(self, name):
#        args = self.reqparse.parse_args()
#        data = {
#            'name' : name,
#            'value' : args['value'],
#        }
#        print data
#        s = sys.query.filter_by(name=name).first()
#        s.value = args['value']
#        db.session.commit()
#        return {'system': marshal(data, system_fields)}, 201
#
#    def delete(self):
#        pass

class ListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("endpoint",
                                   type=str,
                                   help="name of system variable required",
                                   location='json',
                                   )
        self.reqparse.add_argument("title",
                                   type=str,
                                   help="name of system variable required",
                                   location='json',
                                   )
        self.reqparse.add_argument('value',
                                   type=str,
                                   help="data of system variable required",
                                   location='json',
                                   )
        super(ListAPI, self).__init__()

#$  curl -i -H "Content-Type: application/json" -X POST -d '{"endpoint":{"systems": [{"system": [{"name": "kernel", "value": "213as3.ea23.as"}, {"name": "operating_system", "value": "CentOS 6.4"}, {"name": "hostname", "value": "zeuscp_dev"}]}]}}' http://23.253.71.150:8182/api/v1.0/systems

    def get(self, end_point):
        endpoints = []
        titles = {}
        data_path = {}
        data_dict = {}
        data_list = []
        ep = Endpoint.query.filter_by(name=end_point).first()
        data = ep.data.all()
        for x in data:
            
            if x.path:
                if not x.title in titles:
                    titles[x.title] = data_path
                if not x.path in data_path:
                    data_path[x.path] = data_dict
                data_dict[x.name] = x.value
        for x in data:
            if not x.path:
                if not x.title in titles:
                    data_dict = {}
                    data_list = []
                    titles[x.title] = data_dict
                if not x.name in data_dict:
                    data_dict[x.name] = x.value
                else:
                    if isinstance(titles[x.title], list):
                        data_list.append({x.name:x.value})
                    else:
                        data_list = []
                        data_list.append({x.name:x.value})
                        titles[x.title] = data_list
        endpoints.append(titles)
        return jsonify(endpoints[0])

    def post(self, end_point):
        args = self.reqparse.parse_args()
        print end_point
        #try:
        #    Endpoint.query.filter_by(name=end_point).count()
        #except:
        #    pass
        if not db.session.query(Endpoint).filter_by(name=end_point).count():
            print 'ha'
            q = Endpoint(name=end_point)
            db.session.add(q)
            print db.session.commit()
        if args['endpoint']:
            data = ast.literal_eval(args['endpoint'])
        if args['title']:
            args['endpoint'] = {end_point:ast.literal_eval(args['title'])}
            args['title'] = None
            data = args['endpoint']
        for ep in data:
            get_endpoint = Endpoint.query.filter_by(name=ep).first()
            for data_points in data[ep]:
                for data_point in data_points:
                    for entity in data_points[data_point]:
                        if 'path' in entity:
                            insert = EndpointData(title=data_point,
                                                  name=entity['name'],
                                                  value=entity['value'],
                                                  path=entity['path'],
                                                  endpoint=get_endpoint,
                                                  )
                        else:
                            insert = EndpointData(title=data_point,
                                                  name=entity['name'],
                                                  value=entity['value'],
                                                  endpoint=get_endpoint,
                                                  )
                        db.session.add(insert)
                        db.session.commit()
        return data

class ListAllAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("endpoint",
                                   type=str,
                                   help="name of system variable required",
                                   location='json',
                                   )
        super(ListAllAPI, self).__init__()

    def get(self):
        endpoint_data = {}
        endpoint_data['endpoint'] = []
        ep_list = {}
        title = {}
        for ep in Endpoint.query.all():
            for e in Endpoint.query.filter_by(name=ep.name):
                dat = e.data.all()
                for d in dat:
                    if not d.endpoint.name in ep_list:
                        ep_list[d.endpoint.name] = []
                    if not d.title in title:
                        title[d.title] = []
                    title[d.title].append({'name':d.name,'value':d.value})
                    ep_list[d.endpoint.name] = title
                title = {}
        endpoint_data['endpoint'].append(ep_list)
        return jsonify(endpoint_data)

    def post(self):
        args = self.reqparse.parse_args()
        if args['endpoint']:
            data = ast.literal_eval(args['endpoint'])
        if args['title']:
            args['endpoint'] = {end_point:ast.literal_eval(args['title'])}
            args['title'] = None
            data = args['endpoint']
        for ep in data:
            get_endpoint = Endpoint.query.filter_by(name=ep).first()
            for data_points in data[ep]:
                for data_point in data_points:
                    for entity in data_points[data_point]:
                        insert = EndpointData(title=data_point,
                                              name=entity['name'],
                                              value=entity['value'],
                                              endpoint=get_endpoint
                                              )
                        db.session.add(insert)
                        db.session.commit()
        return data

#api.add_resource(SystemAPI, '/api/v1.0/<endpoint>/<name>', endpoint='<endpoint>')
api.add_resource(ListAPI, '/api/v1.0/<end_point>', endpoint='<end_point>')
api.add_resource(ListAllAPI, '/api/v1.0/')
