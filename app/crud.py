from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_job_application(db: Session, app: schemas.JobApplicationCreate, user_id: int):
    db_app = models.JobApplication(**app.dict(), user_id=user_id)
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app
