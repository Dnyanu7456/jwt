# crud.py
from sqlalchemy.orm import Session
import models, schemas, auth

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not auth.verify_password(password, user.hashed_password):
        return False
    return user

def create_note(db: Session, owner_id: int, note: schemas.NoteCreate):
    db_note = models.Note(title=note.title, content=note.content, owner_id=owner_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_notes_for_user(db: Session, owner_id: int):
    return db.query(models.Note).filter(models.Note.owner_id == owner_id).all()

def get_note(db: Session, note_id: int, owner_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == owner_id).first()

def delete_note(db: Session, note_id: int, owner_id: int):
    note = get_note(db, note_id, owner_id)
    if note:
        db.delete(note)
        db.commit()
    return note
