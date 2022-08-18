"""add price for master table

Revision ID: 5b96290d5336
Revises: c07b0c09cc50
Create Date: 2022-08-18 11:29:58.441851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b96290d5336'
down_revision = 'c07b0c09cc50'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('master', sa.Column('price', sa.Integer(), comment='排盘价格'))
    op.add_column('order', sa.Column('product_id', sa.Integer(), nullable=True))
    op.add_column('order', sa.Column('channel', sa.Integer(), nullable=True, comment='渠道'))
    op.add_column('order', sa.Column('shareRate', sa.Integer(), nullable=True, comment='订单分成'))
    op.add_column('order', sa.Column('arrange_status', sa.Integer(), nullable=True, comment='排盘状态：0 - 未排盘, 1 - 已排盘'))
    op.alter_column('order', 'status',
               existing_type=sa.INTEGER(),
               comment='订单状态：0 - 未确认, 1 - 已支付, 3 - 作废, 4 - 退款',
               existing_comment='状态：0 - 未确认, 1 - 已支付, 2 - 已确认, 3 - 作废',
               existing_nullable=True)
    op.drop_index('ix_order_master_id', table_name='order')
    op.drop_index('ix_order_product_name', table_name='order')
    op.create_index(op.f('ix_order_product_id'), 'order', ['product_id'], unique=False)
    op.create_foreign_key(None, 'order', 'master', ['master_id'], ['id'])
    op.drop_column('order', 'product_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('product_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'order', type_='foreignkey')
    op.drop_index(op.f('ix_order_product_id'), table_name='order')
    op.create_index('ix_order_product_name', 'order', ['product_name'], unique=False)
    op.create_index('ix_order_master_id', 'order', ['master_id'], unique=False)
    op.alter_column('order', 'status',
               existing_type=sa.INTEGER(),
               comment='状态：0 - 未确认, 1 - 已支付, 2 - 已确认, 3 - 作废',
               existing_comment='订单状态：0 - 未确认, 1 - 已支付, 3 - 作废, 4 - 退款',
               existing_nullable=True)
    op.drop_column('order', 'arrange_status')
    op.drop_column('order', 'shareRate')
    op.drop_column('order', 'channel')
    op.drop_column('order', 'product_id')
    op.drop_column('master', 'price')
    # ### end Alembic commands ###