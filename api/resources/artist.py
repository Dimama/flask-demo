from http import HTTPStatus

from flask_restful import Resource, reqparse
from flask import current_app, request, render_template, make_response


class Artist(Resource):

    post_parser = reqparse.RequestParser()
    post_parser.add_argument("name", type=str, required=True, location="json")
    post_parser.add_argument("genre", type=str, required=True, location="json")
    post_parser.add_argument("founding_date", type=str, required=False, location="json")
    post_parser.add_argument("country", type=str, required=False, location="json")

    def get(self, artist_id: int = None):
        if artist_id is None:
            artists = current_app.db_wrapper.get_artists()
            # server rendering
            return make_response(render_template("artists.html", title="ARTISTS", artists=artists),
                                 HTTPStatus.OK,
                                 {'Content-Type': 'text/html'})

        artist = current_app.db_wrapper.get_artist(artist_id)
        if artist is None:
            return {"Message": f"artist <{artist_id}> not found"}, HTTPStatus.NOT_FOUND

        return {"Artist": artist}, HTTPStatus.OK

    def post(self):
        current_app.logger.debug(request.data)

        artist = self.post_parser.parse_args()
        try:
            artist_id = current_app.db_wrapper.add_artist(**artist)
        except Exception as e:
            current_app.logger.error(e)
            return {"message": "server error"}, HTTPStatus.INTERNAL_SERVER_ERROR

        return {"artist": f"Artist with id<{artist_id}> created"}, HTTPStatus.CREATED

    def delete(self, artist_id):
        artist = current_app.db_wrapper.delete_artist(artist_id)
        if artist is None:
            return {"Message": f"artist <{artist_id}> not found"}, HTTPStatus.NOT_FOUND

        return {}, HTTPStatus.NO_CONTENT

