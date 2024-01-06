from pydantic import BaseModel


class DoneResponse(BaseModel):
    id: int

    class ConfigDict:
        from_attributes = True