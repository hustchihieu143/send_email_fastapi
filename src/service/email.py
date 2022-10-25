from sqlalchemy.orm.session import Session
from src.models.emails import Email


class EmailService():
      def __init__(self, session: Session) -> None:
            self.session = session
  
      async def find_one(self, id: int):
            return self.session.query(Email).filter_by(id=id).first()

      async def find_all(self):
            return self.session.query(Email).all()

      async def find_by_email(self, email):
            return self.session.query(Email).filter_by(name=email).first()

      async def create(self, name):
            email = Email()
            email.name = name
            self.session.add(email)
            self.session.commit()


      
  
