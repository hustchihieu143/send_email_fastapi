from fastapi import APIRouter
from os.path import join, dirname
from dotenv import load_dotenv
from src.service.email import EmailService

from sqlalchemy.orm.session import Session
from fastapi.params import Depends
from src.dependencies import get_db_session
from src.models.emails import Email

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

def get_email_service(session: Session = Depends(get_db_session)):
    return EmailService(session)

email_router = APIRouter()

@email_router.get("/email/{id}")
async def get_email_by_id(id: int, email_service: EmailService = Depends(get_email_service)):
  user = await email_service.find_one(id)
  return user

@email_router.get("/email")
async def get_email_all(email_service: EmailService = Depends(get_email_service)):
  user = await email_service.find_all()
  return user

@email_router.post("/email")
async def create_email(name: str, email_service: EmailService = Depends(get_email_service)):
  user = await email_service.create(name)
  return user


