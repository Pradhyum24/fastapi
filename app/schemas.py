from pydantic import BaseModel,EmailStr,conint
from datetime import datetime
from typing import Optional

class CreateUser(BaseModel):

    email : EmailStr
    password : str

class UserOut(BaseModel):
    id : int
    email:  EmailStr
    created_at: datetime
    class Config:
        from_attributes = True

class UserLogin(BaseModel):

    email : EmailStr
    password : str


class PostBase(BaseModel):

    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id : int
    created_at: datetime
    owner_id : int
    owner : UserOut

     
    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True

class Token(BaseModel):

    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[int] = None
    
class Vote(BaseModel):
    post_id : int
    dir: conint(ge=0, le=1)  # Allows only 0 or 1
