from src.database import DBSession
from sqlalchemy.orm.session import Session


async def get_db_session() -> Session:
    try:
        db = DBSession()
        yield db
    finally:
        db.close()
