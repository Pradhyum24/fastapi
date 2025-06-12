from fastapi import FastAPI, Response, status, HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import engine,get_db
from .. import models,schemas,utils


router = APIRouter(
    prefix="/users",tags=["Users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    user.password = utils.hash(user.password)
    new_user = models.User(**user.model_dump())
    
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Failed to create user:  The email already exists.")
    
    return new_user


@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id: int,db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"User with {id} does not exist")
    return user

    