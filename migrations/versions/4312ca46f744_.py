"""empty message

Revision ID: 4312ca46f744
Revises: 3da6cf7f778c
Create Date: 2016-07-13 23:02:57.708866

"""

# revision identifiers, used by Alembic.
revision = '4312ca46f744'
down_revision = '3da6cf7f778c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_url', sa.Column('is_product', sa.Boolean(), server_default='0', nullable=False))
    op.create_index(op.f('ix_product_url_is_product'), 'product_url', ['is_product'], unique=False)
    op.drop_index('ix_product_url_referrer', table_name='product_url')
    op.drop_column('product_url', 'referrer')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_url', sa.Column('referrer', sa.TEXT(), autoincrement=False, nullable=True))
    op.create_index('ix_product_url_referrer', 'product_url', ['referrer'], unique=False)
    op.drop_index(op.f('ix_product_url_is_product'), table_name='product_url')
    op.drop_column('product_url', 'is_product')
    ### end Alembic commands ###