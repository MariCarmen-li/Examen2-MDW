from pydantic import BaseModel
class User(BaseModel):
    id: str | None #It's type str or None
    username: str
    email: str
    full_name: str
    disabled: str