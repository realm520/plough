# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.order import Order  # noqa
from app.models.user import User  # noqa
from app.models.mpcode import MPCode  # noqa
from app.models.master import Master # noqa