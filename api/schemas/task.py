from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    class ConfigDict:
        from_attributes = True


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    class ConfigDict:
        from_attributes = True
