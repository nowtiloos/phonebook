from pydantic import BaseModel


class Contact(BaseModel):
    name: str
    patronymic: str
    surname: str
    organization: str
    work_phone: int
    personal_phone: int

    class Config:
        from_attributes = True


headers = list(Contact.__annotations__)
