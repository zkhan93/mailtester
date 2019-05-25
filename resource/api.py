from flask import request, current_app
from flask_restful import Resource, abort
from mailapi import api
import mailtester
import hunterio

class Fetch(Resource):

    def get(self):
        return {}

    def post(self):
        json_data = request.get_json(force=True)
        api_key = json_data.get('api_key')
        if api_key != current_app.config.get('API_KEY'):
            return dict(status=False, message="Invalid Api key")
        data = []
        for item in json_data.get('items'):
            res = {}
            res['input'] = item
            domain = item.get('domain')
            first = item.get('first')
            last = item.get('last')
            email_pattern = hunterio.fetch_email_pattern(domain)
            if email_pattern:
                res['email_pattern'] = email_pattern
            email = hunterio.fetch_email(domain, first, last)
            if email:
                res['email'] = email
                verify_email = mailtester.verify_email(email)
                if verify_email:
                    res['verify_email'] = verify_email
            data.append(res)
        return data

api.add_resource(Fetch, '/api/fetch/')
