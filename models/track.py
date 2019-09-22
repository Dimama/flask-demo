from sqlalchemy import Column, Integer, String, ForeignKey

from models import Base


class Track(Base):

    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    artist = Column(Integer, ForeignKey("artists.id"), nullable=False)
    release_date = Column(String, nullable=True)
    duration = Column(Integer, nullable=True)
    language = Column(String, nullable=True)
    text = Column(String, nullable=True)

    def to_json(self):
        return {"id": self.id,
                "name": self.name,
                "artist": self.artist,
                "release_date": self.release_date,
                "duration": self.duration,
                "language": self.language,
                "text": self.text}
