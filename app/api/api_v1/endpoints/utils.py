from typing import Any

from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.api import deps
# from app.core.celery_app import celery_app
from app.utils import send_test_email

router = APIRouter()


@router.post("/test-celery/", response_model=schemas.Msg, status_code=201)
def test_celery(
    msg: schemas.Msg,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Test Celery worker.
    """
    # celery_app.send_task("app.worker.test_celery", args=[msg.msg])
    return {"msg": "Word received"}


@router.post("/test-email/", response_model=schemas.Msg, status_code=201)
def test_email(
    email_to: EmailStr,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Test emails.
    """
    send_test_email(email_to=email_to)
    return {"msg": "Test email sent"}

@router.get("/get-latest-version/", response_model=schemas.Version, status_code=201)
def get_latest_version(
    product: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get latest version.
    """
    version = crud.version.get_by_product(db=db, product=product)
    return version

@router.post("/release-version/", response_model=schemas.Version)
def release_version(
    obj_in: schemas.VersionCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Release a new version.
    """
    version = crud.version.release_version(db=db, obj_in=obj_in)
    return version