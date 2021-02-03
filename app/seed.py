from sqlalchemy.orm import Session

from app.crud import create_bear, create_user
from app.models import Species
from app.schemas import BearBase, UserBase


def seed_db(db: Session):
    agnes = create_user(db, UserBase(email="agnes@example.com"))
    brynn = create_user(db, UserBase(email="brynn@example.com"))
    carli = create_user(db, UserBase(email="carli@example.com"))

    create_bear(db, BearBase(name="Baloo", species=Species.sloth), agnes)
    create_bear(db, BearBase(name="Boo-Boo", species=Species.brown), brynn)
    create_bear(db, BearBase(name="Cindy", species=Species.brown), carli)
    create_bear(db, BearBase(name="Hei Bai", species=Species.panda), agnes)
    create_bear(db, BearBase(name="Honey", species=Species.sun), brynn)
    create_bear(db, BearBase(name="Jake", species=Species.polar), carli)
    create_bear(db, BearBase(name="Kit Cloudkicker", species=Species.brown), agnes)
    create_bear(db, BearBase(name="Mor'du", species=Species.black), brynn)
    create_bear(db, BearBase(name="Paddington", species=Species.spectacled), carli)
    create_bear(db, BearBase(name="Panny", species=Species.panda), agnes)
    create_bear(db, BearBase(name="PapaPanda", species=Species.panda), brynn)
    create_bear(db, BearBase(name="Po", species=Species.panda), carli)
    create_bear(db, BearBase(name="Smokey", species=Species.black), agnes)
    create_bear(db, BearBase(name="Yogi", species=Species.brown), brynn)
