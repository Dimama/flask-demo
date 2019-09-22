from http import HTTPStatus

from flask_restful import Resource, reqparse
from flask import current_app, request

from db_wrapper import ArtistNotFoundException


class Track(Resource):

    post_parser = reqparse.RequestParser()
    post_parser.add_argument("name", type=str, required=True, location="json")
    post_parser.add_argument("artist", type=int, required=True, location="json")
    post_parser.add_argument("release_date", type=str, required=False, location="json")
    post_parser.add_argument("duration", type=int, required=False, location="json")
    post_parser.add_argument("language", type=str, required=False, location="json")
    post_parser.add_argument("text", type=str, required=False, location="json")

    def get(self, track_id: int):
        track = current_app.db_wrapper.get_track(track_id)
        if track is None:
            return {"Message": f"track <{track_id}> not found"}, HTTPStatus.NOT_FOUND

        return {"Track": track}, HTTPStatus.OK

    def post(self):
        current_app.logger.debug(request.data)

        track = self.post_parser.parse_args()
        try:
            musician_id = current_app.db_wrapper.add_track(**track)
        except ArtistNotFoundException:
            return {"message": "incorrect artist"}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            current_app.logger.error(e)
            return {"message": "server error"}, HTTPStatus.INTERNAL_SERVER_ERROR

        return {"message": f"Track with id<{musician_id}> created"}, HTTPStatus.CREATED

    def delete(self, track_id):
        track = current_app.db_wrapper.delete_track(track_id)
        if track is None:
            return {"Message": f"artist <{track_id}> not found"}, HTTPStatus.NOT_FOUND

        return {}, HTTPStatus.NO_CONTENT

