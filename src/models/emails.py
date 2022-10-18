from sqlalchemy import Column, DateTime, TIMESTAMP, text
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import INTEGER, VARCHAR
from src.database import Base
import datetime



class Email(Base):
    __tablename__ = "emails"

    id = Column(INTEGER, primary_key=True, nullable=False)
    name = Column(VARCHAR(255), nullable=False, unique=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
