import enum

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    is_banned = Column(Boolean, default=False)
    bears = relationship("Bear", back_populates="owner")


class Species(enum.Enum):
    black = "black"
    brown = "brown"
    panda = "panda"
    polar = "polar"
    sloth = "sloth"
    spectacled = "spectacled"
    sun = "sun"


class Bear(Base):
    __tablename__ = "bears"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    species = Column(Enum(Species))
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="bears")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species.value,
            "owner": self.owner.email if self.owner else "",
        }
