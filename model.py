from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    is_sent = Column(Boolean, default=False)
