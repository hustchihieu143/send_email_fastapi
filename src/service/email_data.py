from sqlalchemy.orm.session import Session
from src.models.email_data import Email_Data
from src.models.emails import Email


class EmailDataService():
      def __init__(self, session: Session) -> None:
            self.session = session

      async def create(self, receiver_id, sender, content):
            email_data = Email_Data()
            email_data.receiver_id = receiver_id
            email_data.sender = sender
            email_data.content = content
            self.session.add(email_data)
            self.session.commit()

      async def get_data_by_email(self, email):
        return self.session.query(Email_Data).join(Email, Email_Data.receiver_id == Email.id).filter(Email.name == email).all()



      
  
