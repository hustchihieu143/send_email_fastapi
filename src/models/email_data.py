from sqlalchemy import Column, DateTime, TIMESTAMP, text
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import INTEGER, VARCHAR
from src.database import Base
import datetime



class Email_Data(Base):
    __tablename__ = "email_data"

    id = Column(INTEGER, primary_key=True, nullable=False)
    receiver_id = Column(INTEGER, autoincrement=True, nullable=False)
    sender = Column(VARCHAR(255), nullable=False)
    content = Column(VARCHAR(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
