import sys
from os.path import join, dirname
forder = join(dirname(__file__), './')
sys.path.insert(0, forder)

from fastapi import FastAPI
from src.routes.email import email_router

app = FastAPI()
  
app.include_router(email_router)

