from http import HTTPStatus

from flask_restful import Resource


class Stub(Resource):

    def get(self):
        return {"Message": f"get stub"}, HTTPStatus.OK

    def post(self):
        return {"Message": "stub post"}, HTTPStatus.CREATED

    def delete(self):
        return {}, HTTPStatus.NO_CONTENT

