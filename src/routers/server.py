from fastapi import APIRouter
from src.functions import save_server

router = APIRouter(
    prefix='/server',
    tags=['Server']
)

router.post('/save')(save_server.save_server)
