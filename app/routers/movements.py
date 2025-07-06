from uuid import UUID
from fastapi import APIRouter, HTTPException, Query
from app.database import SessionDependency
from app.models import Movement, MovementCreate, MovementRead, MovementUpdate
from sqlmodel import select

router = APIRouter(
    prefix="/movements",
    tags=["movements"]
)


@router.get(
    "/",
    response_model=list[MovementRead]
)
async def read_movements(session: SessionDependency, offset: int = 0, limit: int = Query(default=100, le=100)):
    movements = session.exec(select(Movement).offset(offset).limit(limit)).all()
    return movements

@router.post(
    "/",
    response_model=MovementRead
)
async def create_movement(payload: MovementCreate, session: SessionDependency):
    db_movement = Movement.model_validate(payload)
    session.add(db_movement)
    session.commit()
    session.refresh(db_movement)
    return db_movement

@router.get(
    "/{movement_id}",
    response_model=MovementRead
)
async def read_movement(movement_id: UUID, session: SessionDependency):
    movement = session.get(Movement, movement_id)
    if not movement:
        raise HTTPException(status_code=404, detail="Movement not found")
    return movement

@router.patch(
    "/{movement_id}",
    response_model=MovementRead
)
async def update_movement(movement_id: UUID, payload: MovementUpdate, session: SessionDependency):
    db_movement = session.get(Movement, movement_id)
    if not db_movement:
        raise HTTPException(status_code=404, detail="Movement not found")
    movement_data = payload.model_dump(exclude_unset=True)
    db_movement.sqlmodel_update(movement_data)
    session.add(db_movement)
    session.commit()
    session.refresh(db_movement)
    return db_movement

@router.delete("/{movement_id}")
async def delete_movement(movement_id: UUID, session: SessionDependency):
    movement = session.get(Movement, movement_id)
    if not movement:
        raise HTTPException(status_code=404, detail="Movement not found")
    session.delete(movement)
    session.commit()
    return {"ok": True}
