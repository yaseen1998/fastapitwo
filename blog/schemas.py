
from typing import Optional
from pydantic import BaseModel
class BlogSchema(BaseModel):
    title: str
    body: str
