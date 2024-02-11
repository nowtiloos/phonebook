from pydantic import BaseModel


class Contact(BaseModel):
    name: str
    patronymic: str
    surname: str
    organization: str
    work_phone: str
    personal_phone: str

    class Config:
        from_attributes = True


