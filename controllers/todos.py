from fastapi import APIRouter

from services.todos_sa import TodoService

router = APIRouter(
    prefix='/api/todos'
)


@router.get('/')
async def get_all_todos(service: TodoService):
    todos = service.get_all()
    return {'todos': todos}
