from fastapi import APIRouter
from src.functions import create_account, create_folders ,save_mail ,save_server ,send_mail

router = APIRouter(
    prefix='/mail',
    tags=['Mail']
)

router.post('/account/create')(create_account.create_account)
router.post('/folders/create')(create_folders.create_folder)
router.post('/save')(save_mail.save_mail)
router.post('/server/save')(save_server.save_server)
router.post('/send')(send_mail.send_mail)