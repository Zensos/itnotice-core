from fastapi import APIRouter
from ..dtos.member import CreateMemberDto
from ..prisma import prisma

router = APIRouter()

@router.get('/')
async def fetch_task():
    # await p risma.task.create(data={'subject': 'ITF', 'description': 'ออปติมัสไปม์', 'category': 'Primary', 'date': datetime.datetime.now()})
    result = await prisma.task.find_many(order={'id':'asc'})
    return result

@router.get('/{category}')
async def fetch_member(category: str):
    result = await prisma.task.find_many(where={'subject': category})
    if result:
        return result
    else:
        return []

@router.get('/{id}')
async def fetch_member_id(id: int):
    result = await prisma.member.find_first(where={'id': int(id)})
    return result

@router.post("/createmember")
async def read_root(memberDto: CreateMemberDto):
    await prisma.member.create(data={"username": memberDto.username, "password": memberDto.password, "balance": 0, "email": memberDto.email})
    return {
        'message': 'Sucessfully Create Member'
    }

@router.put('/updatemember/{id}')
async def update_member(id: int, memberDto: CreateMemberDto):
    await prisma.member.update(where={'id': int(id)}, data={"username": memberDto.username, "email": memberDto.email, "password": memberDto.password})
    return {
        'message': 'Sucessfully Updated'
    }

@router.delete("/deletemember/{id}")
async def delete_member(id):
    print(id)
    await prisma.member.delete(where={'id': int(id)})
    return {
        'message': 'Sucessfully Deleted'
    }

