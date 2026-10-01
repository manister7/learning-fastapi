from sqlalchemy import String 
from sqlalchemy.orm import Mapped, mapped_column 
 
from .database import Base 
 
 
class Student(Base): 
    __tablename__ = "students" 
 
    id: Mapped[int] = mapped_column( 
        primary_key=True, 
        autoincrement=True 
    ) 
 
    name: Mapped[str] = mapped_column(String(100)) 
 
    email: Mapped[str] = mapped_column( 
        String(150), 
        unique=True, 
        index=True 
    ) 
 
    course: Mapped[str] = mapped_column(String(100)) 