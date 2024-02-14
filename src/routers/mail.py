from fastapi import APIRouter
from src.functions.mail import create_folder,save_mail,send_mail

router = APIRouter(
    prefix="/mail",
    tags=["mail"],
)

router.post("/folder")(create_folder)
router.post("/{folder_id}")(save_mail)
router.post("/folder/{folder_id}/send")(send_mail)