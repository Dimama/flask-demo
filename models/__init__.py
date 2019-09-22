from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from .artist import Artist
from .track import Track
