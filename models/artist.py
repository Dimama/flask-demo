from sqlalchemy import Column, Integer, String

from models import Base


class Artist(Base):

    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    founding_date = Column(String, nullable=True)
    country = Column(String, nullable=True)

    def to_json(self):
        return {"id": self.id,
                "name": self.name,
                "genre": self.genre,
                "founding_date": self.founding_date,
                "country": self.country}
