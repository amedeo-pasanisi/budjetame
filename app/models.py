from datetime import datetime, timezone
from typing import Literal
from uuid import UUID, uuid4
from pydantic import ConfigDict, alias_generators
from sqlmodel import SQLModel, Field, String

class MovementBase(SQLModel):
    model_config = ConfigDict(
        alias_generator=alias_generators.to_camel,
        populate_by_name=True
    )
    amount: float = Field(description="Amount of euros. Positive if gained, negative if lost.")
    description: str | None = Field(default=None, description="How or why the amount was spent or gained.")
    type: Literal["gain", "loss", "movement"] = Field(sa_type=String, default="loss")

class Movement(MovementBase, table=True):
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))

class MovementCreate(MovementBase):
    pass

class MovementUpdate(SQLModel):
    model_config = ConfigDict(
        alias_generator=alias_generators.to_camel,
        populate_by_name=True
    )
    amount: float | None = Field(default=None, description="Amount of euros. Positive if gained, negative if lost.")
    description: str | None = Field(default=None, description="How or why the amount was spent or gained.")
    type: Literal["gain", "loss", "movement"] | None = Field(default=None)

class MovementRead(MovementBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    
