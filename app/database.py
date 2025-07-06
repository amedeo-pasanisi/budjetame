from sqlmodel import create_engine
from app.config import config

db_url = f"{config.db_dialect}://{config.db_user}:{config.db_password}@{config.db_host}:{config.db_port}/{config.db_name}"
engine = create_engine(db_url, echo=True)
