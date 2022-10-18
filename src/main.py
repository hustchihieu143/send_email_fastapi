import sys
sys.path.insert(0,'/home/chihieu/project_web/sendmail_fastapi/')
from fastapi import FastAPI
from src.routes.email import email_router

app = FastAPI()
  
app.include_router(email_router)

