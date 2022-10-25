from fastapi import APIRouter
from os.path import join, dirname
from dotenv import load_dotenv
from src.service.email import EmailService
from src.service.email_data import EmailDataService
import random
import string

from sqlalchemy.orm.session import Session
from fastapi.params import Depends
from src.dependencies import get_db_session
from src.models.emails import Email

from smtp_client import send_email
from smtp_server import SMTPServer

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

def get_email_service(session: Session = Depends(get_db_session)):
    return EmailService(session)

def get_email_data_service(session: Session = Depends(get_db_session)):
    return EmailDataService(session)

email_router = APIRouter()

@email_router.get("/email/{id}")
async def get_email_by_id(id: int, email_service: EmailService = Depends(get_email_service)):
  user = await email_service.find_one(id)
  return user

@email_router.get("/email")
async def get_email_all(email_service: EmailService = Depends(get_email_service)):
  user = await email_service.find_all()
  return user

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

@email_router.post("/")
async def random_email_func(email_service: EmailService = Depends(get_email_service)):
    email_rand = random_char(8)+"@gmail.com"
    data = await email_service.create(email_rand)
    return data
    

@email_router.post("/email")
async def create_email(name: str, email_service: EmailService = Depends(get_email_service)):
  user = await email_service.create(name)
  return user

@email_router.post('/send_email_server')
async def email_test(sender: str, receiver: str, content: str, email_service: EmailService = Depends(get_email_service), email_data_service: EmailDataService = Depends(get_email_data_service)):
  server = SMTPServer()
  server.start()
  try:
    send_email(sender, receiver, content)
    email = await email_service.find_by_email(receiver)
    if email:
      await email_data_service.create(email.id, sender, content)
      
  finally:
    server.stop()
  return 'OK'


@email_router.get('/inbox')
async def get_inbox(email: str, email_data_service: EmailDataService = Depends(get_email_data_service)):
  return await email_data_service.get_data_by_email(email)


