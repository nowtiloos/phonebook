import uuid

from pydantic import BaseModel


class Contact(BaseModel):
    id: uuid.UUID
    surname: str
    name: str
    patronymic: str
    organization: str
    work_phone: str
    personal_phone: str

    class Config:
        from_attributes = True
