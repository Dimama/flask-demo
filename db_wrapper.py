from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from models import Base, Artist, Track


class DBWrapper:
    def __init__(self, db_host: str, db_port: int, database: str, db_user: str, db_password: str):
        # postgres
        self.engine = create_engine(f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{database}")

        # sqlite
        # self.engine = create_engine('sqlite:///flaskdemo.db')
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def get_artists(self):
        return [artist.to_json() for artist in self.session.query(Artist).all()]

    def get_artist(self, artist_id: int):
        artist = self.session.query(Artist).filter_by(id=artist_id).first()
        if artist is None:
            return None

        return artist.to_json()

    def add_artist(self, name: str, genre: str, founding_date: str = None, country: str = None):
        artist = Artist(name=name, genre=genre, founding_date=founding_date, country=country)
        self.session.add(artist)
        self.session.commit()

        return artist.id

    def delete_artist(self, artist_id: str):
        artist = self.session.query(Artist).filter_by(id=artist_id).first()
        if artist is None:
            return None

        tracks_to_delete = self.session.query(Track).filter_by(artist=artist_id).all()
        for track in tracks_to_delete:
            self.delete_track(track.id)

        result = artist.to_json()

        self.session.delete(artist)
        self.session.commit()

        return result

    def add_track(self,
                  name: str,
                  artist: int,
                  release_date: str = None,
                  duration: int = None,
                  language: str = None,
                  text: str = None):

        track = Track(name=name,
                      artist=artist,
                      release_date=release_date,
                      duration=duration,
                      language=language,
                      text=text)

        self.session.add(track)
        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise ArtistNotFoundException(f"Artist {artist} not found")

        return track.id

    def get_track(self, track_id: str):
        track = self.session.query(Track).filter_by(id=track_id).first()
        if track is None:
            return None

        return track.to_json()

    def delete_track(self, track_id: str):
        track = self.session.query(Track).filter_by(id=track_id).first()
        if track is None:
            return None

        result = track.to_json()

        self.session.delete(track)
        self.session.commit()

        return result


class ArtistNotFoundException(Exception):
    pass
