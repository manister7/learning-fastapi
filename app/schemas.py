from pydantic import BaseModel 
 
 
class StudentCreate(BaseModel): 
    name: str 
    email: str 
    course: str 
 
 
class StudentResponse(BaseModel): 
    id: int 
    name: str 
    email: str 
    course: str 
 
    model_config = { 
        "from_attributes": True 
    } 