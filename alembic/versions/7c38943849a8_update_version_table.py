"""update version table

Revision ID: 7c38943849a8
Revises: 1ffc67b64581
Create Date: 2022-08-19 14:47:06.365539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c38943849a8'
down_revision = '1ffc67b64581'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('version',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product', sa.String(), nullable=False),
    sa.Column('vstr', sa.String(), nullable=False),
    sa.Column('desc', sa.String(), nullable=False),
    sa.Column('release_time', sa.Integer(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_version_id'), 'version', ['id'], unique=False)
    op.create_index(op.f('ix_version_product'), 'version', ['product'], unique=False)
    op.create_index(op.f('ix_version_release_time'), 'version', ['release_time'], unique=False)
    op.create_index(op.f('ix_version_vstr'), 'version', ['vstr'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_version_vstr'), table_name='version')
    op.drop_index(op.f('ix_version_release_time'), table_name='version')
    op.drop_index(op.f('ix_version_product'), table_name='version')
    op.drop_index(op.f('ix_version_id'), table_name='version')
    op.drop_table('version')
    # ### end Alembic commands ###