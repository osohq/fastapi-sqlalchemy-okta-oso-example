from sqlalchemy.orm import Session

from app.models import Bear, User
from app.schemas import Bear as FormattedBear, BearBase, UserBase


def get_or_create_user_by_email(db: Session, email: str) -> User:
    user = db.query(User).filter(User.email == email).first()
    if user:
        return user
    return create_user(db, UserBase(email=email))


def create_user(db: Session, user: UserBase):
    db_user = User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def list_bears(db: Session):
    return [FormattedBear(**b.to_dict()) for b in db.query(Bear).all()]


def create_bear(db: Session, bear: BearBase, user: User):
    db_bear = Bear(**bear.dict(), owner_id=user.id)
    db.add(db_bear)
    db.commit()
    db.refresh(db_bear)
    return FormattedBear(**db_bear.to_dict())
