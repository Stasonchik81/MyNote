import json
# from classes.note import *
import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import  Column, Integer, String

# строка подключения
SQLALCHEMY_DATABASE_URL = "sqlite:///./db/myNotes.db"

# создаем движок SqlAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#создаем базовый класс для моделей
Base = declarative_base()

# создаем модель, объекты которой будут храниться в бд
class Note(Base):
    __tablename__ = "notes"
 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    message = Column(String)
    date = Column(String)

# создаем таблицы
Base.metadata.create_all(bind=engine)

# создаем сессию подключения к бд
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

# Запись
def write(data):
    date = datetime.datetime.now()
    str_date = date.strftime("%d/%m/%Y")
    note = Note(title=data.title, message=data.message, date=str_date)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note.id

# Чтение
def read(param):
    if param.all:
        data = db.query(Note).all()
    elif param.number:
        data = db.query(Note).filter(Note.id == param.number).first()
    else:
        return -1
    return data

# Удаление
def delete(param):
    if param.all:
        data = db.query(Note).all()
        for n in data:
            db.delete(n)
        db.commit()
    elif param.number:
        data = db.query(Note).filter(Note.id == param.number).first()
        if data != None:
            db.delete(data)
            db.commit()
        else:
            return -1
    else:
        return -1
    return 0

# Редактирование
def edit(param):
    if param.number:
        data = db.query(Note).filter(Note.id == param.number).first()
        if data:
            if param.title:
                data.title = param.title
            if param.message:
                data.message = param.message
            if param.date:
                data.date = param.date #можно сделать проверку на соответствие формату
            db.commit()
        else:
            return -1
    else:
        return -1
    return 0




