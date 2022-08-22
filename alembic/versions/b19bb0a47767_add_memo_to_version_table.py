"""add memo to version table

Revision ID: b19bb0a47767
Revises: ab3c5cc144a8
Create Date: 2022-08-22 10:18:00.076818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b19bb0a47767'
down_revision = 'ab3c5cc144a8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('version', sa.Column('memo', sa.String(), nullable=True))
    op.alter_column('version', 'desc',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('version', 'desc',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('version', 'memo')
    # ### end Alembic commands ###