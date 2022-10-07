from pydantic import BaseModel


class Expression(BaseModel):
    phrase: str
