import logging
import json
import time
from random import sample
from string import ascii_letters, digits
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from wechatpayv3 import WeChatPay, WeChatPayType

from app import crud, models, schemas
from app.api import deps
from app.core.config import get_app_settings
from app.core.settings.app import AppSettings

router = APIRouter()



@router.get("/summary", response_model=List[schemas.Order])
def read_orders(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve orders (User & SuperUser).
    """


@router.get("/", response_model=List[schemas.Order])
def read_orders(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve orders (User & SuperUser).
    """
    if crud.user.is_superuser(current_user):
        orders = crud.order.get_multi(db, skip=skip, limit=limit)
    else:
        orders = crud.order.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    #FIXME, not check count
    products = crud.product.get_multi(db=db)
    ret_obj = []
    for o in orders:
        for p in products:
            if p.id == o.product_id:
                product = p.name
        ret_obj.append(schemas.Order(
            id=o.id,
            product_id=o.product_id,
            product=product,
            order_number=o.order_number,
            name=o.name,
            sex=o.sex,
            birthday=o.birthday,
            location=o.location,
            amount=o.amount,
            owner_id=o.owner_id,
            master_id=o.master_id,
            divination=o.divination,
            create_time=str(o.create_time),
            pay_time=str(o.pay_time),
            arrange_status=o.arrange_status,
            status=o.status,
            master=o.master.name,
            owner=o.owner.user_name
        ))
    return ret_obj


@router.get("/master", response_model=List[schemas.Order])
def read_orders_master(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_master: models.Master = Depends(deps.get_current_active_master),
) -> Any:
    """
    Retrieve orders (Master).
    """
    orders = crud.order.get_multi_by_master(
        db=db, master_id=current_master.id, skip=skip, limit=limit
    )
    #FIXME, not check count
    products = crud.product.get_multi(db=db)
    ret_obj = []
    for o in orders:
        for p in products:
            if p.id == o.product_id:
                product = p.name
        ret_obj.append(schemas.Order(
            id=o.id,
            product_id=o.product_id,
            product=product,
            order_number=o.order_number,
            name=o.name,
            sex=o.sex,
            birthday=o.birthday,
            location=o.location,
            amount=o.amount,
            owner_id=o.owner_id,
            master_id=o.master_id,
            divination=o.divination,
            create_time=str(o.create_time),
            pay_time=str(o.pay_time),
            arrange_status=o.arrange_status,
            status=o.status,
            master=o.master.name,
            owner=o.owner.user_name
        ))
    return ret_obj

@router.post("/")
def create_order(
    *,
    db: Session = Depends(deps.get_db),
    order_in: schemas.OrderCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
    settings: AppSettings = Depends(get_app_settings)
) -> Any:
    """
    Create new order.
    """
    master = crud.master.get(db=db, id=order_in.master_id)
    if not master:
        raise HTTPException(status_code=404, detail="Master not found")
    product = crud.product.get(db=db, id=order_in.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    order_in.amount = master.price
    order = crud.order.create_with_owner(db=db, obj_in=order_in, owner_id=current_user.id)
    with open(settings.PRIVATE_KEY, "r") as f:
        pkey = f.read()
    wxpay = WeChatPay(
        wechatpay_type=WeChatPayType.APP,
        mchid=settings.MCHID,
        private_key=pkey,
        cert_serial_no=settings.CERT_SERIAL_NO,
        apiv3_key=settings.APIV3_KEY,
        appid=settings.APPID,
        notify_url=settings.NOTIFY_URL,
        cert_dir=settings.CERT_DIR,
        logger=None,
        partner_mode=settings.PARTNER_MODE,
        proxy=None)
    code, message = wxpay.pay(
        description=product.name,
        out_trade_no=order.order_number,
        amount={'total': order.amount}
    )
    result = json.loads(message)
    if code in range(200, 300):
        prepay_id = result.get('prepay_id')
        timearray = time.strptime(order_in.create_time, "%Y-%m-%d %H:%M:%S")
        timestamp = int(time.mktime(timearray))
        noncestr = ''.join(sample(ascii_letters + digits, 8))
        package = 'Sign=WXPay'
        paysign = wxpay.sign([settings.APPID, str(timestamp), noncestr, prepay_id])
        return {'code': 0, 'result': {
            'ordernumber': order.order_number,
            'appid': settings.APPID,
            'partnerid': settings.MCHID,
            'prepayid': prepay_id,
            'package': package,
            'nonceStr': noncestr,
            'timestamp': timestamp,
            'price': order.amount,
            'sign': paysign
        }}
    else:
        return {'code': -1, 'result': {'reason': result.get('code')}}



@router.put("/{id}", response_model=schemas.Order)
def update_order(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    order_in: schemas.OrderUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update an order (superuser).
    """
    order = crud.order.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    # if not crud.user.is_superuser(current_user) and (order.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    order = crud.order.update(db=db, db_obj=order, obj_in=order_in)
    return order


@router.put("/master/{id}", response_model=schemas.Order)
def master_update_order(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    order_in: schemas.OrderUpdateDivination,
    current_master: models.User = Depends(deps.get_current_active_master),
) -> Any:
    """
    Update an order by master.
    """
    order = crud.order.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if order.master_id != current_master.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    if order.status != schemes.order.OrderStatus.init:
        raise HTTPException(status_code=400, detail="Not need divination")
    order = crud.order.updateDivination(db=db, db_obj=order, obj_in=order_in)
    return order


@router.get("/{id}", response_model=schemas.Order)
def read_order_by_id(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get order by ID.
    """
    order = crud.order.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if not crud.user.is_superuser(current_user) and (order.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    #FIXME, not check count
    products = crud.product.get_multi(db=db)
    for p in products:
        if p.id == order.product_id:
            product = p.name
    return schemas.Order(
        id=order.id,
        product_id=order.product_id,
        product=product,
        order_number=order.order_number,
        name=order.name,
        sex=order.sex,
        birthday=order.birthday,
        location=order.location,
        amount=order.amount,
        owner_id=order.owner_id,
        master_id=order.master_id,
        divination=order.divination,
        create_time=str(order.create_time),
        pay_time=str(order.pay_time),
        status=order.status,
        arrange_status=order.arrange_status,
        master=order.master.name,
        owner=order.owner.user_name
    )


@router.delete("/{id}", response_model=schemas.Order)
def delete_order(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete an order.
    """
    order = crud.order.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order = crud.order.remove(db=db, id=id)
    return order
