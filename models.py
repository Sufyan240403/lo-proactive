from database import Base, engine
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Float

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String, unique=True, index=True)
    username =  Column(String)
    password = Column(String, nullable=False)
    role = Column(String, default="student")
    created_at = Column(DateTime, index=True)
    is_active = Column(Boolean, default =True)
    
class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer,primary_key=True,index=True)
    student_id = Column(Integer,ForeignKey("users.id"))
    lesson_type = Column(String, index=True)
    lesson_time = Column(String, index=True)
    lesson_date = Column(DateTime)
    status = Column(String, default = "pending")
    is_priority = Column(Boolean,  index= True)
    priority_fee = Column( Float, default=0.0)
    created_at = Column(DateTime,index= True)

class Package(Base):
    __tablename__ = "packages"
    id = Column(Integer,primary_key=True,index=True)
    description = Column(String, index = True)
    price = Column(Float, default= 0.0, index= True)
    num_lessons = Column(Integer, index=True)
    is_active = Column(Boolean, default=True)
    name = Column(String, index=True)

class StudentPackage(Base):
    __tablename__ = "Student_Packages"
    id = Column(Integer,primary_key=True,index=True)
    student_id = Column(Integer,ForeignKey("users.id"))    
    package_id = Column(Integer,ForeignKey("packages.id")) 
    purchased_at = Column(DateTime)
    lessons_remaining = Column(Integer)

class Progress(Base):
    __tablename__ = "progress"
    id = Column(Integer,primary_key=True,index=True)
    student_id = Column(Integer,ForeignKey("users.id"))
    note = Column(Text)
    lesson_number = Column(Integer, index=True)
    created_at = Column(DateTime)

class Video(Base):
    __tablename__ = "video"
    id = Column(Integer,primary_key=True,index=True)
    url = Column(String, index=True)
    title = Column(String,index=True)
    category = Column(String, default="tutorial")
    platform = Column(String, default="youtube", index=True)
    created_at= Column(DateTime, index=True)
    

class Gallery(Base):
    __tablename__ = "gallery"
    id = Column(Integer,primary_key=True,index=True)
    url = Column(String, index=True)
    caption=Column(String)
    created_at= Column(DateTime, index=True)

class ContactMessage(Base):
    __tablename__ = "contact_message"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, index=True)
    message = Column(String)
    lesson_type = Column(String, index=True)
    created_at= Column(DateTime, index=True)
    is_read = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)