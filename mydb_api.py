from flask_restplus import Namespace, Resource
from app_db import get_db_handler

ns_mydb = Namespace("mydb", description='Methods for mydb')

HANDLER_DB = get_db_handler()


# TODO: add here resources for personalized requests
@ns_mydb.route("/test")
@ns_mydb.response(200, 'OK')
class Test(Resource):
    def get(self):
        return {"message": "This is a test"}, 200
