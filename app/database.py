from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine
from app.config import config

db_url = f"{config.db_dialect}://{config.db_user}:{config.db_password}@{config.db_host}:{config.db_port}/{config.db_name}"
engine = create_engine(db_url, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

SessionDependency = Annotated[Session, Depends(get_session)]

