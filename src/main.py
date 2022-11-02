import sys
from os.path import join, dirname

forder = dirname(__file__)
sys.path.insert(0, forder)

from fastapi import FastAPI
from routes.email import email_router

app = FastAPI()


 
app.include_router(email_router)

@app.get("/")
def hello(): 
  return "hello update ci cd test"
