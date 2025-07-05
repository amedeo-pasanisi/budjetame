from datetime import datetime
from uuid import UUID
from sqlmodel import SQLModel, Field


class Movement (SQLModel):
    id: UUID = Field(primary_key=True)
    amount: float = Field(description="Amount of euros. Positive if gained, negative if lost.")
    description: str = Field(description="How or why the amount was spent or gained.")
    created_at: datetime
    updated_at: datetime
    
