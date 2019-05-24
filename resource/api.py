from flask import request, current_app
from flask_restful import Resource, abort
from mailtester import api
import scraper


class CheckMail(Resource):

    def get(self):
        email = request.args.get('email')
        api_key = request.args.get('api_key')
        if api_key != current_app.config.get('API_KEY'):
            return dict(status=False, message="Invalid Api key")
        result = scraper.scrape(email)
        return result

api.add_resource(CheckMail, '/api/checkmail')
