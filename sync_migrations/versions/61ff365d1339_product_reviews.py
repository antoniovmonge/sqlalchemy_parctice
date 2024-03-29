"""product reviews

Revision ID: 61ff365d1339
Revises: cec120c6ef33
Create Date: 2023-09-20 13:10:30.172743

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61ff365d1339'
down_revision: Union[str, None] = 'cec120c6ef33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products_reviews',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Uuid(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name=op.f('fk_products_reviews_customer_id_customers')),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_products_reviews_product_id_products')),
    sa.PrimaryKeyConstraint('product_id', 'customer_id', name=op.f('pk_products_reviews'))
    )
    op.create_index(op.f('ix_products_reviews_timestamp'), 'products_reviews', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_reviews_timestamp'), table_name='products_reviews')
    op.drop_table('products_reviews')
    # ### end Alembic commands ###
