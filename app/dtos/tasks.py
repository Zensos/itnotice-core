from pydantic import BaseModel

class CreateTaskDto(BaseModel):
    subject: str
    description: str
    category: str