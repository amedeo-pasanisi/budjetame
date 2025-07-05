from typing import List
from uuid import UUID
from fastapi import APIRouter
from app.models import Movement

router = APIRouter(
    prefix="/movements",
    tags=["movements"]
)

movements: list[Movement] = []


@router.get(
    "/",
    response_model=List[Movement]
)
async def read_movements():
    return movements

@router.post(
    "/",
    response_model=Movement
)
async def create_movement(payload: Movement):
    movements.append(payload)
    return payload

@router.get(
    "/{movement_id}",
    response_model=Movement
)
async def read_movement(movement_id: UUID):
    for movement in movements:
        if movement.id == movement_id:
            return movement

@router.patch(
    "/{movement_id}",
    response_model=Movement
)
async def update_movement(movement_id: UUID, payload: Movement):
    for idx, movement in enumerate(movements):
        if movement_id == movement.id:
            movements[idx] = payload
            return payload

@router.delete(
    "/{movement_id}",
)
async def delete_movement(movement_id: UUID):
    for idx, movement in enumerate(movements):
        if movement_id == movement.id:
            movements.pop(idx)
