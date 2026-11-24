from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import Mapped,mapped_column
from database import Base

# blog table
class Blog(Base):
    __tablename__="blogs"

    id :Mapped[int] = mapped_column(Integer,primary_key=True, index=True)
    title :Mapped[str] = mapped_column(String)
    content :Mapped[str] = mapped_column(String)