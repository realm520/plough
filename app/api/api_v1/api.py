from fastapi import APIRouter

from app.api.api_v1.endpoints import orders, login, users, masters, utils, pay

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(pay.router, prefix="/pay", tags=["pay"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(masters.router, prefix="/masters", tags=["masters"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
