from fastapi import APIRouter
from src.functions.server import save_server, get_servers,create_account,delete_account,update_account,delete_server,update_server,get_accounts

router = APIRouter(
    prefix="/server",
    tags=["server"],
)

router.post("")(save_server)
router.get("/{owner}")(get_servers)
router.post("/accounts")(create_account)
router.get("/{mail_server}/accounts")(get_accounts)
router.delete("/{mail_server}/accounts/{id}")(delete_account)
router.put("/{mail_server}/accounts/{id}")(update_account)
router.delete("/{id}")(delete_server)
router.put("/{id}/{owner}")(update_server)

