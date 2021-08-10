#!/usr/bin/env python3
from flask import Flask, request, jsonify, json, abort
from flask_restful import Api, Resource, reqparse
from APIs import *
import  sys

envFile = 'env.json'

app = Flask(__name__)
api = Api(app)
list = []
with open(envFile) as f:
    data = json.load(f)
    hostname = data['stg']['hostname']
    organizations = data['stg']['organizations']
    environments = data['stg']['environments']


class get_list(Resource):
    def get(self):
        if request.endpoint == 'api_list':
            response = 'get the API list'
            return response
        elif request.endpoint == 'kvm_list':
            env = request.args.get('env')
            response = list_of_kvm(env)
            return response
        elif request.endpoint == 'list_kvm_size':
            env = request.args.get('env')
            listKVM = list_of_kvm(env)
            print(list.count(listKVM))
            for x in listKVM:
                if isinstance(x, str):
                    print('x : ',x)
                    kvm_individual = api_get_kvm_org(env, x)
                    value = (x , sys.getsizeof(kvm_individual))
                    # print('value', value)
                    list.append(value)
            response = list
            return response

class get_kvm_org(Resource):
    def get(self):
        env = request.args.get('env')
        kvm_name = request.args.get('kvmName')
        response = api_get_kvm_org(env, kvm_name)
        return response


api.add_resource(get_list, "/list_of_Apis", endpoint='api_list')
api.add_resource(get_list, "/list_of_kvm", endpoint='kvm_list')
api.add_resource(get_list, "/list_of_kvm_size", endpoint='list_kvm_size')
api.add_resource(get_kvm_org, "/get_kvm_org", endpoint='kvm')

if __name__ == "__main__":
    app.run(debug=True)
