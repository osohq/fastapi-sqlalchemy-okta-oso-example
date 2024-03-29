from typing import List, Optional

from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from okta_jwt.jwt import validate_token
from sqlalchemy.orm import Session, sessionmaker
from starlette.config import Config

from app.crud import create_bear, get_or_create_user_by_email, list_bears
from app.db import engine, setup_db
from app.models import User
from app.schemas import Bear, BearBase
from app.seed import seed_db

# Load environment variables.
conf = Config(".env")
issuer, audience, client_id = conf("ISSUER"), conf("AUDIENCE"), conf("CLIENT_ID")


def get_db():
    db = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    try:
        yield db
    finally:
        db.close()


def get_token(authorization: Optional[str] = Header(None)) -> str:
    if not authorization:
        raise HTTPException(403, "Missing 'Authorization' header.")
    try:
        return authorization.split()[1]
    except IndexError:
        raise HTTPException(403, "Malformed 'Authorization' header.")


def current_user(
    request: Request, token: str = Depends(get_token), db: Session = Depends(get_db)
):
    try:
        email = validate_token(token, issuer, audience, client_id)["sub"]
        request.state.user = get_or_create_user_by_email(db, email)
    except Exception as e:
        raise HTTPException(403, str(e))


# Reset and seed database.
setup_db()
seed_db(next(get_db()))

# Initialize application.
app = FastAPI(dependencies=[Depends(current_user)])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/bears", response_model=List[Bear])
def index(db: Session = Depends(get_db)):
    return list_bears(db)


@app.post("/bears", response_model=Bear)
def create(request: Request, bear: BearBase, db: Session = Depends(get_db)):
    return create_bear(db, bear, request.state.user)
