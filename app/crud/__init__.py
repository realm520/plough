from .crud_order import order
from .crud_user import user
from .crud_mpcode import mpcode
from .crud_master import master
from .crud_product import product
from .crud_comment import comment
from .crud_version import version

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
