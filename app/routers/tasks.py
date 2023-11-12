from fastapi import APIRouter
from ..dtos.tasks import CreateTaskDto
from ..prisma import prisma

router = APIRouter()

@router.get('/tasks')
async def fetch_task():
    result = await prisma.task.find_many(order={'id':'asc'})
    return result

@router.get('/tasks/{category}')
async def fetch_member(category: str):
    result = await prisma.task.find_many(where={'subject': category})
    if result:
        return result
    else:
        return []

@router.get('/tasks/{id}')
async def fetch_member_id(id: int):
    result = await prisma.member.find_first(where={'id': int(id)})
    return result

@router.post("/tasks")
async def read_root(memberDto: CreateTaskDto):
    await prisma.task.create(data={"subject": memberDto.subject, "description": memberDto.description, "category": memberDto.category})
    return {
        'message': 'สร้างข้อมูลสำเร็จ'
    }
@router.put('/tasks/{id}/star')
async def update_member(id: int):
    result = await prisma.task.find_first(where={'id': int(id)})
    await prisma.task.update(where={'id': result.id}, data={"star": not result.star})
    return {
        'message': 'ติดดาวข้อมูลสำเร็จ'
    }

@router.put('/tasks/{id}/check')
async def update_member(id: int):
    result = await prisma.task.find_first(where={'id': int(id)})
    await prisma.task.update(where={'id': result.id}, data={"check": not result.check})
    return {
        'message': 'เช็คข้อมูลสำเร็จ'
    }

@router.put('/tasks/{id}/read')
async def update_member(id: int):
    result = await prisma.task.find_first(where={'id': int(id)})
    await prisma.task.update(where={'id': result.id}, data={"read": True})
    return {
        'message': 'อ่านข้อมูลสำเร็จ'
    }

@router.put('/tasks/{id}')
async def update_member(id: int, memberDto: CreateTaskDto):
    await prisma.task.update(where={'id': int(id)}, data={"subject": memberDto.subject, "description": memberDto.description, "category": memberDto.category})
    return {
        'message': 'อัปเดตข้อมูลสำเร็จ'
    }

@router.delete("/tasks/{id}")
async def delete_member(id):
    print(id)
    await prisma.task.delete(where={'id': int(id)})
    return {
        'message': 'ลบข้อมูลสำเร็จ'
    }

